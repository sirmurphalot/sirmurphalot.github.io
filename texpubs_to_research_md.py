#!/usr/bin/env python3
"""
Transform publications.tex -> HTML block inside research.md.

Assumptions:
- publications.tex contains:
  - \\begin{etaremune} ... \\item ... \\end{etaremune}
  - then \\textit{Manuscripts in review/preparation:}
  - then \\begin{itemize} ... \\item ... \\end{itemize}

What it does:
- Parses \\item entries from both lists
- Converts a subset of LaTeX to HTML
- Wraps your name "A.C. Murph" in <b class="emerald-text">...</b>
- Replaces content between <!-- PUBS_START --> and <!-- PUBS_END --> in research.md
"""

from __future__ import annotations

import re
from pathlib import Path
from html import escape

NAME_VARIANTS = {
    "A.C. Murph",
    "A. C. Murph",
    "Alexander C Murph",
    "Alexander C. Murph",
}

PUBS_START = "<!-- PUBS_START -->"
PUBS_END = "<!-- PUBS_END -->"

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")

def write_text(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8")

def extract_env_items(tex: str, env: str) -> list[str]:
    """
    Returns raw item strings inside a LaTeX environment:
      \\begin{env} ... \\item ... \\end{env}
    Each item is returned as a single string (newlines collapsed).
    """
    m = re.search(rf"\\begin\{{{re.escape(env)}\}}(.*?)\\end\{{{re.escape(env)}\}}", tex, flags=re.S)
    if not m:
        return []
    body = m.group(1).strip()

    # Split on \item occurrences; keep only non-empty chunks
    chunks = re.split(r"\n\s*\\item\s*", "\n" + body)
    items = [c.strip() for c in chunks if c.strip()]
    # Collapse whitespace
    items = [re.sub(r"\s+", " ", it).strip() for it in items]
    return items

def latex_basic_to_html(s: str) -> str:
    """
    Tailored LaTeX -> HTML converter for publications.tex patterns.
    """

    # 1) Remove surrounding math mode $...$ (you use it mostly for dagger/star annotations)
    # Do this early so we can parse what's inside.
    s = s.replace("$", "")

    # 2) Normalize common LaTeX wrappers around names:
    #    \text{\me{A.C. Murph}}  -> A.C. Murph
    #    \text{Beesley}         -> Beesley
    s = re.sub(r"\\text\{\\me\{([^}]*)\}\}", r"\1", s)
    s = re.sub(r"\\text\{([^}]*)\}", r"\1", s)
    s = re.sub(r"\\me\{([^}]*)\}", r"\1", s)

    # 3) Turn \& into "and"
    s = s.replace(r"\&", "and")

    # 4) Convert bold/italic/smallcaps
    s = re.sub(r"\\textbf\{([^}]*)\}", r"<b>\1</b>", s)
    s = re.sub(r"\\textit\{([^}]*)\}", r"<i>\1</i>", s)
    s = re.sub(r"\\textsc\{([^}]*)\}", r'<span style="font-variant: small-caps;">\1</span>', s)

    # 5) Convert LaTeX star/dagger markers into unicode, then into superscripts
    # Handle both ^\star and ^\dagger and ^{...}
    s = s.replace(r"\star", "★").replace(r"\dagger", "†")
    s = re.sub(r"\^\{([^}]*)\}", r"<sup>\1</sup>", s)
    s = re.sub(r"\^([★†])", r"<sup>\1</sup>", s)

    # 6) Remove spacing commands
    s = s.replace(r"\quad", " ")
    s = s.replace(r"\,", " ")
    s = s.replace("~", " ")

    # 7) Cleanup stray backslashes/tabs that sometimes appear from copy/paste
    s = s.replace("\t", " ")
    s = re.sub(r"\\+", "", s)  # remove any remaining lone backslashes

    # 8) Collapse whitespace
    s = re.sub(r"\s{2,}", " ", s).strip()

    return s


def emphasize_name(html: str) -> str:
    """
    Wrap your name in <b class="emerald-text">...</b> wherever it appears.
    """
    # We do a conservative replace to avoid wrapping inside tags repeatedly.
    for nv in sorted(NAME_VARIANTS, key=len, reverse=True):
        html = re.sub(
            rf"(?<![>\w]){re.escape(nv)}(?![\w<])",
            rf'<b class="emerald-text">{nv}</b>',
            html,
        )
    return html

def item_to_li(item_tex: str, add_links: bool = False) -> str:
    """
    Convert one \\item entry to <li>...</li>.
    For now, we do not auto-generate link blocks because publications.tex
    doesn’t contain link metadata. (You can extend later.)
    """
    html = latex_basic_to_html(item_tex)
    html = emphasize_name(html)

    # Optional: normalize "(202x)." to "(202x)." (already), and ensure sentence spacing
    html = html.replace(" .", ".").replace(" ,", ",")

    return f"  <li>\n      {html}\n  </li>"

def build_publications_block(pubs_items: list[str], review_items: list[str]) -> str:
    pubs_li = "\n".join(item_to_li(it) for it in pubs_items)
    review_li = "\n".join(item_to_li(it) for it in review_items)

    block = f"""
<h3><i>Publications</i></h3>
<p style="margin-top: 0.25rem;">
  <span title="Co-first author">★</span> Co-first author.&nbsp;&nbsp;
  <span title="Graduate student working under my supervision">†</span> Graduate student working under my supervision.
</p>

<u>Accepted Manuscripts</u>:
<ol reversed>
{pubs_li}
</ol>

<u>Manuscripts in review/preparation</u>:
<ul>
{review_li}
</ul>
""".strip() + "\n"
    return block

def replace_between_markers(doc: str, start: str, end: str, replacement: str) -> str:
    if start not in doc or end not in doc:
        raise RuntimeError(f"Markers not found. Expected both {start} and {end}.")
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), flags=re.S)
    return pattern.sub(start + "\n" + replacement + end, doc, count=1)

def main() -> None:
    publications_tex = Path("publications.tex")
    research_md = Path("research.md")

    tex = read_text(publications_tex)

    pubs_items = extract_env_items(tex, "etaremune")
    review_items = extract_env_items(tex, "itemize")

    if not pubs_items:
        raise RuntimeError("No items found in etaremune. Check publications.tex formatting.")
    if not review_items:
        # It’s okay if you temporarily have none, but usually you do.
        review_items = []

    new_block = build_publications_block(pubs_items, review_items)

    md = read_text(research_md)
    updated = replace_between_markers(md, PUBS_START, PUBS_END, new_block)

    write_text(research_md, updated)
    print("✅ Updated research.md publications section.")

if __name__ == "__main__":
    main()
