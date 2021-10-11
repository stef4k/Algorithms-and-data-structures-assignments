# Plant Grammar
This assignment covers a specific type of grammar called L-Systems by Aristid Lindenmayer. An L-system is a set of string production rules and an axiom, which gives the starting point of the strings we want to produce.

The grammar of such a system is as follows:  

<b>A → AB  
B → A </b>  

The axiom is the symbol <b>A</b>. Therefore, by repeatedly applying the rules of production, we get:

A⇒AB  
&nbsp;&nbsp;⇒ABA  
&nbsp;&nbsp;⇒ABAAB  
&nbsp;&nbsp;⇒ABAABABA    
&nbsp;&nbsp;⇒ABAABABAABAAB    
&nbsp;&nbsp;⇒ABAABABAABAABABAABABA    
&nbsp;&nbsp;⇒ABAABABAABAABABAABABAABAABABAABAAB
 
## Koch Curve
Axiom: <b>F</b>  
Rule: <b>F+F−F−F+F</b>

The `F` symbol means moving forward, the `+` symbol means turning left 90 degress, the `-` symbol means turning right 90 degrees. Applying the rule once obviously gives us the string:

<b>F + F − F − F + F</b>

which corresponds to the following figure:  
<p align="center">
<img src="https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/images/koch_curve1.png" width="300" height="300" />
</p>

If we apply the rule twice, we will get the string:

<b>F + F-F-F + F + F + F-F-F + F-F + F-F-F + F-F + F-F-F + F + F + F-F-F + F + F</b>

This gives us the following figure:  
<p align="center">
<img src="https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/images/koch_curve2.png" width="400" height="400"  />
</p>

If we apply the rule five times, we will get a much larger string, with 6,249 characters, which gives us the following shape:  

<p align="center">
<img src="https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/images/koch_curve5.png" width="600" height="500" />
</p>

## Installation requirements
Install the necessary library:  

    pip install matplotlib

## Running the script
In order to run the script, execute the following command from cmd:  

    python lsystem.py [-m] [-d] <input_file> [output_file]

The program will either edit grammar files or find the grammar that describes a shape. This behavior will be determined by the presence of the -d parameter

## Grammar Editing

Firstly, if the user does not give the -d parameter. Then the <input_file> parameter is the name of the file that contains the L-system grammar and the parameters that will be used. For example for the koch curve, the file is:

    {
      "axiom" : "F",
      "left_angle": 90.0,
      "right_angle": 90.0,
      "step_length": 5,
      "order": 5,
      "start_angle" : 0,    
      "rules" : {
        "F": "F+F-F-F+F"
      }
    }
    
The file contains the following fields:
* axiom: the axiom
* left_angle: the angle of the left turn
* right_angle: the angle of the right turn
* step_length: the length of the step
* order: the number of applications of the rules
* start_angle: the value of the starting angle
* rules: the rules of grammar

If the parameter -m is given, the program prints the result string as an output. If the user gives the [output_file] parameter, [output_file] is the name of a file to be created. This file will consist of lines. Each line of the file will contain two pairs of coordinates:

`(x1, y1) (x2, y2)`

## Examples
### Example 1
If the user uses the [koch_2.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/koch_2.json) file and runs the script the following way:

    python lsystem.py -m koch_2.json
   
the output of the program should be exactly as follows:

    F + F-F-F + F + F + F-F-F + F-F + F-F-F + F-F + F-F-F + F + F + F-F-F + F + F

### Example 2
If the user runs the script the following way, using the [koch_5.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/koch_5.json) file:

    python lsystem.py koch_5.json koch_5.txt
    
the output of the program should be the koch_5.txt file, which describes the Koch curve with five iterations.

In order to view the image, run:

    python mpl_draw.py koch_5.txt
To save it to a file, run:

    python mpl_draw.py koch_5.txt koch_5.png

To create the island of Koch, use the file [koch_island.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/koch_island.json) to get the result koch_island.txt:

    python lsystem.py koch_island.json koch_island.txt
And then to view it, use:

    python mpl_draw.py koch_island.txt

### Example 3
To create the dragon curve, use the [dragon.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/dragon.json) file:

    python lsystem.py dragon.json dragon.txt

And then to view it, use:

    python mpl_draw.py dragon.txt

### Example 4
For the two Sierpiński triangles use the files [sierpinski.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/sierpinski.json) and [sierpinski_triangle_arrowhead.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/sierpinski_triangle_arrowhead.json)

### Example 5
To create various plants use the following files [plant_1.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/plant_1.json), [plant_2.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/plant_2.json), [plant_3.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/plant_3.json), [plant_4.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/plant_4.json), [plant_5.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/plant_5.json), [plant_6.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/plant_6.json)

### Example 6
To create the Penrose mosaic use the [penrose.json](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/penrose.json) file.

### Example 7
If the user uses the [edge_rewriting_1.txt](https://github.com/stef4k/Algorithms-and-data-structures-assignments/blob/main/assignment-3/input%20files/edge_rewriting_1.txt) file and runs the script:

    python lsystem.py -d edge_rewriting_1.txt

The output should be:

    FF + G + G-F-F + G + GF-G-FFG + F-G-FF-G + FG + G + F-F-GG +
    -FF + G + G-F-FG-F + GG + F + G-FGG + F + GF-F-G + G + F-F-GG


##
[Complete Greek assignment description](https://github.com/dmst-algorithms-course/assignment-2019-3/blob/master/assignment_2019_3.ipynb)
