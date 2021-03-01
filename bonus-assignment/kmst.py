# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 01:06:38 2019

@author: Stefanos
"""
import math
import pprint
import sys
import random

#function that gets as an argument the name of a file and 
#creates a dictionary @dic that contains the names of the points as keys
#and the coordinates of the points as values of the keys 
#coordinates will be tuples as (abscissa,ordinate)
#@filename must have the following format:
#s1 (5, 0)
#s2 (3, 7)
#s3 (10, 9)
#
#where s1, s2, s3 are the names of the points and the tuples are the coordinates
def open_textfile(filename): 
    dic={}
    with open(filename) as file_input:
            for line in file_input:
               g=line.split(' ') 
               dic[g[0]]=(float(g[1][1:-1]),float(g[2][:-2]))
    return (dic)

#function that gets two points: @p1, @p2 that are tuples (x,y) where 
#x is abscissa of the point and y is the ordinate
#returns the euclidean distance of those points. 
#In detail, for the euclidean distance:
#firstly calculate the difference of the abscissa of the two points 
#then the difference of the ordinate of the two points 
#then calculate the square of each difference , add them together
#lastly take the square root of the sum 
def euclidean_distance(p1,p2):
    return  math.sqrt( pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1],2))

#function that takes as argument two points @p1 @p2 that are tuples
#calculates and returns the midpoint of the line that starts from @p1 and 
#ends in @p2
#abscissa of the midpoint is the sum of abscissas of the points divided by 2
#ordinate of the midpoint is the sum of ordinates of the points divided by 2
def midpoint_finder(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

#function that gets as arguments the diameter and the center of a circle and
#calculates the 4 corners of the square of side @diameter circumscribing the 
#circle . Returns a list containing 2 corners as tuples (x,y) 
#(the left-low and the top-right corner)
def get_square_Q(diameter, center):
    right_high_corner=(center[0]+diameter/2,center[1]+diameter/2)
    #doing a diagramm it is easy to understand that: the
    #abscissa of the right_high_corner is the same as the biggest abscissa of the 
    #points of the circle and the
    #ordinate of the right_high_corner is the same as the biggest ordinate of the 
    #points of the circle 
    left_low_corner=(center[0]-diameter/2,center[1]-diameter/2)
    #accordingly we see for the left-low corner
    return [left_low_corner, right_high_corner]

#function that checks if a point (@point) is contained in a square (@square)
# @square is a list that contains two tuples, first tuple is the bottom left 
#corner of the square and second tuple is the upper right corner of the square
#let's say @point is a tuple (x,y) and @square is [(x1,y1),(x2,y2)]
#then @point is inside the square only if:
# x>x1 and y>y1 and x<=x2 and y<=y2
#returns true is the point is contained in the square
#false otherwise
#I consider that if a point is right on the border it will be contained
#only if it is on the upper or right side of the square
#otherwise two points could end up in the two different cells, leading to
#incorrect results
def check_point_in_square(point, square):
    start_corner=square[0] #assigns bottom-left corner of square to @start_corner
    end_corner=square[1]  #assigns upper-right corner of square to @end_corner
    if (point[0]>start_corner[0] and point[1] > start_corner[1] and point[0]<=end_corner[0] and point[1]<= end_corner[1]):
        #checks the abscissa and ordinates of the points as explained in the description
        return True
    return False

#a function that gets as arguments a list of points (@lis) whom we want to find
#the minimum spanning tree, a dictionary @S that contains the names of the points
#as keys and the coordinates(tuple (abscissa,ordinate)) of the points as values
# This function finds and returns the minimum spanning tree of the points in
# @lis according to the Prim's algorithm for mst.
#It works by keeping a list of visited points and a  dictionary that contains 
#other dictionaries of the distances , and everytime we look for the minimum 
#distance of a visited point to a not visited point
def prim_kmst(lis,S):
    num_points=len(lis) #number of points that the mst will have 
    distance={}
    for every_point in lis:
        distance[every_point]={}
        for second_point in lis:
            if every_point != second_point:
                distance[every_point][second_point]=euclidean_distance(S[every_point],S[second_point])
    #dictionary that contains as keys all the points and for every key 
    #it has an inner dictionary that contains all the other points ( except for 
    #the point that is the outer key) and after contains the distance 
    # for example :
    # {'s1': {'s2': 7.280109889280518,
    #        's3': 10.295630140987,
    #        's4': 5.0,
    #        's5': 7.211102550927978} ....}
    visited=[] #a list that contains the names of the points that have  already been visited
    solution={} #dictionary that contains the solution as: keys are tuples of the 
    #points that are connected and value is the distance of those points (in the tuple)
    # for example:
    #{('s1', 's9'): 5.0, ('s1', 's7'): 6.0 ....}
    len_mst=0 #variable to know how many coonections we  already have (number of edges)
    node_now=lis[0] #assigns first point to visit the first item of the list
    #it doesn't really matter which point we select to visit first
    while len_mst!= num_points-1 :
    #knowing that the kmst has one egge less than the nodes it connects 
    #we run the loop till len_mst=num_points-1
        visited.append(node_now) #node_now is considered visited
        min_dis= sys.maxsize #assign min_dis with a very big number
        for every_visited in visited:
            #for every point we have already visited we look for the 
            #minimum distance from that point to any unvisited point
            min_visited_distance=min(distance[every_visited].values())
            #@min_visited_distance is the minimum distance of the specific @every_visited 
            #between all the other points
            if min_visited_distance < min_dis:
               point_to_visit=list(distance[every_visited].keys())[list(distance[every_visited].values()).index(min_visited_distance)]
               #in order to find the point whom @every_visited is connected 
               #to with @min_visited_distance, we use this trick
               #( We know the outer key of the dictionary @distance and the 
               #value (@min_visited_distance) but we are looking for the inner key)
               node_now=every_visited
               min_dis=min_visited_distance
        for every_visited in visited:
            #in order for all of this to work, we need to delete the points and distances 
            #that we can't use anymore because there is already a connection
            #As a result, we delete the points and distances of all the visited 
            #points and the newpoint(@point_to_visit)
            del distance[every_visited][point_to_visit]
            del distance [point_to_visit][every_visited]
        len_mst +=1 #number of edges is increased by one
        solution[(node_now,point_to_visit)]=min_dis
        node_now=point_to_visit #node_now is the new point we visit
    return solution

#MAIN
file = sys.argv[1]
k = int(sys.argv[2]) #minimum ammount of points that the tree is spanning
S=open_textfile(file)   
#in order for the algorithm to work, k must have a square root that is an integer. 
# In detail, for step (4) where we divide Q into k square cells,
# the square cells will have equal dimensions and area(emvadon)
#only if there are sqrt(k) rows and sqrt(k) columns inside the square Q .
# As a result sqrt(k) must be an integer otherwise the algorithm can't work
while k< len(S) and not (math.sqrt(k)).is_integer():
    #The programm will return the mst for at least k points (sum of points is n)
    #We continiously increase k till it reaches an integer that has 
    # a square root that is an integer or till k equals to n
    k+=1
solution={}#dictionary that contains solutions and  
        #is used to get every  distinct pair of points
#When k is equal to n(sum of points), we only need to construct  one minimum
#spanning tree for all the n points and the solution is the length of it 
if k==len(S):
    solution= prim_kmst(list(S.keys()),S)
    len_tree=sum(solution.values())
    print("For ",k," points the MST has length: ",len_tree)
    print("The links that were used are: ")
    pprint.pprint(solution)   
else:
#k is less than  n (sum of points) so we follow the steps from the paper    
    min_length=sys.maxsize
    for p1 in S.keys():
        for p2 in S.keys():
            #for every distinct pair of points
            #we achieve that by appending to the dictionary @solution
            #the mst between the two points
            #so we just check if the pair of points we examine, exists in the 
            #dic @solution and also if the the two points are not the same
            if ((p1,p2) not in solution) and p1!=p2:
                d=math.sqrt(3) * euclidean_distance(S[p1], S[p2])
                #d is the diameter of the circle centered in the midpoint of
                #the line segment of p1, p2
                midpoint= midpoint_finder(S[p1],S[p2])
                #calculate the midpoint from the function
                sc=[] # subset of S contained in C
                for point in S.keys():
                    if (euclidean_distance(S[point],midpoint)<d/2): 
                        #if distance between @midpoint and @point is less than 
                        #diameter/2 (radius), then @point is contained in the circle
                        sc.append(point)
                if len(sc)< k:     #if sc contains fewer than k points               
                    solution[(p2,p1)]=None #enter in dictionary @solution
                    #so that we don't check the same pair of points again
                    continue #skip to the next iteration
                Q=get_square_Q(d,midpoint)
                #Q be is the square of side d circumscribing C.
                cells={}
                #initialize the list @cells which will contain lists of points 
                #which are placed in the specific cell
                for i in range (int(math.sqrt(k))):
                    for j in range (int(math.sqrt(k))):
                        cells[(i,j)]=[]
                sum_points_of_cell=[[0 for j in range (int(math.sqrt(k)))] for i in range (int(math.sqrt(k)))]
                #a list that contains the sum of points inside every cell
                #for instance the sum of cell (1,2) will be sum_points_of_cell[1][2]
                for point in sc:
                #for every point that is contained in the circle C
                    point_change=(S[point][0]-Q[0][0],S[point][1]-Q[0][1])
                    #we transform all points by considering that the bottom left 
                    #corner of the square Q is the start of axis so that we can
                    #calculate in which cell every point is by using the 
                    #operator //
                    x_cell=int(point_change[0] // (d/math.sqrt(k)))
                    y_cell=int(point_change[1]// (d/math.sqrt(k)))
                    #each square cell has a side d/sqrt(k)
                    #in order to know in which cell the point is, we divide by
                    # (d/sqrt(k)) and the integer of the result is the position of the cell 
                    #we do the above for both the abscissa and the ordinate
                    sum_points_of_cell[x_cell][y_cell]+=1
                    #increase the sum of points in the specific cell by one
                    cells[(x_cell,y_cell)].append(point)
                    #append the point as value of the dictionary @cells with 
                    # key the coordinates of the cell it is in the square Q
                sort_list=[]
                #sorting the cells by finding the max in sum_points_of_cell
                #Then finding the index of the max, for both the inner and outer list
                #@sum_points_of_cell is a list that contains lists 
                #then we assign the sum_points_of_cell[x_max][y_max] with -1 
                #so that we don't encounter it again
                for i in range (int(math.sqrt(k))):
                    for j in range (int(math.sqrt(k))):
                        max_value=max([max(every_lis) for every_lis in sum_points_of_cell])
                        #finding the max_value of the whole list
                        for z in range (int(math.sqrt(k))):
                            if max_value in sum_points_of_cell[z]:
                                x_max=z
                                #finding the index of the list that max_value 
                                #is contained (outer) that index is the 
                                #abscissa of the cell  that contains the most points
                                break
                        y_max=sum_points_of_cell[x_max].index(max_value)
                        #finding the index of the inner list where max_value is found
                        #that index is the ordinate of the cell that contains the most points
                        sort_list.append((x_max,y_max))
                        #append to sort_list
                        sum_points_of_cell[x_max][y_max]=-1
                        #so that we don't encounter the same cell again
                sum_selected=0 #variable to know how many points are contained so far
                counter=0 #variable to know the index of @sort_list that we are at
                point_selected=[]# list that will contain all the k points
                while sum_selected<k:
                    #as long as we haven't selected k points the loop is going
                    cell_now=sort_list[counter]
                    #gets the cells from the ones that contain the most points to less
                    #as sort_list is sorted
                    for point in cells[cell_now]:
                    #for every point that is contained in the specific cell (@cell_now)
                        sum_selected+=1
                        point_selected.append(point)
                    counter +=1
                sum_of_lastcell=len(cells[cell_now])#finds the sum of points added
                #from the last chosen cell
                #
                #This loop randomly discards points from the last cell so that
                #the sum of points selected (in list @point_selected) is 
                #equal to k
                while len(point_selected)!=k:
                    #while we have selected more than k points 
                    point_to_pop=random.randint(len(point_selected)-sum_of_lastcell,len(point_selected)-1)
                    #gets a random number that corresponds to an index
                    #of a point that belonged to the last chosen cell
                    #that was used to collect the needed points
                    point_selected.pop(point_to_pop)
                    sum_of_lastcell-=1
                    #reducing the variable @sum_of_cell in order not to 
                    #discard any points that don't belong to the last chosen cell
                    #(We only want to discard points from the last chosen cell)
                solution[(p2,p1)]=prim_kmst(point_selected,S)
                #finding the mst for the k points in the list @point_selected
                len_tree=sum(solution[(p2,p1)].values())
                #length is the sum of all distances of the connections
                if len_tree < min_length:
                    min_length=len_tree
                    min_len_pair=(p2,p1)
    print("For ",k," points the MST has length: ",min_length)
    print("The links that were used are: ")
    pprint.pprint(solution[min_len_pair])