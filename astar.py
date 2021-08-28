import matplotlib.pyplot as plt
import random
import math
import operator
from shapely.geometry import Point, Polygon, LineString

class Node:

    def __init__(self,x,y,cost,parent,nearest_nodes,index):

        self.x=x
        self.y=y
        self.parent=parent
        self.score=score
        self.nearest_nodes=nearest_nodes
        self.index=index

class Astar:
    
    def __init__(self,obstacle_list):
        self.obstacle_list=obstacle_list

    start=(0,0)
    goal=(9,9)
    max_cord=(10,10)
    min_cord=(0,0)
    num_nodes=2000
    rate=0.5

    def path(self):
        
        #Generating the node network
            nodes=[]
            nodes.append(Node(start[0],start[1],0,0,[],0))

            for i in range(0,num_nodes):
                rnd_node=(random.uniform(0,10),random.uniform(0,10))
                node=Node(rnd_node[0],rnd_node[1],0,0,[],len(nodes))

            if(within(self.obstacle_list,rnd_node)==True):
                continue
            nodes.append(node)

            for i in range(0,len(nodes)-1):
                dist=math.sqrt((rnd_node[0]-nodes[i].x)**2 + (rnd_node[0]-nodes[i].y)**2)
                if(dist<=rate and cross(self.obstacle_list,rnd_node,nodes[i])==False):
                    nodes[i].nearest_nodes.append[len(nodes)-1]
                    nodes[len(nodes)-1].nearest_nodes.append(i)
    
        nodes.append(goal[0],goal[1],0,0,[],len(nodes)
            for i in range(0,len(nodes)):
            dist=math.sqrt((nodes[i].x-goal[0])**2 + (nodes[i].y-goal[1])**2)
            if(dist<=rate and cross(self.obstacle_list,rnd_node,nodes[i])==False):
                nodes[i].nearest_nodes.append(len(nodes)-1)
                nodes[len(nodes-1)].nearest_nodes.append(i)
    
        #Astar
        #start
        open_list=[]
        IsGoal=False
        for node in nodes:
            node.cost=1000000000
        nodes[0].cost=0
        for index in nodes[0].nearest_nodes:
            nodes[index].cost=math.sqrt((nodes[0].x-nodes[index].x)**2 + (nodes[0].y-nodes[index].y)**2) + math.sqrt(nodes[index].x-goal[0])**2 + (nodes[index].y-goal[1])**2)
            nodes[index].parent=0
        
        for node in nodes:
            open_list.append([node.index,node.score])
        open_list.sort(key=lambda x:x[1])

        while(Isgoal==False && len(open_list)>0):
            if(open_list[0][0]==len(nodes)-1): 
                #len(nodes)-1 is the last nodes index 
                IsGoal=True
            
            for index in nodes[open_list[0][0]].nearest_nodes:
                cost=nodes[0][0].score+ math.sqrt((nodes(open_list[0][0]).x-nodes[index].x)**2 + (nodes(open_list[0][0]).y-nodes[index].y)**2) + math.sqrt((nodes[index].x-goal[0])**2 + (nodes[index].y-goal[1])**2)
                if(cost<nodes[index].score):
                    nodes[index].score=cost
                    nodes[index].parent=open_list[0][0]
            
            open_list.pop(0)
            for array in open_list:
                array[1]=node[array[0]].cost
            open_list.sort(key=lambda x:x[1])

        poly1=Polygon(obstacle_list[0])
        poly2=Polygon(obstacle_list[1])
        poly3=Polygon(obstacle_list[2])
        x1,y1=poly1.exterior.xy
        x2,y2=poly2.exterior.xy
        x3,y3=poly3.exterior.xy
        p.plot(x1,y1)
        p.plot(x2,y2)
        p.plot(x3,y3)
        #plotting the nodes and path
        for node in nodes:
            for index in node.nearest_nodes:
                plt.plot([node.x,nodes[index].x],[node.y,nodes[index].y],color='r') 
        
        current=len(nodes)-1
        plot_list=[]

        while(current!=0):
            plot_list.append(nodes[current])
            current=nodes[current].parent

        plot_list.append(Node(start[0],start[1],0,0,[],0))
        reverse(plot_list)
        i=0
        while i<len(plot_list)-1:
            plt.plot([plot_list[i].x,plot_list[i+1].x],[plot_list[i].y,plot_list[i+1].y],color='blue')
        
    def within(self,obstacle_list,rnd_node):
        #checking if point is valid
        isWithin=False
        point=Point(rnd_node[0],rnd_node[1])
        if(point.within(Polygon(obstacle_list[0]))==True or point.within(Polygon(obstacle_list[1]))==True or point.within(Polygon(obstacle_list[2]))==True)
            isWithin=True
        return isWithin

    def cross(self,obstacle_list,rnd_node,node):
        isCrosses=False
        point=Point(rnd_node[0],rnd_node[1])
        line=LineString(rnd_node,node)
        if(line.crosses(Polygon(obstacle_list[0]))==True or line.crosses(Polygon(obstacle_list[1]))==True or line.crosses(Polygon(obstacle_list[2]))==True or point.touches(Polygon(obstacle_list[0]))==True or point.touches(Polygon(obstacle_list[1])) ==True or point.touches(Polygon(obstacle_list[2]))==True):
            isCrosses=True
        return isCrosses

def main():
    print("start planning")
    obstacles=[[(2, 10), (7, 10), (6, 7), (4, 7), (4, 9), (2, 9)],[(3, 1), (3, 6), (4, 6), (4, 1)],[(7, 3), (7, 8), (9, 8), (9, 3)]]
    astar=Astar(obstacles)
    astar.path()

if __name__=="main":
    main()
    
