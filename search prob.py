class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the graph
        self.graph = {}

#adding one node at a time to make a cycle or tree
    def add_node(self, node):
         if node not in self.graph:
             self.graph[node]=[]
            
#adding edge to connect all the nodes together
    def add_edge(self, node1, node2):
        if node1 and node2 not in self.graph:
            return None
        
        else:
            self.graph[node1].append(node2)   #node1 -> node2


#finding the path using checks and an iterative loop
    def find_path(self , start_node , end_node , path=[]):
        path=path+start_node
        if start_node==end_node:
            return path
        


        if start_node not in self.graph:
            return None

 #within the main function we create an object of the class 
if __name__ == "__main__":
    g = Graph()


#here we defined all the nodes that the cycle or tree has
nodes = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']
#using the for loop we are adding nodes 
for node in nodes:
    g.add_node(node)

#here we connect all the nodes , two nodes at a time 
g.add_edge('A' , 'B')    
g.add_edge('A' , 'C')    
g.add_edge('B' , 'D')    
g.add_edge('C' , 'E')    
g.add_edge('D' , 'E')    
g.add_edge('D' , 'F')    
g.add_edge('E' , 'F')

#defined the interpreter about the start and end node
start_node = 'A'
end_node = 'F'
#added the current path to a variable called "path"
path = g.find_path(start_node , end_node)
#printing the final path we gained
print(f"path from { start_node} to {end_node} : {path}")



#  A -> C
#  |    |
#  |    v
#  |    E--
#  v    |  |
#       |  v
#  B - >D->F 
  




