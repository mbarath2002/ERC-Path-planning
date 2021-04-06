import matplotlib.pyplot as p
import math
import numpy as np
import random

def collision(node,obstacle_list):
flag=0

class Node(object):
    def __init__(self, node):
        self.parent = None

def RRT(start,goal,obstacle_list):
    min=0
    max=10                           #bounds of region to generate random node
    rate=0.5                         #distance of node expansion when adding new node
    n=400
    list=[start]                     #list of nodes
    while True:
        x=random.uniform(min,max)      #random node generation
        y=random.uniform(min,max)    
        rnd_node=(x,y)         
        dist= [(node[0]-rnd_node[0])**2 + (node[1]-rnd_node[1])**2 for node in list] #distance of nearest node in list
        min_pos=dist.index(min(dist)) #position noded to add to list
        nearest_node=list[min_pos]
        angle=math.atan2(y-nearest_node[1], x-nearest_node[0]) 
        new_node_x=nearest_node[0]+rate*math.cos(angle) #expanding nodes in that direction
        new_node_y=nearest_node[1]+rate*math.sin(angle)
        new_node=(new_node_x,new_node_y)
        new_node=Node(new_node)
        new_node.parent=min_pos
        list.append[new_node]           #add new node to list
        p.plot((new_node[0],nearest_node[0]),(new_node[1],nearest_node[1]))
        p.show()
        d_x= new_node[0]-goal[0]
        d_y= new_node[1]-goal[1]
        d= math.sqrt(d_x**2 + d_y**2)
        if(d<=rate):
            print("goal reached")
            break;
    end=len(list)-1
    path=[goal]
    while list[end].parent is not None:
        path.append(list[end])
        end=list[end].parent
    path.append(start)
    return path

def visualize(path):
    i=len(path)-2
    p.plot((start[0],path[i][0]),(start[1],path[i][1]))
    while(i>0):
        p.plot((path[i][0],path[i-1][0]),(path[i][1],path[i-1][1]))
        i=i-1
        p.show()
        
def main():
    obstacle_list = [
            [(2, 10), (7, 10), (6, 7), (4, 7), (4, 9), (2, 9)],
            [(3, 1), (3, 6), (4, 6), (4, 1)],
            [(7, 3), (7, 8), (9, 8), (9, 3)],
        ]

    start = (1, 1)
    goal = (10, 10)
    path = RRT(start,goal)
    visualize(path)
    
if __name__ == '__main__':
    main()
                                  
