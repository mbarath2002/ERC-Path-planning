import matplotlib.pyplot as p
import math
import numpy as np
import random
import copy
from shapely.geometry import Point, Polygon
from shapely.geometry import LineString     #all relevant libraries included

class Node(object):
    def __init__(self, node):
        self.node=node
        self.parent = None                 #defining attributes of nodes generated, parent node is what each node in the list was previously generated from

def RRT(start,goal,obstacle_list):
    low=0                                  #bounds for random node generation
    high=10                           
    rate=0.25                              #distance between node and prev node each time new one added
    n=400
    s=Node(start)                          #s as an object containing start node
    stack=[s]
    p.scatter(start[0],start[1],color='r',s=5) #scatter plot radius node 5, color red
    p.scatter(goal[0],goal[1],color='r',s=5)
    while True:
      x=random.uniform(low,high)      #random node generation
      y=random.uniform(low,high)    
      rnd_node=(x,y)         
      dist= [(n.node[0]-rnd_node[0])**2 + (n.node[1]-rnd_node[1])**2 for n in stack] #calculating least distance from each node in list to find nearest node
      min_pos=dist.index(min(dist))    #taking that nodes position
      nearest_node=stack[min_pos]
      angle=math.atan2(y-nearest_node.node[1], x-nearest_node.node[0]) #angle/direction of new node from nearest node 
      new_node_x=nearest_node.node[0]+rate*math.cos(angle) #using cos , sin of angle and adding to rate we get the new node position
      new_node_y=nearest_node.node[1]+rate*math.sin(angle)
      new_node=(new_node_x,new_node_y)
      point=Point(new_node_x,new_node_y) #point to check
      coord=(new_node,nearest_node.node) #coordinates defined
      line=LineString(coord) #line connecting new node, nearest node
      if(point.within(Polygon(obstacle_list[0]))==False and point.within(Polygon(obstacle_list[1]))==False and point.within(Polygon(obstacle_list[2]))==False
         and line.crosses(Polygon(obstacle_list[0]))==False and line.crosses(Polygon(obstacle_list[1]))==False and line.crosses(Polygon(obstacle_list[2]))
          ==False and point.touches(Polygon(obstacle_list[0]))==False and point.touches(Polygon(obstacle_list[1])) ==False and point.touches(Polygon(obstacle_list[2]))==False):
        #checking if node is inside the obstacle, line between 2 nodes intersect or if it touches the boundary of an obstacle
          p.scatter(new_node_x,new_node_y,color='r',s=5) #scatter of each new node
          p.plot((nearest_node.node[0],new_node_x),(nearest_node.node[1],new_node_y),color='r') #connnecting each newnode created with nearest
          obj=Node(new_node) #obj of new node to save attributes
          obj.parent=min_pos # node of each new node
          stack.append(obj) #we append this object to the node list
          d_x= obj.node[0]-goal[0] #checking distance from goal
          d_y= obj.node[1]-goal[1]
          d= math.sqrt(d_x*d_x + d_y*d_y)
          if(d<=rate):
              print("goal reached")
              end=len(stack)-1
              path=[(goal)]
              while stack[end].parent is not None: #till we traverse through the entire array
                  path.append(stack[end].node) #starting from the last node we track its path by going through a chain of its parents till we reacg start
                  end=stack[end].parent
              path.append(start) 
              return path 

def visualize(path,obstacle_list):
    i=len(path)-1
    poly1=Polygon(obstacle_list[0]) #polygon set of points
    poly2=Polygon(obstacle_list[1])
    poly3=Polygon(obstacle_list[2])
    x1,y1=poly1.exterior.xy #defining coordinates for polygon plotting
    x2,y2=poly2.exterior.xy
    x3,y3=poly3.exterior.xy
    p.plot(x1,y1) #plotting
    p.plot(x2,y2)
    p.plot(x3,y3)
    while(i>0):
        p.plot((path[i][0],path[i-1][0]),(path[i][1],path[i-1][1]),color='g') #traverse though path and display each node from the end, denote it with green
        i=i-1

p.show() #display everything plotted
#each of the functions called and values passed from the main function
