# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:38:20 2019

@author: Stefanos
"""
import json #for opening jason file
import math #for mathematic equation and pi
import argparse #for positional and optimal arguments
from collections import deque #for the implemantation of stacks and queues

#only used when -d is typed in cmd
#function that takes as input a list with the starting and ending point 
#those two points create a line
#and returns the coordinates of the squares that have that  line as a side of the square
#first coordinates correspond to right side and second ones to left
def find_points(list_el,step_length):
    x1 = list_el[0] / step_length
    y1 = list_el[1] / step_length
    x2 = list_el[2] / step_length
    y2 = list_el[3] / step_length
    #for every line there are 4 different cases in order to 
    #calculate which squares it is attached to
    #devide every coordinate by step_length in order to the coordinates  
    #correspond to the boxes of 2 dimensional space
    if y1==y2:
        horizontal = True #case that the line is horizontal
        if x2>x1:
            frontwards = True #subcase that the line goes frontwards
        else:
            frontwards = False#subcase that the line goes backwards
    else:
        horizontal = False #case that the line is vertical
        if y2>y1:
            upside = True #subcase that the line goes upwards 
        else:
            upside = False #subcase that the line goes downwards
    if horizontal: 
        if not frontwards:#if horizontal and backwards
            x1,x2=x2,x1 #swaps x values
            return (int(x2-1), int(y2), int(x1), int(y1-1)) 
            #different return so that 
            #first coordinates correspond to right side and second ones to left side
        return(int(x1), int(y1-1), int(x2-1), int(y2))
    else:
        if not upside: #if vertical and downwards
            y1, y2 = y2, y1 #swaps y values
            return (int(x1-1), int(y1), int(x2), int(y2-1)) 
            #different return so that first
            #coordinates correspond to right side and second ones to left side
        return(int(x2), int(y2-1), int(x1-1), int(y1))

#function that takes as argument the filename and returns a list
#with 4 floats in every line(that is also a list)
#first float is the x that we start, second is the y that we start
#third is the x that we end , and forth is the y that we end 
def open_textfile_rewrite(filename):
    with open(filename) as textfile: 
        points = []#create list
        for line in textfile:#for every line of file
            g = line.split(' ') #split line at space
            x_start = float(g[0][1:-1]) #x_start is the x of first tuple
            #'(' and ',' is cut
            y_start = float(g[1][:-1]) #y_start is the y of first tuple
            #')' is cut from g[1]
            x_end = float(g[2][1:-1]) #x_end is the x of second tuple
            #'(' and ',' is cut
            if '\n' in g[3]: #if \n is contained in last split
                y_end = float(g[3][:-2]) #y_end is the y of second tuple 
                #cuts the \n and ')'
            else:
                y_end = float(g[3][:-1]) #y_end is the y of second tuple
                #cuts ')'
            points.append([x_start, y_start, x_end, y_end])
        return(points)

#only when -d is typed in cmd
#function that finds the turns in every step
#'+' means left, '-' means right and '*' means straight (no turn)
#@point is a list that contains lists of the coordinates of points 
#@rightwards is a boolean to know if we run from left to right (True)
#or from right to left (False)
def find_turns(point,step_len,rightwards,side_sq):
    if rightwards:
        x_angle = -step_len#starting angle
        y_angle = 0 #in order to get the rigth turn from the atan function 
        #we have point [-step_len,0] as starting point
        point.append([point[-1][2], point[-1][3], point[-1][2] + step_len, point[-1][3]])
    #adds one last point so that we have to turn to horizontal level
    #with x_start the last x_end, y_start the last y_end of the list
    #x_end =the last x_end+step_length
    #y_end= the last y_end
    else:
        x_angle = step_len*(side_sq+1)#starting angle
        y_angle = 0
        #we have point [step_len*(side_sq+1),0] as starting point 
        #to get the right turn from left to right
        point.append([-step_len,0,0,0])
        #adds one last point so that we have to finish to horizontal level
        #which is [-step_len,0]
    turns = []#list that contains all turns : '+' is left, '-'is right 
    #'*' is no turn
    for x_prev,y_prev,x_nex,y_nex in point: #for every point
        if not rightwards: #if we go from left to right
            x_prev, x_nex = x_nex, x_prev # swap values 
            y_prev, y_nex = y_nex, y_prev #swap values
        x_angle = x_angle - x_prev #reduces x_angle by x_prev
        y_angle = y_angle - y_prev#reduces y_angle by y_prev
        x_nex = x_nex - x_prev #reduces x_nex by x_prev
        y_nex = y_nex - y_prev #reduces y_nex by y_prev
        #those calculations are done so we can use the atan2 function
        #that calculates the angle of vectors:
        #[(0,0),(x_angle,y_angle)] και [(0,0),(x_nex,y_nex)]
        angle = math.atan2(x_angle*y_nex - y_angle*x_nex, x_angle*x_nex + y_angle*y_nex)
        if angle == -math.pi / 2: #-90 degrees angle
            turns.append('+')
        elif angle == math.pi / 2:# 90 degrees angle
            turns.append('-')
        else: #0 degrees angle 
            #(we know that we either turn left or right for 90 degrees)
            turns.append('*')
        x_angle = x_prev #assigns x_angle with the x_prev so that we can calculate the arctan
        y_angle = y_prev #assigns @y_angle with @y_prev 
        #so that we can calculate the arctan with the 
        #module that requires vectors [(0,0),(x_angle,y_angle)] and [(0,0),(x_nex,y_nex)]
    point.pop()#pops the last point we appended 
    return (turns)

#function that returns the max value of a list that contains other lists
def find_max_list(lis):
    return (max([max(every_lis) for every_lis in lis]))
    #creates a list with the max for every sublist and returns the max that created list

#-d is typed im cmd
#function that  fills up all squares 
#by creating a list of strings for every part of line
#which can either be 'L' or 'R'
#a list @visited is created so that we know which squares are already visited
#goal is to visit every square exactly once  
def find_LRstring_rewrite(points,step_len,side_square):
    visited = [[False for j in range(side_square)] for i in range(side_square)] 
    #list to know which square is already visited 
    #(we have @side_squarex@side_square square)
    dq = deque() #creates empty deque structure
    index = 0 #sets @index 0
    #fills dq with points and index for every set of points 
    #so that we keep the identity of every point
    for elements in points:
        elements.append(index)
        dq.append(elements)# fills @dq with elements
        index = index+1 #adds 1 to @index
    results = [None for i in range (index)]
    #creates a list @results with length the index from before
    while dq: #while @dq is not empty
        elements=dq.popleft() #popleft from @dq
        x_point1,y_point1,x_point2,y_point2 = find_points(elements, step_len) 
        #calls funtion find_points to calculate which square is connected to the points
        #as a side of the particular square
        #first two points are the coordinates of the right square 
        #second two points are the coordinates of the left square
        if x_point1 < 0 or y_point1 < 0 or x_point1 >= side_square or y_point1 >= side_square: 
            #if one of the first coordinates is less that 0
            #or more than @side_square it means that the line belongs to the second square
            visited[x_point2][y_point2] = True #assigns visited of the second square with True
            results[elements[4]] = 'L' 
            #assigns @results of the particular set of points (with @index) with 'l'
        elif x_point2 < 0 or y_point2 < 0 or x_point2 >= side_square or y_point2 >= side_square: 
            #if one of the second coordinates is less that 0
            #or more than @side_square it means that the line belongs to the first square
            visited[x_point1][y_point1] = True 
            #assigns visited of the first square with True
            results[elements[4]] = 'R' 
            #assigns @results of the particular set of points (with @index) with 'R'
        elif visited[x_point1][y_point1]: #if the first square is already visited
            visited[x_point2][y_point2] = True 
            # turns visited of the second point True
            results[elements[4]] = 'L' 
            #assigns @results of the particular set of points (with @index) with 'L'
            #if one of the squares is already visited then there is only one option left
        elif visited[x_point2][y_point2]: #if the second square is already visited
            visited[x_point1][y_point1] = True  
            # turns visited of the first point True
            results[elements[4]] = 'R' 
            #assigns @results of the particular set of point (with @index) with 'R'
        else:
            dq.append(elements) #if none of the above exists, we append elements into the deque
            #so that hopefully next time we encounter it, one of the points is already visited 
            #and we can assign @results of the particular set of points
    return(results)

#function when -d is typed in cmd
#it unified the list of the results and turns 
#in order to get one list with the final output
#@rightwards in order to know how to correspond L and R to F/G
#@rightwards=True means from right to left
#@rightwards=False means from left to right
def calculate_finalresults_rewrite(results, turn, rightwards):
    finish_res=[]#creates empty list
    for i in range (len(results)): #runs simultaneously the @turn 
        #and @result list to append their elements to 
        if turn[i] != '*': #if turn[i] is '+' or '-'
            finish_res.append(turn[i])#append the specific to @finish_res
        if (results[i] == 'L'and rightwards) or (results[i] == 'R' and (not rightwards)):
            #if the result with index i is 'L' and rightwards
            # or is R and not rightwards append it to the @finish_res
            finish_res.append('F')
        else: #otherwise append 'G' to finish_res
            finish_res.append('G')
    if turn[-1] != '*': #in order to check the last spot of @turn 
        #as it is longer than @results for 1 index
        #if the last element of turn is '+' or '-'
        finish_res.append(turn[-1]) #append it to the @finish_res
    return(finish_res)

#function that is caled if -d is typed in cmd
#it open the file and prints the pattern string from the edge rewriting
#it actually calculates the rules with axiom: 'F'       
def edge_rewrite(filename):
    points= open_textfile_rewrite(filename) #calls function to transform the file into a list that
    #contains every line as a list of 4 floats
    step_length = points[0][3] - points[0][1] + points[0][2] - points[0][1] 
    #calculates step length from difference of point[0] and point[1]
    side_square = int(find_max_list(points) / step_length)
    #calls function find_max_list() and devides by step_len
    #in order to get the dimensions of the edge rewrite square
    turns = find_turns(points, step_length, True, side_square)#calls function to find the turns
    res = find_LRstring_rewrite(points, step_length, side_square)
    finish_result = calculate_finalresults_rewrite(res, turns, True)
    points = [ev_point[:4] for ev_point in points] 
    #cuts the index that we appended as 5th elements for every sublist in @points
    turns2 = find_turns(points[::-1], step_length, False, side_square) 
    #calls function with @points reversed as we start from the end 
    #when we go from left to right
    res2 = find_LRstring_rewrite(points[::-1], step_length, side_square)
    #calls function with list @points reversed
    finish_result2 = calculate_finalresults_rewrite(res2, turns2, False)
    print(''.join(finish_result))#prints the @finish_result without any spaces or commas
    print(''.join(finish_result2)) #prints the @finish_result2 without any spaces or commas
    

#function that find the pattern string from the @info given (json file)
#returns the @axi of the particular @info
def axi_finder(info):
    axi = info["axiom"] #assigns @axi with the axiom of the L system
    for i in range (info["order"]): #for as many times as order says
        len_bef = len(axi) #assigns @len_bef with the length of @axi now
        for character in axi: #for every letter in @axi
            if character.isalpha() and  character in info["rules"] :
                #if the character is 
                #a letter and there is a rule for it
                axi = axi + info["rules"][character] #adds to the word the rule
            else:
                axi = axi + character#adds only the symbol
        axi = axi[len_bef:] #assigns @axi the characters 
                            #from spot @len(axi) till end (throws previous characters away) 
    return(axi)

#function that creates file whose name was given as an argument in cmd 
#when no optional argument was typed
#after the creation of the file, it checks every character of the string of pattern
#from the axium and  creates the 2 pair of points accordingly
#in the end it closes the file creation
def file_createwith_coordinates(filename,info,axium):
    file_create = open(filename,"w+")#assigns @file_created with the name 
    #of the file we give from cmd
    angle = info["start_angle"] * math.pi / 180 #changes degrees to rad
    prev = (0,0) #initialize @prev with (0,0)
    point_memory = deque() #deque to store the point for the symbols []"
    angle_memory = deque() #deque to store the angle for the symbold []"
    for character in axium: #for every character in produced string of axium"
        if character.isupper() and character >= "A" and character <= "L": 
            #if  @character is a capital letter between A and L
            s = math.sin(angle) #assigns @s with the sine of the angle
            c = math.cos(angle) #assigns @c with the cosine of the angle
            xnex = round(prev[0] + info["step_length"] * c, 2) 
            #assigns @xnex with the change of abscissa
            #by adding the step_length to x prev
            #in the right direction (using the cosine of the angle)
            ynex = round(prev[1] + info["step_length"] * s, 2) 
            #assigns @ynex with the change of ordinate
            #by adding the step_length to y prev
            #in the right direction (using the sine of the angle)
            nex = (xnex,ynex) #@assigns @nex with the tuple xnex,ynex
            file_create.write("%s %s\n" % (str(prev), str(nex)))
            #writes @prev and @nex into  @file_create
            prev = (xnex,ynex) #gives @prev same value as @nex (nex is copied)
        elif character == "+": #if @character is +, turns left by left_angle degress
            angle = angle + (info["left_angle"] * math.pi / 180) 
            #transforms degrees of left_angle 
            #into rad and adds it to the angle as we turn left
        elif character == "-": #if @character is -, turns right by right_angle degrees
            angle = angle - info["right_angle"] * math.pi / 180
            #transforms degrees of right_angle 
            #into rad and subducts it from the angle as we turn right
        elif character == "[": #if @character is [, stores the spot and angle 
                                #the specific moment as we will come back to it in the future
            point_memory.append(prev) #adds @prev to list @point_memory
            angle_memory.append(angle) #adds @angle to list @angle_memory
        elif character == "]": #if @character is ], we go back to the last spot and angle
                                #that we store in @point_memory and @angle_memory
            prev = point_memory.pop() #pops @point_memory into @prev
            angle = angle_memory.pop() #pops @angle_memory into @angle
    file_create.close() #closes the file for no leaks    
    
                            
#MAIN
parser = argparse.ArgumentParser() #creation of parser
parser.add_argument('-m','--makestring',action="store_true",
                    help="prints the string of end axium after \
                    all rules applied for @order times")
#create the optional argument -m for showing the end string 
parser.add_argument('files',  
                    help="insert the json file to be used for the drawing as \
                    first and the file to be created as second if no optional \
                    argument is inserted",nargs='*')
#create the positional argument for the file input and output
#first argument will correspond to the input and second to the output file
# in case no optional argument is typed
parser.add_argument('-d','--decode_rewrite',action="store_true",
                    help="prints the string of end axium after \
                    edge rewriting and finding the rules of the shape")
#create the optional argument -d for the edge rewriting procedure
args = parser.parse_args() 
filename = args.files[0] #assigns @filename with the first positional argument
if args.decode_rewrite: #if -d is typed in cmd
    edge_rewrite(filename) #call function edge_rewrrite 
else:
    with open(filename) as json_data: #opens json file
        data = json.load(json_data) #loads json file into @data ( as dictionary)
    axi = axi_finder(data)#calls function axi_finder to get axi
    if args.makestring: #if -m was typed in cmd
        print(axi) 
    else: #neither -m nor -d was typed as optional arguments
        file_createwith_coordinates(args.files[1], data, axi) #calls function
   

    
   
    
        
        
    

