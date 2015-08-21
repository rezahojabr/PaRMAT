PaRMAT
======

PaRMAT is a multi-threaded RMAT graph generator. Using PaRMAT, you can create very large directed or undirected RMAT graphs. PaRMAT is designed to exploit multiple threads and to avoid failing when there is not a lot of memory (RAM) available.


A little bit of background
-------------------

Those who work on graph processing solutions clearly know that [RMAT graphs](http://epubs.siam.org/doi/pdf/10.1137/1.9781611972740.43) usually imitate the structure of graphs that are extracted from real-world origins hence are of great importance. AFAIK, there are only two publicly avaiable RMAT graph generators out there: [GTgraph](http://www.cse.psu.edu/~madduri/software/GTgraph/) and [SNAP](http://snap.stanford.edu/snap/download.html). GTGraph, which is especifically built for RMAT graph generation purpose, fails during creation of very very large graphs (half a biilion edges on a machine with 4 GB of RAM was the furthest it could go). In addition, it only creates directed graphs and cannot avoid existence of duplicate edges in the graph. How about SNAP? SNAP is on the other hand a really big graph analysis and mining library. To generate RMAT graphs in SNAP, you've got to open up the source code (*snap/examples/graphgen/*) and add the capability of RMAT graph generation (well, that's the way I know, there may be a nicer way). It only creates undirected graphs and again fails to create very large RMAT graphs (with explicitly specified number of edges and vertices).


PaRMAT
---------------
PaRMAT is a piece of software designed to create large RMAT graphs, even on a machine with limited amount of available memory. PaRMAT divides the adjacency matrix into squares and the workload between multiple threads. PaRMAT provides a number of options for the RMAT graph: being directed or non-directed, disallowing duplicate edges, sorting the output, varying RMAT graph parameters, etc. Directecd and non-directed graphs generated by PaRMAT show the same degree distribution as GTGraph's and SNAP's. PaRMAT does not fail when the specified graph is very large and creates the graphs faster than GTGraph and SNAP.


PaRMAT Requirement
---------------------
To compile PaRMAT, you'll need to have a C++ compiler that supports C++11 features. 


Making PaRMAT
------------------
I personally could create PaRMAT on Ubuntu 12.04 and Ubuntu 14.04 (g++ versions 4.8.1 and 4.8.2 respectively). Run `make` in the `Release` folder, and everything will be taken care of. I don't think it would be hard to make and run PaRMAT in a machine with a different operating system.


Running PaRMAT
------------------
PaRMAT needs two required command-line arguments: `-nVertices` and `-nEdges` which provide the number of vertices and number of edges in the specified graph respectively. For example, running:
    
    ./PaRMAT -nVertices 100000 -nEdges 1000000
    
creates a graph with a million edges and a hundred thousand vertices. Other accepted command-line arguments can be found by executing the program with no argument. I repeat them in below:

	Usage: 	Required command line arguments:
		-Number of edges. E.g., -nEdges 1021
		-NUmber of vertices. E.g., -nVertices 51
	Additional arguments:
		-Output file (default: out.txt). E.g., -output myout.txt
		-RMAT a parameter (default: 0.45). E.g., -a 0.42
		-RMAT b parameter (default: 0.22). E.g., -b 0.42
		-RMAT c parameter (default: 0.22). E.g., -c 0.42
		-Number of worker CPU threads (default: queried/1). E.g., -threads 4
		-Output should be sorted based on source index (default: not sorted). To sort: -sorted
		-Allow edge to self (default:yes). To disable: -noEdgeToSelf
		-Allow duplicate edges (default:yes). To disable: -noDuplicateEdges
		-Will the graph be directed (default:yes). To make it undirected: -undirected
		-Usage of available system memory (default: 0.5 which means up to half of available RAM may be requested). E.g., -memUsage 0.9

In addition to above arguments, there are a number of parameters internal to the program itself. They are accessible in `internal_config.hpp`. After applying modifications to this file, you obviously need to re-compile the program to see the effects.


Citing
------------------
```shell
@MISC{PaRMAT,
  author = "Farzad Khorasani, Keval Vora and Rajiv Gupta",
  title = "PaRMAT: A Parallel Generator for Large R-MAT Graphs",
  year = "2015",
  url = "https://github.com/farkhor/PaRMAT"
}
```

