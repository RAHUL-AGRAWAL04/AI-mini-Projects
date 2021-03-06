# -*- coding: utf-8 -*-
"""3_WATER_JUG_USING_BFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pKWdXPYoJ2o9K4v_jN6_976X1GGYd0nw
"""

import time
jug1 = 8
jug2 = 5
jug3 = 3

def pour_water_from_jug1_to_jug2(capacity):
    current_jug1 = capacity[0]
    current_jug2 = capacity[1]
    current_jug3 = capacity[2]
    available_capacity = jug2-current_jug2
    while True:
      if (current_jug1<=0 or current_jug2>=jug2) or available_capacity<=0:
          break
      else:
        available_capacity -= 1
        current_jug1 -= 1
        current_jug2 += 1
    return [current_jug1,current_jug2, current_jug3]    

# driver code:
new_states = pour_water_from_jug1_to_jug2([8,0,0])
print(new_states)

def pour_water_from_jug1_to_jug3(capacity):
    current_jug1 = capacity[0]
    current_jug2 = capacity[1]
    current_jug3 = capacity[2]
    available_capacity = jug3-current_jug3
    while True:
      if (current_jug1<=0 or current_jug3>=jug3) or available_capacity<=0:
          break
      else:
        available_capacity -= 1
        current_jug1 -= 1
        current_jug3 += 1
    return [current_jug1,current_jug2,current_jug3]    
       
# driver code:
new_states = pour_water_from_jug1_to_jug3([8,0,0])
print(new_states)

def pour_water_from_jug2_to_jug1(capacity):
    current_jug1 = capacity[0]
    current_jug2 = capacity[1]
    current_jug3 = capacity[2]
    available_capacity = jug1-current_jug1
    while True:
      if (current_jug2<=0 or current_jug1>=jug1) or available_capacity<=0:
          break
      else:
        available_capacity -= 1
        current_jug2 -= 1
        current_jug1 += 1
    return [current_jug1,current_jug2,current_jug3]     
      
# driver code:
new_states = pour_water_from_jug2_to_jug1([2,3,3])
print(new_states)

def pour_water_from_jug2_to_jug3(capacity):
    current_jug1 = capacity[0]
    current_jug2 = capacity[1]
    current_jug3 = capacity[2]
    available_capacity = jug3-current_jug3
    while True:
      if (current_jug2<=0 or current_jug3>=jug3) or available_capacity<=0:
          break
      else:
        available_capacity -= 1
        current_jug2 -= 1
        current_jug3 += 1
    return [current_jug1,current_jug2, current_jug3]    
       
# driver code:
new_states = pour_water_from_jug2_to_jug3([3,5,0])
print(new_states)

def pour_water_from_jug3_to_jug2(capacity):
    current_jug1 = capacity[0]
    current_jug2 = capacity[1]
    current_jug3 = capacity[2]
    available_capacity = jug2-current_jug2
    while True:
      if (current_jug3<=0 or current_jug2>=jug2) or available_capacity<=0:
          break
      else:
        available_capacity -= 1
        current_jug3 -= 1
        current_jug2 += 1
    return [current_jug1,current_jug2,current_jug3]     
      
# driver code:
new_states = pour_water_from_jug3_to_jug2([5,0,3])
print(new_states)

def pour_water_from_jug3_to_jug1(capacity):
    current_jug1 = capacity[0]
    current_jug2 = capacity[1]
    current_jug3 = capacity[2]
    available_capacity = jug1-current_jug1
    while True:
      if (current_jug3<=0 or current_jug1>=jug1) or available_capacity<=0:
          break
      else:
        available_capacity -= 1
        current_jug3 -= 1
        current_jug1 += 1
    return [current_jug1,current_jug2, current_jug3]     
      
# driver code:
new_states = pour_water_from_jug3_to_jug1([0,5,3])
print(new_states)

def find_path(parents):
    path=[]
    path.append(parents[len(parents)-1][1])
    path.append(parents[len(parents)-1][0])
    x=parents[len(parents)-1][0]
    for parent in range(len(parents)-2,-1,-1):
        if parents[parent][1]==x:
            x=parents[parent][0]
            path.append(x)
    return path
    
#drivers code
x=find_path([['E', 'A'], ['E', 'B'], ['E', 'D'], ['E', 'H'], ['A', 'C'], ['H', 'F'], ['C', 'G']])
print(x)

def bfs_goal_search(start,goal):
    explored = []
    queue = [start]
    neighbour=[]
    parents=[]
    if(start==goal):
        return(print("start is goal"))

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)

        neighbour = pour_water_from_jug1_to_jug2(node)
        if neighbour != None:
            if neighbour not in queue and neighbour not in explored :
                queue.append(neighbour)
                parents.append([node,neighbour])
            if neighbour == goal:
                return find_path(parents)
                return neighbour
                    
        neighbour = pour_water_from_jug1_to_jug3(node)
        if neighbour != None:
            if neighbour not in queue and neighbour not in explored :
                queue.append(neighbour)
                parents.append([node,neighbour])
            if neighbour == goal:
                return find_path(parents)
                return neighbour
        
        neighbour = pour_water_from_jug2_to_jug1(node)
        if neighbour != None:
            if neighbour not in queue and neighbour not in explored :
                queue.append(neighbour)
                parents.append([node,neighbour])
            if neighbour == goal:
                return find_path(parents)
                return neighbour
            
        neighbour = pour_water_from_jug2_to_jug3(node)
        if neighbour != None:
            if neighbour not in queue and neighbour not in explored :
                queue.append(neighbour)
                parents.append([node,neighbour])
            if neighbour == goal:
                return find_path(parents)
                return neighbour

        neighbour = pour_water_from_jug3_to_jug1(node)
        if neighbour != None:
            if neighbour not in queue and neighbour not in explored :
                queue.append(neighbour)
                parents.append([node,neighbour])
            if neighbour == goal:
                return find_path(parents)
                return neighbour

        neighbour = pour_water_from_jug3_to_jug2(node)
        if neighbour != None:
            if neighbour not in queue and neighbour not in explored :
                queue.append(neighbour)
                parents.append([node,neighbour])
            if neighbour == goal:
                return find_path(parents)
                return neighbour
            
     
# driver code      
start = [8,0,0]
goal = [4,4,0]
print('Solution of 3 water jug problem with jug1=8, jug2=5, jug3=3 as capacity of 3 jugs')
print('=================================================================================')
solutions = bfs_goal_search(start,goal)
print('Initial State(step- 1) ==>',solutions[-1])
for index in range(2,len(solutions)):
  print('Step-',index,'==>',solutions[-index])
print('Goal State(step-',len(solutions),') ==>',solutions[0])