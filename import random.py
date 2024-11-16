import random
from collections import deque

height=5
width=5

start_node= (0,0)
x,y=start_node
goal_node=(height-1 , width-1)
moves=[(1,0) , (-1,0) , (0,1) , (0,-1)]
wall_proabability=0

def maze_generator(height , width , wall_probability):
    maze=[[ 'S' if(i,j)==start_node else
           'G' if(i,j)==goal_node else
            1 if random.random()<wall_probability else
            0 for j in range(width)] for i in range(height)]
    for row in maze:
      print(row)

    return maze , start_node , goal_node


#path finding using BFS

def BFS(maze , start_node , goal_node ):
    if(start_node==goal_node):
        return path
    
    else:
        queue=deque([(start_node , [start_node])])
        visited=set([start_node])  #set(path)

        while queue:
            current_position , path=queue.popleft()
            x,y=current_position
           # node=path(-1)
            if(current_position==goal_node):
                return path
            

           

            for move in moves:
                X,Y = x+move[0] , y+move[1]   
                new_position=(X,Y)

                if 0<=X<height and 0<=Y<width:
                     if new_position not in visited and (maze[X][Y] == 0 or maze[X][Y]== 'G'): 
                         queue.append((new_position , path+[new_position]))
                         visited.add(new_position)

        return None                


maze, start_node, goal_node = maze_generator(height, width, wall_proabability)
path = BFS(maze, start_node, goal_node)
if path:
    print (f"path from {start_node} to {goal_node} : {path}")
else:
    print("not found")
                 














