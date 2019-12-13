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
    I am a Graduate Student of <a href="http://www.cs.washington.edu/">Computer Science</a> at the <a href="http://www.washington.edu">University of Washington</a>. I am a part of the <a href="http://db.cs.washington.edu/">UW Database Lab</a> working with <a href="https://homes.cs.washington.edu/~akcheung/">Prof. Alvin Cheung</a> and <a href="https://homes.cs.washington.edu/~suciu/">Prof. Dan Suciu</a>. In the summer of 2017, I interned at <a href="https://www.microsoft.com/en-us/research/lab/microsoft-research-redmond/">Microsoft Research Redmond</a> with <a href="https://www.microsoft.com/en-us/research/people/badrishc/">Badrish Chandramouli</a> on building a state-of-the-art key-value store called <a href="https://www.microsoft.com/en-us/research/project/faster/">FASTER</a>. Previously, I was a Research Fellow in the <a href="http://research.microsoft.com/en-us/groups/plato/">Programming Languages and Tools</a> group at <a href="http://research.microsoft.com/en-us/labs/india/">Microsoft Research India</a>, where I built a scalable low-latency ordered stream processing system with <a href="http://research.microsoft.com/en-us/people/grama/">Dr. Ganesan Ramalingam</a>. I obtained my undergraduate degree from IIT Bombay, where I worked with <a href="http://www.cse.iitb.ac.in/~sudarsha/">Prof. S. Sudarshan</a> on I/O optimal index structures for key value stores. I spent the first eighteen years of my life in the <a href="https://www.facebook.com/mycitychennai/">beautiful</a> city of Madras (Chennai) in the southern part of India.
    </p>
</div>
