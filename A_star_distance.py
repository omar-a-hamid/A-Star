import traci
import sumolib

import pandas as pd
#TODO: bug some time it fetches the speed zero
"""
TODO: 

import traffic data, csv? 

csv --> 
    
                edge        E0        E2      E3        E4      E5      E6      E6      ...
     
        time     

        12:00             60KM/Hr  60KM/Hr  60KM/Hr  60KM/Hr  60KM/Hr 
        12:01             60KM/Hr  60KM/Hr  60KM/Hr  60KM/Hr  60KM/Hr
        12:02             60KM/Hr  60KM/Hr  60KM/Hr  60KM/Hr  60KM/Hr
          .
          .
          .

    current time
          if current time == time stamp 
          edge == edge fetch speed? 

    currrent time += time previous edge 


define a function to measure time from distance 

config file for edges 

how do you pass start and end node

for edge in edges
    
    edge.get_traffic()
    


"""
"""
def get_Time

   return  edge. length / edge.get_traffic()


def get traffic(time, edge): 


    return traffic_df[time, edge]
"""


ds = pd.read_csv("traffic.csv")
df = pd.pivot_table(ds,index = 'dateandtime')
def get_traffic(edge,time): 

    try: 
        return df.loc[str(time), str(edge)]
    except:
        return 60


# print(df['dateandtime'])


df.loc['2022-12-07 08:48:00','26253984#3']=1
print(df.loc['2022-12-07 08:48:00','26253984#3'])


df.loc['2022-12-07 08:48:00','-26253996#2']=1
print(df.loc['2022-12-07 08:48:00','-26253996#2'])


def get_time(edge,time):
    try:
        return net.getEdge(edge).getLength() / get_traffic( edge,time)
    except:
        return net.getEdge(edge).getLength() / 50
    
time = '2022-12-07 08:48:00'

# start the simulation and connect to it
traci.start(["sumo", "-c", "osm.sumocfg"])

# define the start and goal nodes
start_node = '287524294'
goal_node = "6570524692"

net = sumolib.net.readNet('osm.net.xml')

# define the heuristic function (in this case, it's just the Euclidean distance)
def heuristic(node):
    print("Node: ",node)
    # print("**************************")
    # print("**************************")
    # print("**************************")

    node_x, node_y = net.getNode(node).getCoord()
    goal_x, goal_y = net.getNode(goal_node).getCoord()
    print("H: ",(((node_x - goal_x)**2 + (node_y - goal_y)**2)**0.5)/60)
    return (((node_x - goal_x)**2 + (node_y - goal_y)**2)**0.5)/45
    # return (((node_x - goal_x)**2 + (node_y - goal_y)**2)**0.5)


# define the A* algorithm function

"""
def a_star(start_node, goal_node):
    open_set = [start_node]
    came_from = {}
    g_score = {start_node: 0}
    f_score = {start_node: heuristic(start_node)}
    
    while open_set:
        current_node = min(open_set, key=lambda node: f_score[node])
        if current_node == goal_node:
            path = [current_node]
            print(came_from)
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path
            
        open_set.remove(current_node)
        
        for neighbor_str in net.getNode(current_node).getOutgoing():
            neighbor = neighbor_str.getID() 

            neighbor_node = net.getEdge(neighbor).getToNode()
            # traci.simulation.getEdgeTarget(neighbor)
            # tentative_g_score = g_score[current_node] +   net.getEdge(neighbor).getLength() #
            print('edge: ',neighbor)
            tentative_g_score = g_score[current_node] +   get_time(neighbor,time) #
            print("g: ",get_time(neighbor,time) )
              
            
            if neighbor_node not in g_score or tentative_g_score < g_score[neighbor_node]:
                neighbor_node = neighbor_node.getID()
                came_from[neighbor_node] = current_node
                g_score[neighbor_node] = tentative_g_score

                f_score[neighbor_node] = tentative_g_score + heuristic(neighbor_node)
                
                if neighbor_node not in open_set:
                    open_set.append(neighbor_node)
                    
    return None

"""
def a_star(start_node, goal_node):
    open_set = [start_node]
    came_from = {}
    g_score = {start_node: 0}
    f_score = {start_node: heuristic(start_node)}
    visited = set()  # Keep track of visited nodes
    
    while open_set:
        current_node = min(open_set, key=lambda node: f_score[node])
        if current_node == goal_node:
            path = [current_node]
            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)
            path.reverse()
            return path
            
        open_set.remove(current_node)
        visited.add(current_node)
        
        for neighbor_str in net.getNode(current_node).getOutgoing():
            neighbor = neighbor_str.getID()
            neighbor_node = net.getEdge(neighbor).getToNode()
            

            tentative_g_score = g_score[current_node] + get_time(neighbor, time)
            print('edge: ',neighbor)
            print("g: ",get_time(neighbor,time) )
            
            if neighbor_node not in visited or tentative_g_score < g_score[neighbor_node]:
                neighbor_node_id = neighbor_node.getID()
                if neighbor_node_id not in visited:
                    came_from[neighbor_node_id] = current_node
                    g_score[neighbor_node_id] = tentative_g_score
                    f_score[neighbor_node_id] = tentative_g_score + heuristic(neighbor_node_id)
                    open_set.append(neighbor_node_id)
                    visited.add(neighbor_node_id)
                    
    return None
# find the shortest path using A* algorithm
shortest_path = a_star(start_node, goal_node)
print("Shortest path:", shortest_path)

# stop the simulation
traci.close()

