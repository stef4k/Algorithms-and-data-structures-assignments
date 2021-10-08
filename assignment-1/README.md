# Degeneracy - Graph Theory

This assignment required to detect the [k-cores](https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)) of a graph. Implement the following algorithm to find the core number of each node of any given graph:


<img src="https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-1/images/kcores%20algorithm.png" width="500" height="600" />

## Running the script
Use the command line to run the script:  

`python k_cores.py <input_file>`  

where `input_file` is the name of the file that contains the graph we wish to analyze. The graph files have the following form:

0 1  
0 2  
1 3  
2 3  
2 6  
2 7  
3 6  
3 7  
3 8  
4 5  
5 6  
5 10  
6 7  
7 8  
7 11  
8 9  

In other words, each line of the file describes one edge between two nodes. In fact, all graphs are undirected.

## Example
The script is runned for the text file [example_graph.txt](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-1/graphs/example_graph.txt):  

`python k_cores.py example_graph.txt`  

The exit of the script should be the following:  

0 2  
1 2  
2 3  
3 3  
4 1  
5 1  
6 3  
7 3  
8 2  
9 1  
10 1  
11 1  

Also, run the script for the graph [human brain functional activations](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-1/graphs/human_brain_functional_activations.txt) and verify the [solutions](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-1/solutions/human_brain_solutions.txt).

## 
[Complete Greek version of the assignment description](https://github.com/dmst-algorithms-course/assignment-2019-1/blob/master/assignment_2019_1.ipynb)

