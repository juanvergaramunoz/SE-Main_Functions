
# coding: utf-8

# In[1]:

##############################
####### network CLASS ########
##############################
#
# DESCRIPTION:
#   This class permits inserting the cost related with connecting all possible edges from a network.
#     Then, there is an internal function ("minimize_cost") that returns the required edges to minimize the total cost of having all nodes connected to the same one network.
#   When inserting a node for the first time, an 'installation' cost can be provided. For example, imagine that you are about to install a water supply pipelne in a town in Africa. You can connect one house to the one of a neighbour (cost attached to the edge between those 2 nodes), or you could isolate that house and install a new water well in case it is too far away. The cost of 'installation' is exactly the cost of starting a new distribution point isolated from the current infrastructure.
#      We assume that at least ONE NODE WILL HAVE TO ASSUME the INSTALLATION COST

####### FUNCTIONS FOR THIS CLASS #######
#
# - __init__: Generates the dictionary that will sotre the nodes attached to each node
#              --->  self.dict[0] == ((node1,cost_0-1),(node2,cost_0-2),...)
#              --->  self.dict[node1] == ((0,cost_1-0),(node2,cost_1-2),...)
#              --->  self.dict[node2] == ((0,cost_2-0),(node1,cost_2-1),...)
#
# - insert_node: This function inserts new nodes to the network. They get initially connected to a non-existent node 0, that exists only to contemplate the cost of 'installation'
#
# - insert_edge: This function permits to insert edges from the network, as well as costs associated with each edge
#
# - minimize_cost: This function iterates to get the final total cost, and edges required
#

class network:
    #############################
    ### Time complexity: O(1) ###
    #############################
    def __init__(self):
        #nodes = number of total nodes
        
        #Array will store the edges of each node i
        self.dict = {}
    
    
    #############################
    ### Time complexity: O(1) ###
    #############################
    #INPUT: 1) Node name (accepts numbers)
    #       2) "Installation" cost (cost of isolating parts of the networks)
    def insert_node(self,node,cost):
        
        try:
            self.dict[0].append((node,cost))
        except:
            self.dict[0] = [(node,cost)]
        
        try:
            self.dict[node].append((0,cost))
        except:
            self.dict[node] = [(0,cost)]
        
        return
    
    
    #############################
    ### Time complexity: O(1) ###
    #############################
    #INPUT: 1) Tupple of two nodes that could be connected
    #       2) Cost of connecting those nodes directly
    #OUTPUT: Bool --> TRUE __ if insertion correct | FALSE __ if there is a problem during insertion
    def insert_edge(self,node_pair,cost):
        if node_pair[0] not in self.dict.keys():
            print("ERROR - Node",node_pair[0],"is non existent")
            return False
        if node_pair[1] not in self.dict.keys():
            print("ERROR - Node",node_pair[1],"is non existent")
            return False
        
        
        try:
            self.dict[node_pair[0]].append((node_pair[1],cost))
        except:
            self.dict[node_pair[0]] = [(node_pair[1],cost)]
        
        try:
            self.dict[node_pair[1]].append((node_pair[0],cost))
        except:
            self.dict[node_pair[1]] = [(node_pair[0],cost)]
        
        return True
    
    
    #############################
    ### Time complexity: O(1) ###
    #############################
    #OUTPUT: 1) Bool --> TRUE __ if insertion correct | FALSE __ if there is a problem during insertion
    #        2) Tupple of edges that are to be connected in the final installation
    #            - When a node is connected to "node 0", a new installation has to be started at that node
    def minimize_cost(self):
        
        n_nodes = len(self.dict.keys()) #Amount of total nodes
        tot_cost = 0                    #Total Cost
        count = 1                       #Amount of nodes visited (We start in one, so when the last is found we don't go into the loop again where no more nodes are available)
        visited = []                    #Places visited
        possible_paths = []             #Possible paths
        
        next_node = 0      #We start with the central node (the center -- represents the routering option)
        while count < n_nodes:
            visited.append(next_node)
            count += 1
            #print("\nINSERTING NODE",next_node,"in Visited ---- Count =",count)
            cost = float("inf")
            for elem in self.dict[next_node]:
                
                #print("FROM NODE",next_node,"WE GET TO ANALIZE NODE",elem[0])
                if elem[0] in visited:
                    #print("CONTINUE STATED 1")
                    continue
                
                if elem[0] < next_node:
                     path = (elem[0],next_node,elem[1])
                else:
                    path = (next_node,elem[0],elem[1])
                
                if path in possible_paths:
                    #print("CONTINUE STATED 2")
                    continue
                
                #print("----> POSSIBLE PATHS:",possible_paths)
                i = 0
                aux = i
                n = int(len(possible_paths))
                while i < n:
                    aux = (n-i)//2 + i
                    if possible_paths[aux][2] < path[2]:
                        if aux == i:
                            aux += 1
                        
                        i = aux
                    elif possible_paths[aux][2] > path[2]:
                        if aux == n:
                            aux -= 1
                        
                        n = aux
                    else:
                        break
                
                #print("------> NEW PATH:",path,"located at position",aux)
                possible_paths.insert(aux,path)
            
            j = 0
            for i in range(len(possible_paths)):
                if possible_paths[i+j][0] in visited and possible_paths[i+j][1] in visited:
                    possible_paths.pop(i+j)
                    j = j-1
            
            next_path = possible_paths.pop(0)
            
            #print("\n***** PATH ADDED is....",next_path)
            tot_cost += next_path[2]
            if next_path[0] not in visited:
                next_node = next_path[0]
            elif next_path[1] not in visited:
                next_node = next_path[1]
            else:
                #print("ERROR FOUND --- BOTH NODES ON NEW PATH ARE ALREADY ON NETWORK...")
                return 0
        
        
        return tot_cost

        

