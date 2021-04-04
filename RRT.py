import matplotlib.pyplot as p
import math
import numpy as np
import random

def collision(node,obstacle_list):
flag=0

def RRT(start,goal,obstacle_list):
min=0
max=10                           #bounds of region to generate random node
rate=0.5                         #distance of node expansion when adding new node
n=400
list=[start]                     #list of nodes
x=random.uniform(min,max)        #random node generation
y=random.uniform(min,max)    
rnd_node=(x,y)         
dist= [(node[0]-rnd_node[0])**2 + (node[1]-rnd_node[1])**2 for node in list] #distance of nearest node in list
min_pos=dist.index(min(dist)) #position noded to add to list
nearest_node=list[min_pos]
angle=math.atan2(y-nearest_node[1], x-nearest_node[0]) 
new_node_x=nearest_node[0]+rate*math.cos(angle) #expanding nodes in that direction
new_node_y=nearest_node[1]+rate*math.sin(angle)
new_node=(new_node_x,new_node_y)
list.append[new_node] #add new node to list
d_x= new_node[0]-goal[0]
d_y= new_node[1]-goal[1]
d= math.sqrt(d_x**2 + d_y**2)
if(d<=rate):
  print("goal reached")
else:
  

def visualize(path,obstacle_list):
