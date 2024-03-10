import copy 

# Variables
queue_structure = []
old_node = []

# Functions
# Movement Functions

def BlankTileLocation(matrix):
        for i in range(len(matrix)):
         for j in range(len(matrix)):
             if matrix[i][j] == 0:
                 x = i
                 y = j
                 zero_value = (x,y)
        return zero_value

def ActionMoveLeft(CurrentNode):
    
    NewNode = copy.deepcopy(CurrentNode)
    [i,j] = BlankTileLocation(CurrentNode)
    
    if j >0:
        
        j_left = j - 1
        numTile = CurrentNode[i][j_left]
        NewNode[i][j] = numTile
        NewNode[i][j_left] = 0
        
    return NewNode

def ActionMoveRight(CurrentNode):
   
    NewNode = copy.deepcopy(CurrentNode)
    [i,j] = BlankTileLocation(CurrentNode)
   
    if j <2:
       
        j_right = j + 1
        numTile = CurrentNode[i][j_right]
        NewNode[i][j] = numTile
        NewNode[i][j_right] = 0
        
    return NewNode

def ActionMoveUp(CurrentNode):
   
     NewNode = copy.deepcopy(CurrentNode)
     [i,j] = BlankTileLocation(CurrentNode)
     
     if i > 0:
         
         i_up = i - 1
         numTile = CurrentNode[i_up][j]
         NewNode[i][j] = numTile
         NewNode[i_up][j] = 0
         
     return NewNode

def ActionMoveDown(CurrentNode):
     
     NewNode = copy.deepcopy(CurrentNode)
     [i,j] = BlankTileLocation(CurrentNode)
     
     if i < 2:
         
         i_down = i + 1
         numTile = CurrentNode[i_down][j]
         NewNode[i][j] = numTile
         NewNode[i_down][j] = 0
         
     return NewNode

# Old Node fuction

def isold_node(node1):
	check = copy.deepcopy(node1)
	x = node_int(check)
	for i in range(len(old_node)):
		if x==old_node[i]:
			return True
		else:
			return False
        
# Conversion Function
def node_int(node):
	flat_array = sum(node, [])
	s = [str(i) for i in flat_array]
	integer_value = int("".join(s))
	return integer_value

# Initial and goal state

initial = [[1,4,7],[5,0,8],[2,3,6]]
goal = [[1,4,7 ],[2,5,8],[3,6,0]]

# Filling the queue data structure

queue_structure.append(initial)
old_node.append(node_int(initial))
    

# BFS

while (len(queue_structure)>0):
    done = 0
    node_i = queue_structure.pop(0)
    all_possible_values = [ActionMoveLeft(node_i), ActionMoveRight(node_i), ActionMoveUp(node_i), ActionMoveDown(node_i)]
    values = []
    print(all_possible_values)

    for j in range(len(all_possible_values)):
	    if (all_possible_values[j] != 0):
             values.append(all_possible_values[j])
		    


    for i in range(len(values)):
        if not isold_node(values[i]):
            if node_int(values[i]) == node_int(goal):
                final_matrix = values[i]
                old_node.append(node_int(final_matrix))
                done = 1
                break
            else:
                queue_structure.append(values[i])
                old_node.append(node_int(values[i]))

    if done == 1:
        break
    
# Output as a text file
output = open("C:/Users/nisar/Downloads/proj1_nisargkumar_upadhyay/Case 1 nodepath.txt","w")
output.write('\n'.join(str(x) for x in old_node))

