# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 20:42:14 2019

@author: stef4k
"""
import sys
import Levenshtein #import Levenshtein through virtual environment
from collections  import deque  

#function that reads dictionary text file and returns a list containing the elements of it    
def readfile(file) :   
    g = []
    with open(file) as graph_input:
        for line in graph_input:
            g.append(str(line.split()[0])) #adds word of the specific line to list as key and an diferent int as value(like an id)
    return g

#function that sets the root of the tree (inserts a word as key in the dictionary)
#also creates a dictionary inside the dictionary @tree for key @element
def setRoot(tree,element):      
    tree[element] = {}
    
#function that finds and returns the root of the bktree(first key of @tree)
def getRoot(tree):
    #return list(tree)[0]#gets element with index 0
    return next(iter(tree))

#function that returns the child of a node that has a specific distance
#if it exists else returns None
def getChild(element,dist):                       
    return diction_with_distance[element].get(dist)
         #return the value of the nested dictionary with inner key @dist and outer key @element   
    
#function that updates @tree
# after the adding of a new child
def addChild(par,dist,element,tree):
    tree[element] = {} #creates an empty nested dictionary for key @element
    tree[par][dist] = element #inserts into nested dictionary @element for inner key @dist and outer key @par
    
#function that inserts a word in the bk tree(saved as dictionary)
#first word to be inserted is the root of the tree
#every node of the tree can have unlimited children (children>=0)
#bk tree will help finding efficiently the neighboors(levenstein distance=1) of every word
def BK_tree_insertion(bk_with_distance,word):
    if not (bk_with_distance):#if bk is empty
        setRoot(bk_with_distance,word)#call function setRoot()
        return       
    node = getRoot(bk_with_distance)   #assigns @node  the first element of bktree (root of the tree)
    while node:     #while node is not none
        parent = node      #assign parent with the value of node
        distance = Levenshtein.distance(node,word)    #get distance between @node and @word           
        node = getChild(node,distance)   #calls function getChild() to see if node has a child wit distance @distance 
        if node is None:
            addChild(parent,distance, word,bk_with_distance)#calls functions addChild          
        
#function that finds quickly the words that have Levenstein distance =1 from a word that we are interested
def BK_tree_search(bk_with_distance,word):
    results = set() #creates empty set @results
    to_check = deque([getRoot(bk_with_distance)])#creates deque with element the root of the bktree inside
    while to_check: #while deque is not empty
        node = to_check.popleft() #pops first element that we put inside
        distance = Levenshtein.distance(node,word) #gets the levenstein distance
        if distance == 1: 
            results.add(node) #adds the node to the results list
        l = distance-1
        h = distance+1
        for d in bk_with_distance[node]: #for every inner key(distance) that has outer key @node in bk_with_distance
            if d >= l and d <= h:
                to_check.append(bk_with_distance[node][d]) #adds node that has outer key @node and inner key @d in the deque
    return results

#function dijkstra for our case
#instead of a deque we use a list @pq where we get the minimum every time
#In start we only initialize the start word and in every reccurrence , the neighbors of the @u are initialized
def dijkstra(bk_with_distance, s,e):
    # Initialize dictionary holding path lengths, we only put the starting word
    dist = {s : 0}
    pred = { s : -1, e : -1 }    # Initialize dictionary holding node predecessors.
    pq = dist.copy()# Initialize the priority queue; initially it 
                # is just the same with the distance dictionary.
    elements_in_queue = 1 #initialize elements in queue (the amount lowers per 1 every recurrence and can also increase )
    while elements_in_queue != 0:         
        u = min(pq, key=pq.get) #gets the key of the minimum value in pq 
        pq[u] = MAX_INT
        elements_in_queue -= 1
        for v in BK_tree_search(bk_with_distance,u): #for every neighbor of @u
            if v not in dist: #if v is not in dictionary @dist
                dist[v]=MAX_INT  #we add @v to the dictionary @dist with the value of MAX_INT
                elements_in_queue+=1 #increase of elements_in_queue by 1
            if  dist[v] > dist[u] + 1: # If a better path is found,
                dist[v] = dist[u] + 1 # relax the distance and update the priority queue.
                pred[v] = u
                if (v == e):#reached the shortest path so return results                                              
                    return pred
                pq[v] = dist[v]+Levenshtein.distance(v,e) #update pq with the distance from the @wordstart plus the levenstein
                #distance to the @wordend for more efficient search of the shortest path
    return pred


#MAIN
MAX_INT = sys.maxsize
file_name = sys.argv[1]
wordstart = sys.argv[2]
wordend = sys.argv[3]
diction = readfile(file_name)#creates a list with all the words of the dictionary
diction_with_distance = {} #creates an empty dictionary
index_wordstart=diction.index(wordstart)#gets index of wordstart in list @diction
diction[0],diction[index_wordstart]=diction[index_wordstart], diction[0]#switches position of first item and wordstart in @diction 
#swaping wordstart with the first word of the list so that the bk_tree_search takes less time 
for u in diction:
    BK_tree_insertion(diction_with_distance,u)
#inserts every word of the dictionary in the diction_with_distance as well as the distance 
#so @diction_with_distance will look like :
#{food:{1:good,
#       2:cook,
#       3:spoon}
#good:{2:fold}
#cook:{}
#spoon:{5:farm}
#fold:{}
#farm:{} }  
exchange = False#to know if we exchanged @wordstart with @wordend
#checks which word has less neighbors so that we start the dijkstra function 
#from it. Starting from the word that has less neighbors  means that we won't
#encounter many dead ends in the beginning and as a result it will usually check
#less words and furthermore will take less time. Lastly, exchanging the words 
#doesn't influence the results as the path from a to b is the same as the path 
#from b to a but with the reversed turn
if len(BK_tree_search(diction_with_distance,wordstart)) > len(BK_tree_search(diction_with_distance,wordend)):
    exchange = True
    wordstart,wordend = wordend,wordstart
elif len(BK_tree_search(diction_with_distance,wordstart)) == len(BK_tree_search(diction_with_distance,wordend)):
    #if the words have the same amount of neighbors , we use the longer word as 
    #@wordstart because the longer word will usually have less neighbors of the neighbors
    #as there are more short than long words
    if (len(wordend)>=len(wordstart)):
        exchange = True
        wordstart,wordend = wordend,wordstart
res = dijkstra(diction_with_distance,wordstart,wordend)
if res[wordend] != -1:#checks if there is a path from @wordstart to @wordend
    previous = wordend
    output = []
    while (previous !=-1):#while we haven't reached the wordstart
        output.append(previous)#adds the word to list output
        previous = res[previous]#assigns previous with the previous word of the path from @res
    if exchange:
        print (', '.join(output[::]))
    else:
        print(', '.join(output[::-1])) # correct print
else:#there is no path from @wordstart to @wordend
    if exchange:
        print(wordend)
    else:
        print(wordstart)
