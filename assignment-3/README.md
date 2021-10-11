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

### Example 2

### Example 3

### Example 4

### Example 5

### Example 6

### Example 7


##
[Complete Greek assignment description](https://github.com/dmst-algorithms-course/assignment-2019-3/blob/master/assignment_2019_3.ipynb)
