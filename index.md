---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: default
title: Alexander Murph
permalink: 
---
<div class="banner">
    <div class="photo">
        <img src="https://sirmurphalot.github.io/assets/me.jpg" width="140px" height="140px">
    </div>
    <div class="contact">
        <i>Graduate Student</i> <br>
        Statistics and Operations Research<br>
        Chapel Hill, NC<br>
        <a href="mailto:acmurph@live.unc.edu"> <img src="{{site.url}}css/icons/gmail.jpg"  class="icon"> </a>
        <a href="https://twitter.com/sirmurphalot"><img src="{{site.url}}css/icons/twitter.jpg"  class="icon"> </a>
        <a href="https://www.linkedin.com/in/alexander-murph-a39772b0/"><img src="{{site.url}}css/icons/linkedin.jpg"  class="icon"> </a>
        <a href="https://github.com/sirmurphalot"><img src="{{site.url}}css/icons/github.png" class="icon"></a>
    </div>
</div>
<div class="homecontent">
    <p>
    <h3>Research Interests</h3>
    I develop novel fiducial approaches to classical inferential problems, and illustrate the usefulness in context to current methods.  I'm expecially interested in exploring recent work on admissibility of models used to enhance, and even replace, ubiquitous sparsity assumptions. I am further actively researching how to use the EAS methodology for model selection with Gaussian Graphical Models.
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
    Hey there.
    </p>
</div>
