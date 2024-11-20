import time
width = 15
#maze with multiple solutions
maze = [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "S", " ", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"],
    ["X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"],
    ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", "X", "X", "X", "X"],
    ["X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X"],
    ["X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", " ", "X", "X", "X"],
    ["X", " ", " ", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"],
    ["X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X", " ", "X"],
    ["X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", " ", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"],
    ["X", "X", "X", "X", "X", " ", "X", "X", "X", "X", "X", "X", "X", "E", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
]

def print_board(board):
    for row in board:
        print(" ".join(row))

testMaze = [
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "S", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", "X", "X", "X", "X", " ", " ", " ", " ", "X"],
    ["X", " ", " ", " ", "X", " ", " ", " ", " ", "X"],
    ["X", " ", " ", " ", "X", " ", " ", " ", " ", "X"],
    ["X", " ", " ", " ", "X", " ", " ", " ", " ", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", " ", "X"],
    ["X", " ", "X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", " ", " ", " ", " ", " ", " ", " ", "E", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
]

print_board(testMaze)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE= (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
MAGENTA = (255, 0, 255)

## HEURISTICS ##
#
# The shortest path
# The the distance from the start plus the distance to the end

startNode = (1, 1)
endNode = (8, 8)

currentNode = (1, 1) #current node is a variable that will change
checkedNodes = list() 
openNodes = list() #The nodes that haven't been visited but have been discovered
neighbours = list()

def findneighbours(pos): #node should be a tuple
    neighbours = list()
    neighbours.append((pos[0]-1, pos[1]))
    neighbours.append((pos[0]+1, pos[1]))
    neighbours.append((pos[0], pos[1]-1))
    neighbours.append((pos[0], pos[1]+1))
    return neighbours
    
#node value is used to determine if it's worth visiting that node
def nodeValue(node, start): #the cost of going to that node
    (x1, y1) = node
    (x2, y2) = start
    return abs(x1 - x2) + abs(y1 - y2) #the estimated cost of going to the end

def heuristic(node, end): 
    (x1, y1) = node
    (x2, y2) = end
    return abs(x1 - x2) + abs(y1 - y2)
    

def find_priority_node():
    #priority contains the total cost of the cell and the location of said cell
    priority = openNodes[0]
    #print("Priority", priority)
    #print("Line 98 type", type(openNodes[0][0]))
    for i in range(len(openNodes)):
        if openNodes[i][0] <= priority[0]:
            priority = openNodes[i] ############################
            #print("line 101 type:", type(openNodes[i][1]))
    checkedNodes.append([priority[1], currentNode])
    openNodes.remove(priority)
    return priority[1]
    
#finding the way to the end
#in checkedNodes, each item will include the node that was checked as well as the node that was previous to it.
#####################################################################################
while not "E" in checkedNodes:
    #finding free spaces 
    #print("line 111:", type(currentNode))
    print("openNodes", openNodes)
    neighbours = findneighbours(currentNode)
    #print(checkedNodes)
    
    #finds the four neighbours
    for i in range(4):
        (row, col) = (neighbours[i][0], neighbours[i][1])
        if testMaze[row][col] == " ":
            totalCost = nodeValue(currentNode, startNode) + heuristic(currentNode, endNode)
            openNodes.append([totalCost, (row, col)]) #every item in openNodes is a list with an integer and a tuple
            testMaze[row][col] = "O"
        elif testMaze[row][col] == "E":
            checkedNodes.append(testMaze[row][col], currentNode)
            break
    ############################
    priority = list()
    if not (" ") in neighbours:
        pass
        #find another free spot on the priority
    
    currentNode = find_priority_node()
    
    print_board(testMaze)
    
    time.sleep(0.25) 
    
    