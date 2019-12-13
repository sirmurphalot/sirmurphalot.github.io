---
layout: default
title: Guna Prasaad | Research
permalink: research
---

<div><h2>Research Interests</h2><br></div>
<p>My research interests span Database Management Systems, Programming Languages and Distributed Systems. </p>
<div><br><hr><hr><br><h2>Current Projects</h2></div>
<ul>
<br>
<li>
  <p>
  <h3>STRIFE: A Novel Transactional Engine</h3> <br>
  Research in transaction processing has made significant progress in improving the performance of multi-core in-memory transactional systems. However, the focus has mainly been on low-contention workloads. Modern transactional systems perform poorly on workloads with transactions accessing a few highly contended data items.  We observe that most transactional workloads, including those with high contention, can be divided into clusters of data conflict-free transactions and a small set of residuals. </p>
  <p>In this project, we introduce a new concurrency control protocol called STRIFE that leverages the above observation. STRIFE executes transactions in batches, where each batch is partitioned into clusters of conflict-free transactions and a small set of residual transactions. The conflict-free clusters are executed in parallel without any concurrency control, followed by executing the residual cluster either serially or with concurrency control. We present a low-overhead algorithm that partitions a batch of transactions into clusters that do not have cross-cluster conflicts and a small residual cluster. We evaluate STRIFE against the optimistic concurrency control protocol and several variants of two-phase locking, where the latter is known to perform better than other concurrency protocols under high contention, and show that STRIFE can improve transactional throughput by up to 2$\times$. </p>
  <span><a href="https://arxiv.org/abs/1810.01997">[arXiv]</a></span>
  <span><a href="{{site.url}}assets/STRIFE-quals.pptx">[Slides]</a></span>
