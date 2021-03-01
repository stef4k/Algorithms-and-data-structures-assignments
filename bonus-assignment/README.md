# Assignment-2019-bonus
### Description
This project given n points in the
two-dimensional space and a positive integer k (k<=n),
constructs a tree spanning at least k of
these points such that the total length of the tree is at most O(k ^(1/4)) 
times that of a minimum-length tree spanning any k of the points.
In the best case the minimum tree constructed consists of 
exactly k points. If that is not possible the tree will
consist of k+m points where m>0 and k+m<n and m the least integer so that the square root 
of (k+m) has no decimal places (root (k+m) is an integer).
Lastly, in the worst case scenario if there is no such number
as m, the minimum spanning tree will consist of exactly n points.
The output of the project describes the number of points that the 
MST (minimum-spanning tree) consists of, the length of the MST 
( the sum of distances of all the connections used in the MST) 
and finally the connections of the  points that are used to construct
the MST.

### Importance
The finding of MST can be quite important in various cases. Firstly,
in the case of a telecommunications company trying to lay cable in a new
neighborhood. If it is constrained to bury the cable only along certain paths 
(e.g. roads), then there would be a graph containing the points (e.g. houses) 
connected by those paths. Some of the paths might be more expensive, because 
they are longer, or require the cable to be buried deeper. These paths would 
be represented by edges with larger weights ([MST-wiki](https://en.wikipedia.org/wiki/Minimum_spanning_tree)). 
Furthermore, another case is for instance when the oil reconnaissance boats are back from
their final trip off the coast of Norway and present the coordinators with a detailed map of the
seas surrounding the coastline. Marked in this map are locations that are believed to
have a good chance of containing oil under the sea bed. The company has a limited
number of oil rigs that it is willing to invest in the effort. The problem is to position
these oil rigs at marked places so that the cost of laying down pipelines between these
rigs is minimized. The problem at hand can be modeled as follows: given a graph with
nonnegative edge weights and a specified number k, find a tree of minimum weight
spanning at least k nodes. The solution to the problem will be a tree spanning
exactly k nodes. This problem is called the k-minimum spanning tree (kMST).

### Algorithm
Before calculations start, k is checked if it has a square root without any decimal places. If not, k is continuously
increased till it becomes an integer whose square root has no decimal places or till it becomes equal to n . In those cases, k will be changed. 

If k is equal to n, there will be only one MST (the one that contains all the n points). As a result, the MST of the n points 
is constructed by using the Prim's algorithm for finding minimum spanning trees. Via the MST, the length of the tree is calculated 
and the appropriate output is made.

In any other case ( it will be:  k < n ), the right k points must be estimated in order to find the MST for those k points. Let's 
call S={s1,s2,...,sn} the given set of points and d(i,j) the Euclidean distance between si and sj. In order to find
the right k points and followingly the MST, the following steps must be pursued, for each distinct pair of points si, sj in S:
1. Construct the circle C with diameter D = root(3) * d(i, j) centered at the
midpoint of the line segment (si, sj)
2. Let Sc be the subset of S contained in C. If Sc contains fewer than
k points, skip to the next iteration of the loop (i.e., try the next pair of
points). Otherwise, do the following.
3. Let Q be the square of side D circumscribing C.
4. Divide Q into k square cells each with side = D / root(k)
5. Sort the cells by the number of points from Sc they contain and
choose the minimum number of cells so that the chosen cells together
contain at least k points. In case there are more than k points in the chosen cells, randomly discard points from
the last chosen cell so that the total number of points in all the cells is
equal to k.
6. Construct a minimum spanning tree for the k chosen points. 
7. The solution value for the pair (si, sj) is the length of this MST.

From all the distinct pairs select the pair with the minimum length of its MST. That MST is the soltuion and together with the length and the connections,
the appropriate output is made.


### Installation
Clone the whole project to your computer via git
```
git clone https://github.com/stef4k/Algorithms-and-data-structures-assignments2019.git
```
Select the right project
```
cd bonus-assignment/
```

### Usage
The project must be called from the cmd like:
```
python kmst.py <input_file> <k_number>
```
* <input_file> is the text file of points whom the MST will be constructed. The input file must have the following format (n lines for n points 
followed by a blank line):
```
point1 (abscissa1, ordinate1)
point2 (abscissa2, ordinate2)
point3 (abscissa3, ordinate3)
point4 (abscissa4, ordinate4)
pointn (abscissan, ordinaten)

```

* <k_number> is the minimum integer number of points that the tree will span, so the following must be valid: k_number > 1 and k_number <=n

##### Example 1
* Running the file points1.txt for k=4
```
python kmst.py points1.txt 4
```
Output is:
```
For  4  points the MST has length:  4.650281539872885
The links that were used are:
{('s2', 's5'): 2.23606797749979,
 ('s5', 's7'): 1.0,
 ('s7', 's6'): 1.4142135623730951}
```
In conlusion, it is noticed that the k we inputed has a square root without decimal places (root(4)=2), as a result the MST contains exactly 4 points.

* Running the file points1.txt for k=5
```
python kmst.py points1.txt 5
```
Output is:
```
For  9  points the MST has length:  28.053497054771064
The links that were used are:
{('s1', 's9'): 7.0,
 ('s10', 's1'): 4.0,
 ('s10', 's4'): 1.0,
 ('s2', 's3'): 7.280109889280518,
 ('s2', 's5'): 2.23606797749979,
 ('s5', 's7'): 1.0,
 ('s6', 's10'): 4.123105625617661,
 ('s7', 's6'): 1.4142135623730951}
```
In conclusion, it is noticable that the MST that is constructed contains 9 points because square root of 5 equals to 2.23606 which contains decimal places. 
As a result, k is transformed into 9 whose root equals to 3.

##### Example 2 
* Running the file points2.txt for k=7
```
python kmst.py points2.txt 7
```
Output is:
```
For  9  points the MST has length:  32.2504345133836
The links that were used are:
{('s1', 's5'): 3.1622776601683795,
 ('s12', 's16'): 5.0,
 ('s16', 's13'): 5.0,
 ('s16', 's7'): 4.242640687119285,
 ('s5', 's8'): 4.47213595499958,
 ('s7', 's6'): 3.605551275463989,
 ('s8', 's12'): 3.1622776601683795,
 ('s8', 's9'): 3.605551275463989}
```
To sum up, k is changed from 7 to 9 and the MST for 9 points is calculated.

* Running the file points2.txt for k=16
```
python kmst.py points2.txt 16
```
Output is:
```
For  16  points the MST has length:  63.52304920697716
The links that were used are:
{('s1', 's4'): 6.082762530298219,
 ('s1', 's5'): 3.1622776601683795,
 ('s12', 's16'): 5.0,
 ('s13', 's19'): 4.242640687119285,
 ('s16', 's13'): 5.0,
 ('s16', 's7'): 4.242640687119285,
 ('s17', 's2'): 3.0,
 ('s20', 's10'): 3.605551275463989,
 ('s4', 's17'): 4.242640687119285,
 ('s5', 's8'): 4.47213595499958,
 ('s7', 's6'): 3.605551275463989,
 ('s8', 's12'): 3.1622776601683795,
 ('s8', 's9'): 3.605551275463989,
 ('s9', 's14'): 5.0,
 ('s9', 's20'): 5.0990195135927845}
```
Last but not least, k is not changed because square root of 16 equals to 4. As a result, the smallest MST for 16 of all the 20 points is constructed and 
its length is found.

##### Example 3 
Running the file points3.txt for k=16
```
python kmst.py points3.txt 16
```
Output can be:
```
For  16  points the MST has length:  55.3852467174233
The links that were used are:
{('s1', 's31'): 2.8284271247461903,
 ('s10', 's11'): 5.0,
 ('s11', 's34'): 2.23606797749979,
 ('s12', 's16'): 5.0,
 ('s16', 's7'): 4.242640687119285,
 ('s20', 's10'): 3.605551275463989,
 ('s31', 's4'): 4.123105625617661,
 ('s32', 's14'): 1.0,
 ('s5', 's1'): 3.1622776601683795,
 ('s7', 's6'): 3.605551275463989,
 ('s8', 's12'): 3.1622776601683795,
 ('s8', 's5'): 4.47213595499958,
 ('s9', 's20'): 5.0990195135927845,
 ('s9', 's32'): 4.242640687119285,
 ('s9', 's8'): 3.605551275463989}
```
Output can also be:
```
For  16  points the MST has length:  54.022336129078596
The links that were used are:
{('s1', 's31'): 2.8284271247461903,
 ('s10', 's11'): 5.0,
 ('s11', 's34'): 2.23606797749979,
 ('s17', 's2'): 3.0,
 ('s20', 's10'): 3.605551275463989,
 ('s31', 's3'): 4.242640687119285,
 ('s31', 's4'): 4.123105625617661,
 ('s32', 's14'): 1.0,
 ('s4', 's17'): 4.242640687119285,
 ('s5', 's1'): 3.1622776601683795,
 ('s8', 's12'): 3.1622776601683795,
 ('s8', 's5'): 4.47213595499958,
 ('s8', 's9'): 3.605551275463989,
 ('s9', 's20'): 5.0990195135927845,
 ('s9', 's32'): 4.242640687119285}
```
Lastly, output could also be:
```
For  16  points the MST has length:  55.43654969145169
The links that were used are:
{('s1', 's31'): 2.8284271247461903,
 ('s10', 's11'): 5.0,
 ('s11', 's34'): 2.23606797749979,
 ('s14', 's32'): 1.0,
 ('s17', 's2'): 3.0,
 ('s20', 's10'): 3.605551275463989,
 ('s31', 's4'): 4.123105625617661,
 ('s32', 's9'): 4.242640687119285,
 ('s34', 's21'): 5.656854249492381,
 ('s4', 's17'): 4.242640687119285,
 ('s5', 's1'): 3.1622776601683795,
 ('s8', 's12'): 3.1622776601683795,
 ('s8', 's5'): 4.47213595499958,
 ('s9', 's20'): 5.0990195135927845,
 ('s9', 's8'): 3.605551275463989}
```

In conclusion, sometimes there are different outputs because in step 5 of the algorithm, points are randomly discarded from the last chosen cell until 
the sum of the chosen points is equal to k. As a result, different MST are constructed for some pairs, leading to a different solution.

### Built with
* [Spyder](https://www.spyder-ide.org/)
* [Anaconda](https://www.anaconda.com/)

### Credits
* [Stefanos Kypritidis](https://github.com/stef4k) - Author
* [Robert C. Prim](https://en.wikipedia.org/wiki/Robert_C._Prim ) (For Prim's algorithm for finding minimum spanning trees)

### License
#### MIT License

Copyright (c) 2019 STEFANOS KYPRITIDIS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

