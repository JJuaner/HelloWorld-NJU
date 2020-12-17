google-mapreduce c++底层  
hadoop-mapreduce java实现、复现google论文、开源


pagerank  
随机游走改进


谷歌搜索引擎：pagerank but海量网页->海量数据存储和处理需求   
存储问题->计算问题  
谷歌搜索引擎的实现：
存储：(分布式存储)分布式文件系统DFS->一个实现->hadoop dfs(开源)  16wcode 99% 磁盘损坏、服务器宕机->复制容错
计算：(复杂计算并行化) 大数据并行处理框架->一个实现->hadoop mapreduce 27wcode 99%
装了hadoop和mapreduce，把大规模数据的处理的可靠性都交给它们，用它们跑代码：它们的实现保证提供程序的正确结果，返回错误的结果是逻辑的错误，报错不返回结果是系统的错误，
mpi和mapreduce：mapreduce约束中间结果（键值对），从而可以多个阶段的加速

谷歌的三驾马车：
hadoop生态：DFS，MR，Yarn（资源调度）一般认为前两者封装好了，主要工作集中于Yarn


mapreduce课：怎么并行化
mapreduce是种编程范式，都分为两阶段，中间阶段都约束
