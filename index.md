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
        <img src="https://sirmurphalot.github.io/assets/me.jpg" width="170px" height="200px">
    </div>
    <div class="contact">
        <font size="+2">Alexander C. Murph</font> <br>
        Statistics and Operations Research PhD Student<br>
        Chapel Hill, NC<br>
        <a href="mailto:acmurph@live.unc.edu"> <img src="{{site.url}}css/icons/gmail.jpg"  class="icon"> </a>
        <a href="https://twitter.com/sirmurphalot"><img src="{{site.url}}css/icons/twitter.jpg"  class="icon"> </a>
        <a href="https://www.linkedin.com/in/alexander-murph-a39772b0/"><img src="{{site.url}}css/icons/linkedin.jpg"  class="icon"> </a>
        <a href="https://github.com/sirmurphalot"><img src="{{site.url}}css/icons/github.png" class="icon"></a>
    </div>
</div>
<style>
div {
  background-image: 'background.png';
}
</style>
<div class="homecontent">
    <p>
    <h3>Research Interests</h3>
    I develop novel fiducial approaches to classical inferential problems, and illustrate the usefulness in context to current methods.  I'm expecially interested in exploring recent work on admissibility of models used to enhance, and even replace, ubiquitous sparsity assumptions. I am further actively researching how to use the EAS methodology for model selection with Gaussian Graphical Models.
</p>
<p>
    <h3>Teaching</h3>
    This semester, I am assisting with UNC's Machine Learning class in the Statistics and Operations Research Department.  My office hours are Tuesdays from 9:30am-10:30am, and Fridays from 10:30am-11:30am in Hanes B46.
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
    I'm a born-and-raised Pittsburgh-er who traveled down south to pursue my dream of being a Statistics professor.  When I'm not thinking about math and coding, I'm swimming, dancing, and singing loudly in the shower.
    </p>
</div>
