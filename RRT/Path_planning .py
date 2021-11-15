import matplotlib.pyplot as p
import math
import numpy as np
import random
import copy
from shapely.geometry import Point, Polygon
from shapely.geometry import LineString

class Node(object):
    def __init__(self, node):
        self.node=node
        self.parent = None

def RRT(start,goal,obstacle_list):
    low=0
    high=10                           
    rate=0.25
    n=400
    s=Node(start)
    stack=[s]
    p.scatter(start[0],start[1],color='r',s=5)
    p.scatter(goal[0],goal[1],color='r',s=5)
    while True:
      x=random.uniform(low,high)      
      y=random.uniform(low,high)    
      rnd_node=(x,y)         
      dist= [(n.node[0]-rnd_node[0])**2 + (n.node[1]-rnd_node[1])**2 for n in stack] 
      min_pos=dist.index(min(dist))    
      nearest_node=stack[min_pos]
      angle=math.atan2(y-nearest_node.node[1], x-nearest_node.node[0]) 
      new_node_x=nearest_node.node[0]+rate*math.cos(angle) 
      new_node_y=nearest_node.node[1]+rate*math.sin(angle)
      new_node=(new_node_x,new_node_y)
      point=Point(new_node_x,new_node_y)
      coord=(new_node,nearest_node.node)
      line=LineString(coord)
      if(point.within(Polygon(obstacle_list[0]))==False and point.within(Polygon(obstacle_list[1]))==False and point.within(Polygon(obstacle_list[2]))==False
         and line.crosses(Polygon(obstacle_list[0]))==False and line.crosses(Polygon(obstacle_list[1]))==False and line.crosses(Polygon(obstacle_list[2]))
          ==False and point.touches(Polygon(obstacle_list[0]))==False and point.touches(Polygon(obstacle_list[1])) ==False and point.touches(Polygon(obstacle_list[2]))==False):
          p.scatter(new_node_x,new_node_y,color='r',s=5)
          p.plot((nearest_node.node[0],new_node_x),(nearest_node.node[1],new_node_y),color='r')
          obj=Node(new_node)
          obj.parent=min_pos
          stack.append(obj)
          d_x= obj.node[0]-goal[0]
          d_y= obj.node[1]-goal[1]
          d= math.sqrt(d_x*d_x + d_y*d_y)
          if(d<=rate):
              print("goal reached")
              end=len(stack)-1
              path=[(goal)]
              while stack[end].parent is not None:
                  path.append(stack[end].node)
                  end=stack[end].parent
              path.append(start)
              return path

def visualize(path,obstacle_list):
    i=len(path)-1
    poly1=Polygon(obstacle_list[0])
    poly2=Polygon(obstacle_list[1])
    poly3=Polygon(obstacle_list[2])
    x1,y1=poly1.exterior.xy
    x2,y2=poly2.exterior.xy
    x3,y3=poly3.exterior.xy
    p.plot(x1,y1)
    p.plot(x2,y2)
    p.plot(x3,y3)
    while(i>0):
        p.plot((path[i][0],path[i-1][0]),(path[i][1],path[i-1][1]),color='g')
        i=i-1

def main():
    print("Start")
    start = (1, 1)
    goal = (10, 10)
    obstacle_list=[
            [(2, 10), (7, 10), (6, 7), (4, 7), (4, 9), (2, 9)],
            [(3, 1), (3, 6), (4, 6), (4, 1)],
            [(7, 3), (7, 8), (9, 8), (9, 3)],
        ]
    path = RRT(start,goal,obstacle_list)
    visualize(path,obstacle_list)
    
if __name__ == '__main__':
    main()

p.show()
