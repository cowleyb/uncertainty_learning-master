This replication package is for the paper "Online Learning and Uncertainty in Compositional Self-Adaptation: An Inter-Scenario Study", submitted to ACSOS 2021.

Our experiments were executed on a fully up to date Ubuntu 18.04 server edition, running on a micro-server with an Intel i5-64000T 2.2GHz quad-core processor and 4GB of RAM. Similar result trends should be observed on any other platform.

This package assumes the use of Dana v245, though it may also work on future releases. You'll need to download and install Dana using the instructions at <http://www.projectdana.com>.

The replication package contains both the experiments and the code to create all of the graphs which appear in the paper (using Dana's chart library).

---

## Running the experiments

First, open a command-prompt in the 'experiments' folder of this replication package. Type the command:

dnc .

This compiles the entire directory.

### Section IV.A

List study divergence graph (Fig. 1):

Type:

dana ListDivergenceTest.o -s 1000

This will run the experiment. When the experiment is finished, it will have written a text file to the output_data directory.

List study adapt speed graph (Fig. 2):

Run the command:

dana AdaptSpeedTest.o

When the experiment is finished, it will have written a text file to the output_data directory.

Learning convergence graphs and total learning effect graphs (Fig. 3, Fig. 4, Fig. 5, Fig. 6):

In the same directory, type the set commands:

dana ListLearningTest.o workloads/list-10-90.txt -c 12000 -t 167
dana ListLearningTest.o workloads/list-90-10.txt -c 12000 -t 167
dana ListLearningTest.o workloads/list-10-90--90-10-c10.txt -c 12000 -t 167
dana ListLearningTest.o workloads/list-10-90--90-10-c10sq.txt -c 12000 -t 167
dana ListLearningTest.o workloads/list-10-90--90-10-c10xq.txt -c 12000 -t 167

dana ListLearningConvergedTest.o workloads/list-10-90.txt -c 12000 -t 167
dana ListLearningConvergedTest.o workloads/list-90-10.txt -c 12000 -t 167
dana ListLearningConvergedTest.o workloads/list-10-90--90-10-c10.txt -c 12000 -t 167
dana ListLearningConvergedTest.o workloads/list-10-90--90-10-c10sq.txt -c 12000 -t 167
dana ListLearningConvergedTest.o workloads/list-10-90--90-10-c10xq.txt -c 12000 -t 167

dana ListCompletionTest.o workloads/list-10-90.txt -d data/adt/Linked.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-90-10.txt -d data/adt/Linked.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-10-90--90-10-c10.txt -d data/adt/Linked.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-10-90--90-10-c10sq.txt -d data/adt/Linked.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-10-90--90-10-c10xq.txt -d data/adt/Linked.o -c 12000 -t 167

dana ListCompletionTest.o workloads/list-10-90.txt -d data/adt/Array.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-90-10.txt -d data/adt/Array.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-10-90--90-10-c10.txt -d data/adt/Array.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-10-90--90-10-c10sq.txt -d data/adt/Array.o -c 12000 -t 167
dana ListCompletionTest.o workloads/list-10-90--90-10-c10xq.txt -d data/adt/Array.o -c 12000 -t 167

dana ListLearningTest.o workloads/list-10-90.txt -c 12000 -t 167 -s 100
dana ListLearningTest.o workloads/list-90-10.txt -c 12000 -t 167 -s 100
dana ListLearningTest.o workloads/list-10-90--90-10-c10.txt -c 12000 -t 167 -s 100
dana ListLearningTest.o workloads/list-10-90--90-10-c10sq.txt -c 12000 -t 167 -s 100
dana ListLearningTest.o workloads/list-10-90--90-10-c10xq.txt -c 12000 -t 167 -s 100

dana ListLearningConvergedTest.o workloads/list-10-90.txt -c 12000 -t 167 -s 100
dana ListLearningConvergedTest.o workloads/list-90-10.txt -c 12000 -t 167 -s 100
dana ListLearningConvergedTest.o workloads/list-10-90--90-10-c10.txt -c 12000 -t 167 -s 100
dana ListLearningConvergedTest.o workloads/list-10-90--90-10-c10sq.txt -c 12000 -t 167 -s 100
dana ListLearningConvergedTest.o workloads/list-10-90--90-10-c10xq.txt -c 12000 -t 167 -s 100

dana ListCompletionTest.o workloads/list-10-90.txt -d data/adt/Linked.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-90-10.txt -d data/adt/Linked.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-10-90--90-10-c10.txt -d data/adt/Linked.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-10-90--90-10-c10sq.txt -d data/adt/Linked.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-10-90--90-10-c10xq.txt -d data/adt/Linked.o -c 12000 -t 167 -s 100

dana ListCompletionTest.o workloads/list-10-90.txt -d data/adt/Array.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-90-10.txt -d data/adt/Array.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-10-90--90-10-c10.txt -d data/adt/Array.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-10-90--90-10-c10sq.txt -d data/adt/Array.o -c 12000 -t 167 -s 100
dana ListCompletionTest.o workloads/list-10-90--90-10-c10xq.txt -d data/adt/Array.o -c 12000 -t 167 -s 100

This runs the experiment set once for each workload, and for each of the list stored item counts. When the experiments finish, they will have written text files to the output_data directory.


### Section IV.B

Cache study divergence graph (Fig. 7):

In the same directory as above, run the command:

dana CacheDivergenceTest.o

This will run the experiment; when finished, it will have written a text file to the output_data directory.

Learning convergence graphs and total learning effect graphs (Fig. 3, Fig. 4, Fig. 5, Fig. 6):

In the same directory, use the sequence of commands (one per experiment):

dana CacheLearningTest.o workloads/cache-10-500000-400000.txt -c 12000 -t 167
dana CacheLearningTest.o workloads/cache-200-500000-400000.txt -c 12000 -t 167
dana CacheLearningTest.o workloads/cache-10--200-500000-400000.txt -c 12000 -t 167
dana CacheLearningTest.o workloads/cache-10--200-500000-400000-csk.txt -c 12000 -t 167
dana CacheLearningTest.o workloads/cache-10--200-500000-400000-xcsk.txt -c 12000 -t 167

dana CacheLearningConvergedTest.o workloads/cache-10-500000-400000.txt -c 12000 -t 167
dana CacheLearningConvergedTest.o workloads/cache-200-500000-400000.txt -c 12000 -t 167
dana CacheLearningConvergedTest.o workloads/cache-10--200-500000-400000.txt -c 12000 -t 167
dana CacheLearningConvergedTest.o workloads/cache-10--200-500000-400000-csk.txt -c 12000 -t 167
dana CacheLearningConvergedTest.o workloads/cache-10--200-500000-400000-xcsk.txt -c 12000 -t 167

dana CacheCompletionTest.o workloads/cache-10-500000-400000.txt -d files/FileLoader.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-200-500000-400000.txt -d files/FileLoader.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-10--200-500000-400000.txt -d files/FileLoader.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-10--200-500000-400000-csk.txt -d files/FileLoader.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-10--200-500000-400000-xcsk.txt -d files/FileLoader.o -c 12000 -t 167

dana CacheCompletionTest.o workloads/cache-10-500000-400000.txt -d files/FileLoaderCache.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-200-500000-400000.txt -d files/FileLoaderCache.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-10--200-500000-400000.txt -d files/FileLoaderCache.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-10--200-500000-400000-csk.txt -d files/FileLoaderCache.o -c 12000 -t 167
dana CacheCompletionTest.o workloads/cache-10--200-500000-400000-xcsk.txt -d files/FileLoaderCache.o -c 12000 -t 167

This runs the experiment set once for each workload. When the experiments finish, they will have written text files to the output_data directory.

---

## Making the graphs

Copy each the output_data directory to the 'graphs' folder of this replication package.

Open a command-prompt in the 'adaptation' folder of this replication package. Type the command:

dnc .

Then:

dana Graphs.o

This will render each of the graphs shown in the paper.