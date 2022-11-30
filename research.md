---
layout: default
title: Alexander Murph | Research
permalink: research
bibliography: assets/references.bib  
---

<div><h2>Research Interests</h2><br></div>
<p>~~~~~My research focuses on developing statistical methodologies that are theoretically attractive and broadly applicable, often taking a Bayesian or Generalized Fiducial perspective.  I believe a ``sweet spot" exists where my passion for theoretical statistics research leads to positive human impacts, and I am looking for complicated and unique applications in pursuit of this intersection.  In my consulting work for the Mayo Clinic, I develop a novel Bayesian changepoint detection system that meets a real need for the in-process models in its hospitals.  This method detects a broad class of changes in longitudinal data while simultaneously determining a changepoint's cause.  An additional research interest of mine is Generalized Fiducial Inference (GFI), which is a modern perspective on Fisher's fiducial argument [@-fisher1935; @-hannig2016].  My theoretical work uses differential geometry to define a Generalized Fiducial Distribution (GFD) on smooth manifolds.  This distribution has strong inferential capabilities on a large class of constrained parameter spaces and exhibits many useful theoretical qualities. </p>
<div><br><hr><hr><br><h2>Current Projects</h2></div>
<ul>
<br>
<li> 
<h3>Generalized Fiducial Inference</h3> 
  <p>As famously put by J. Savage in his 1961 paper, fiducial statistics was R.A. Fisher's <q>bold attempt to make the Bayesian omelet without breaking the Bayesian eggs.</q>  Fisher's fiducial school is precisely that.  One can define a posterior-like distribution of a target parameter (i.e. the omelet) without having to arbitrary select a prior distribution (i.e. breaking the eggs). After Fisher's death, some statisticians declared the approach to be "largely of historical importance" or, put more directly, "dead."  While a whole generation of statisticians abandoned Fisher's "biggest blunder," the approach has seen modern success with updates to Fisher's original switching principle. As Bradley Efron put it in his 1996 Fisher lecture, "maybe Fisher’s biggest blunder will become a big hit in the 21st century!" </p>
  <p>Many of my theoretical projects involve fiducial inference in some way.  I was able to express my enthusiasm for the fiducial method in an early project during my Ph.D., which involved writing a paper on new fiducial approaches to classical inferential problems (see publications). </p>
</li>
<br>

<li> 
<h3>Bayesian Changepoint Detection</h3> 
  <p>When a predictive model is in production, it must be monitored over time to ensure that its performance does not suffer from drift or abrupt changes to data.  Typically this is done by evaluating the algorithm’s predictions to outcome data and ensuring that the algorithm maintains an acceptable level of accuracy over time.  However, it is far preferable to learn about major changes in the input data that could affect the models performance in real-time, long before learning that the performance of the model itself has dropped by monitoring outcome data.  Thus, there is large need for robust, real-time monitoring of high dimensional input data over time.  As part of my position at the Mayo Clinic, I study the problem of change point detection on high-dimensional longitudinal data with mixed variable types and missing values.  Our solution to this problem involves fitting an array of Mixture Gaussian Graphical Models to groupings of homogeneous data in time, called regimes, which we model as the observed states of a Markov process with unknown transition probabilities.   The primary goal of this model is to identify when there is a regime change, as this indicates a significant change in the input data distribution.  To handle the messy nature of real-world data which has mixed continuous/discrete variable types, missing data, etc., we take a Bayesian latent variable approach. This affords us flexibility to handle missing values in a principled manner, while simultaneously providing a way to encode discrete and censored values into a continuous framework. We take this approach a step further by encoding the missingness structure, which allows our model to then detect major changes in the patterns of missingness, in addition to the structure of the data distributions themselves. This approach has seen extraordinary success on simulated data; we are presently applying it to an in-production model at the Mayo Clinic in Rochester. </p>
</li>
<br>

<li>
  <h3>Fiducial Statistics on Riemannian Manifolds</h3> 
  <p>I am broadly interested in the intersection between classical Geometry and modern Statistics.  My current project explores this intersection by developing a Generalized Fiducial Distribution (GFD) on constrained parameter spaces.  Specifically, I am interested in the case where the parameter space can be expressed as a differentiable level set.  The general form of the GFD developed by <a href="https://hannig.cloudapps.unc.edu/publications/HannigIyerLaiLee2016.pdf">Hannig et. al 2016</a> can be naturally constrained to a such space.  This "constrained GFD" inherits many desirable asymptotic qualities from the original GFD, and has shown promising results on simulated data.</p>
  </li>
<br>
<li>
    
  <h3>EAS with Graphical Models</h3> 
  <p>One overarching aim of my research is to bring what has come to be known as the EAS methodology for model selection to GGMs, which will introduce a creative new means for graphical selection in GGMs, as well as a new way to predict general precision matrices. The EAS methodology leverages notions of redundancy to manage the size of the sample space of possible models: $M$. The beauty of this approach is that it realistically expects and addresses the ubiquitous issue of huge numbers of variables $p$ and sample sets $n$: a problem that causes the probability of every possible model (including the true model $M_0$) to tend towards zero. In numerous cases, this approach gives strong consistency of the posterior-like probability of the true oracle model.  Another particularly attractive aspect of EAS is that it uses recent advances in Generalized Fiducial Inference (GFI) to derive a probability distribution of possible models, without the need for an arbitrary prior. This opens up a means for analysis beyond mere point estimation, such as confidence regions for the true model $M_0$. </p>
  
  If you're interested, check out these papers:
  <span><a href="https://arxiv.org/abs/1906.04812">[arXiv]</a></span>
  <span><a href="https://projecteuclid.org/euclid.aos/1550026855">[AOS]</a></span>
</li>
<br><hr><br>
</ul>

