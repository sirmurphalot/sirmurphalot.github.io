---
layout: default
title: Guna Prasaad | Blog
---
<h3>Newest</h3>
<p>Most recent blog posts.</p>
<ul class="posts">
  {% for post in site.posts limit:5 %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{post.url}}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
