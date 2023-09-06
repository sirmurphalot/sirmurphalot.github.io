---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Alexander C Murph
permalink: 
---
<div class="banner">
    <div class="photo">
        <img src="https://sirmurphalot.github.io/assets/me.jpg" width="207px" height="200px">
    </div>
    <div class="contact">
        <font size="+2">Alexander C. Murph</font> <br>
        Postdoc at Los Alamos National Lab<br>
        Research Consultant at the Mayo Clinic<br>
        Santa Fe, NM <br>
        <a href="mailto:acmurph@live.unc.edu"> <img src="{{site.url}}css/icons/gmail.jpg"  class="icon"> </a>
        <a href="https://www.linkedin.com/in/alexander-murph-a39772b0/"><img src="{{site.url}}css/icons/linkedin.jpg"  class="icon"> </a>
        <a href="https://github.com/sirmurphalot"><img src="{{site.url}}css/icons/github.png" class="icon"></a>
        <a href="https://www.imdb.com/name/nm7015552/"><img src="{{site.url}}css/icons/imdb.png" class="icon"></a>
    </div>
</div>
<div class="homecontent">
    <br>
    <br>
    <p>
    <h3>Research Interests</h3>
    I develop novel fiducial approaches to classical inferential problems and illustrate the usefulness in context to current methods.  I am broadly interested in the intersection between classical Geometry and modern Statistics, especially from the fiducial perspective.  My research often also involves Gaussian Graphical Models (GGMs); under this wide umbrella, I am currently engaged in projects that are both purely theoretical and applied.  My applied work on GGMs is with the Mayo Clinic and involves detecting drift or abrupt changes to data.
</p>
<p>
    <h3>Teaching</h3>
    Due to funding from the Mayo Clinic, I will not be teaching for the remainder of my PhD program.  I report this news with great enthusiasm, yet still with some melancholy.  Teaching is a passion of mine and I know that it will be in my future.
</p>
    <p>
    <h3>Recent News</h3>
<table class="news">
  {% assign news = (site.data.news | sort: 'date') | reverse %} {% for n in news limit:5 %}
  <tr>
    <td class="date">{{ n.date | date_to_string }} </td> 
    <td class="description"> {{ n.description | markdownify }} </td>
  </tr>
  {% endfor %}
</table>
<a href="{{site.url}}news.html">View All</a> <br>
    </p>
    <p>
    <h3>Brief Bio</h3>
    I'm a born-and-raised Pittsburgh-er who traveled down south to pursue my dream of being a Statistics professor.  When that dream changed, I headed westward.  When I'm not thinking about math and coding, I'm swimming, dancing, and singing loudly in the shower.
    </p>
    <b>Erdös-Bacon Number</b>: 5
</div>
