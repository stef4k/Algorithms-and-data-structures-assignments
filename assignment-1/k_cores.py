# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 02:00:32 2019

@author: stef4k
"""
import sys

#function to create the priority queue
def create_pq():
    return []

#function that adds an element in the end of the queue
def add_last(pq, c):
   pq.append(c)

#function that returns the position of the root
def root(pq):
    return 0

#function that assigns an element to the queue. However, if the queue is empty,
#it will be changed to a one element list. Otherwise, the element will be put 
#to position 0 
def set_root(pq, c):
    if len(pq) == 0:
        pq = [c]
    else:
        pq[0] = c

#function that returns the data stored at specific position of the queue
def get_data(pq, p):
    return pq[p]

#function that returns the children of an element in the queue
def children(pq, p):
    if 2*p + 2 < len(pq):
        return [2*p + 1, 2*p + 2]
    else:
        return [2*p + 1]     

#function that returns the parent of an element
def parent(p):
    return (p - 1) // 2

#function that swaps two elements of the queue
def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]

#function that inserts an element in the queue and keeps swaping it with 
#its parent  if its value is  less that its parent's value
def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p
        
#function that extracts the last element of the queue
def extract_last_from_pq(pq):
    return pq.pop()   
     
#function that checks whether an element has children
def has_children(pq, p):
    return 2*p + 1 < len(pq)

#function that extracts the minimum element of the queue and swaps children
#with parents if their value is less
def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c        
        exchange(pq, i, j)
        i = j
    return c

   
#function that finds index of queue by starting searching in index @ind
# @pq is the priority queue, @pair is the  pair we want to find 
#and @ind is the index we check first
#recursively searches the tree from root to  children 
def indexfind(pq,pair,ind):
    if get_data(pq,ind)==pair:#if @pair is the same as the containing of this exact element
        return ind #end function and return the index of this branch
    elif get_data(pq,ind)[0]<=pair[0] and has_children(pq,ind): 
        #if value of pair is greater than or equl examined element 
        #and the  element has children
            kids=children(pq,ind) #assign @kids as the result of function children() #not needed
            for u in kids: # for every element in the list kids #for u in children(pq,ind)
                indInKids=indexfind(pq,pair,u) #examine the child,by recursion
                if indInKids is not None: #if the value of indInKids is not null
                 return indInKids #return it and end function


#function that fixes the queue structure after the exchange of elements 
#in function updatePQ(). It continiously checks if the position now
#is not the root of queue and if the value of the parent of the element 
#that has index @index is greater than the element and then exchanges parent with child
def fixQueueStructure(pq,index):
 while (index!=root(pq) and get_data(pq,index)[0]<get_data(pq,parent(index))[0]):
            #if the newpair is not the  root  and its value is less 
            #than its parent value, it swaps it with its' parent
            p = parent(index)
            exchange(pq, index, p)
            index = p
            

#function that updates the queue. Firstly, it searches the index of @oldpair,
# then it inserts the @newpair (as last in the queue),
#swaps it with the @oldpair and extracts the last element (oldpair), 
def updatePQ(pq,oldpair,newpair):
        indx=indexfind(pq,oldpair,0)#gets the index of the oldpair in the queue
                                #from function indexfind() starting from root
        add_last(pq,newpair) #inserts the newpair in the last spot of the queue
        exchange(pq,indx,len(pq)-1)#exchange the elements oldpair and newpair 
                             #as the newpair is in the last spot of the queue
        extract_last_from_pq(pq)#exctracts the last element of pq (which is the oldpair)
        fixQueueStructure(pq,indx)#fixes the queue according the priority queue rules
            
    

#kcores method with input graph @G and result cores that
#contains the k-core of node i in spot i of the list
def KCores(G):
    mh=create_pq()
    d=[len(G[i]) for i in range  (len(G))] #fills d with number of neighboors of every node
    p=d[:] #create list p, with the same values as d
    core=[0 for i in range (len(G))]#initialize core with 0 for every spot
    for u in range (len(G)):
        pn=[p[u],u]
        insert_in_pq(mh, pn)
    while (len(mh)>0):
        t=extract_min_from_pq(mh)
        core[t[1]]=t[0]
        if (len(mh)!=0):
            for u in G[t[1]]:
                d[u]-=1
                opn=[p[u],u]
                p[u]=max([t[0],d[u]])
                npn=[p[u],u]
                if  core[u]==0 and opn[0]!=npn[0]:
                    #checks if u is in the priority queue by checking list core[u] 
                    #(if core[u] is 0 then it is true)
                    #and also checks if first element of opn and npn are different
                   updatePQ(mh,opn,npn)#calls update function
    return core #ends function KCores()
                
    
#function that reads a graph from a file    
def readgraph(file) :   
    g = {}
    with open(file) as graph_input:
        for line in graph_input:
            # Split line and convert line parts to integers.
            nodes = [int(x) for x in line.split()]
            if len(nodes) != 2:
                continue
            # If a node is not already in the graph
            # we must create a new empty list.
            if nodes[0] not in g:
                g[nodes[0]] = []
            if nodes[1] not in g:
                g[nodes[1]] = []
                # We need to append the "to" node
                # to the existing list for the "from" node.
            g[nodes[0]].append(nodes[1])
            # And also the other way round.
            g[nodes[1]].append(nodes[0])
    return g

#start of main programm
if (len(sys.argv)==2): #checks if we entered two arguments from the cmd
    filename =sys.argv[1] #variable filename is assigned with the string 2nd argument
else:
    if (len(sys.argv)<2):
        print("Error,less than two arguments entered in commandline")
    else:
        print ("Error, more than two arguments entered in command line")
    sys.exit() #ends the programm if we didn't enter exactly two arguments
graph=readgraph(filename) #variable graph is assigned with the result of function readgraph()
core=KCores(graph)#variable core is assigned with the result of function KCores()
                #it contains the number of every node and the core of the node
for i in range (len(core)):
    print(i,core[i]) #prints the node number and core number of it
                
