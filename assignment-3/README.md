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

If we apply the rule twice, we will get the string:

<b>F + F-F-F + F + F + F-F-F + F-F + F-F-F + F-F + F-F-F + F + F + F-F-F + F + F</b>

This gives us the following figure:

If we apply the rule five times, we will get a much larger string, with 6,249 characters, which gives us the following shape:

##
[Complete Greek assignment description](https://github.com/dmst-algorithms-course/assignment-2019-3/blob/master/assignment_2019_3.ipynb)