</li>
<br><hr><br>
<li>
<p>
<h3>Concurrent Prefix Recovery: Performing CPR on a Database</h3><br>
With increasing multi-core parallelism, modern databases and key-value stores have been designed for scalability, and yield very high throughput for the in-memory working set. These systems typically depend on group commit using write-ahead-logging to provide durability and crash recovery. However, write-ahead logging incurs significant overhead, particularly for update-intensive workloads, where it introduces a concurrency bottleneck (the log), and incurs log creation and flush I/O overhead. </p>
<p>In this project, we propose a new recovery model based on group commit, called concurrent prefix recovery (CPR). CPR differs from traditional group commit implementations in two ways: (1) we provide users a semantic description of committed operations, of the form "all operations until time $T_i$ on thread $i$"; and (2) we use asynchronous incremental checkpointing instead of a WAL to implement the group commit in a scalable bottleneck-free manner. CPR provides the same consistency as a point-in-time commit, but allows a concurrent and scalable implementation. We design and implement protocols and solutions to make two systems durable using CPR: (1) a custom in-memory transactional database; and (2) a state-of-the-art scalable larger-than-memory hash-based key-value store. A detailed evaluation of these modified systems shows that CPR is capable of supporting highly concurrent and scalable performance, reaching hundreds of millions of operations per second on a multi-core machine.</p>
<span><a href="mailto:guna@cs.washington.edu">[On Request]</a></span>
</li>
</ul>
<div><hr><hr><br><h2>Past Projects</h2></div>
<ul>
<br>
<li>
<p><h3>FASTER: A Concurrent Key-Value Store</h3><br>
Over the last decade, there has been a tremendous growth in data-intensive applications and services in the cloud. Data is created on a variety of edge sources, e.g., devices, browsers, and servers, and processed by cloud applications to gain insights or take decisions. Applications and services either work on collected data, or monitor and process data in real time. These applications are typically update intensive and involve a large amount of state beyond what can fit in main memory. However, they display significant temporal locality in their access pattern. This paper presents Faster, a new key-value store for point read, blind update, and read-modify-write operations. Faster combines a highly cache-optimized concurrent hash index with a hybrid log: a concurrent log-structured record store that spans main memory and storage, while supporting fast in-place updates of the hot set in memory. Experiments show that Faster achieves orders-of-magnitude better throughput – up to 160M operations per second on a single machine – than alternative systems deployed widely today, and exceeds the performance of pure in-memory data structures when the workload fits in memory. </p>
<span><a href="https://github.com/Microsoft/FASTER">[Github]</a></span> 
<span><a href="https://www.microsoft.com/en-us/research/uploads/prod/2018/03/faster-sigmod18.pdf">[SIGMOD 2018]</a></span> <span><a href="http://www.vldb.org/pvldb/vol11/p1930-chandramouli.pdf">[VLDB 2018 (Demo)]</a></span>
<span><a href="{{site.url}}assets/FASTER-sigmod18.pptx">[Slides]</a></span> </li>
<br><hr><br>
<li>
<p><h3>RILLE: Scalable Ordered Stream Processing</h3><br>
Many modern applications require real-time processing of large volumes of high-speed data. Such data processing needs can be modeled as a streaming computation. A streaming computation is specified as a dataflow graph that exposes multiple opportunities for parallelizing its execution, in the form of data, pipeline and task parallelism. On the other hand, many important applications require that processing of the stream be ordered, where inputs are processed in the same order as they arrive. There is a fundamental conflict between ordered processing and parallelizing the streaming computation. This paper focuses on the problem of effectively parallelizing ordered streaming computations on a shared-memory multicore machine.  </p>
<p>We first address the key challenges in exploiting data parallelism in the ordered setting. We present a low-latency, non-blocking concurrent data structure to order outputs produced by concurrent workers on an operator. We also propose a new approach to parallelizing partitioned stateful operators that can handle load imbalance across partitions effectively and mostly avoid delays due to ordering. We illustrate the trade-offs and effectiveness of our concurrent data-structures on micro-benchmarks and streaming queries from the TPCx-BB benchmark. We then present an adaptive runtime that dynamically maps the exposed parallelism in the computation to that of the machine. We propose several intuitive scheduling heuristics and compare them empirically on the TPCx-BB queries. We find that for streaming computations, heuristics that exploit as much pipeline parallelism as possible perform better than those that seek to exploit data parallelism. </p>
<span><a href="https://arxiv.org/abs/1803.11328">[arXiv]</a></span> 
</li>
<br><hr><br>
<li>
<p><h3>Automated Linguistic Personalization</h3><br>
Personalizing marketing messages for specific audience segments is vital for increasing user engagement with advertisements, but it becomes very resource-intensive when the marketer has to deal with multiple segments, products or campaigns. In this research, we take the first steps towards automating message personalization by algorithmically inserting adjectives and adverbs that have been found to evoke positive sentiment in specific audience segments, into basic versions of ad messages. First, we build language models representative of linguistic styles from user-generated textual content on social media for each segment. Next, we mine product-specific adjectives and adverbs from content associated with positive sentiment. Finally, we insert extracted words into the basic version using the language models to enrich the message for each target segment, after statistically checking in-context readability. Decreased cross-entropy values from the basic to the transformed messages show that we are able to approach the linguistic style of the target segments. Crowdsourced experiments verify that our personalized messages are almost indistinguishable from similar human compositions. Social network data processed for this research has been made publicly available for community use. </p>
<span><a href="https://link.springer.com/chapter/10.1007/978-3-319-18117-2_16">[CICLing 2015]</a></span>
<span><a href="http://people.mpi-inf.mpg.de/~rsaharo/cicling15slides_rsrapgpjpk.pdf">[Slides]</a></span>
</li>
<br><hr><br>
<li>
<p><h3>I/O Optimal Index Structures</h3><br>
Indexing techniques optimized for a higher write throughput such as LSM Trees generally compromise on read performance. We designed and implemented an indexing technique optimized for both read and write latencies. As part of the project we both experimentally and analytically verified the validity of some well known ideas in designing key value stores. </p>
<span><a href="{{site.url}}/assets/buffertree-report.pdf">[Thesis (old)]</a></span> </li>
<br><hr><br>
<li><h3>Synthesis Modulo Bisimulation</h3><br>
<p>We worked on the open problem of synthesizing distributed implementation from global specifications in the framework of transition systems, using bismulation as the equivalence criterion. We focussed on the loosely cooperating model of distributed transition systems. We identified several interesting properties about synthesizable specification out of which the major one was diamond closure property in the bisimulation quotient of a synthesizable system. We also showed that the bisimulation quotient need not necessarily be a product. </p> 
</li>
</ul>

