import sys

class State:
    def __init__(self, position, dirty_set, path):
        self.position = position #current position
        self.dirty_set = dirty_set #dirty cells left
        self.path = path #past path

    

EMPTY_CELL = "-"
BLKD_CELL = "#"
DIRTY_CELL = "*"
START_CELL = "@"

def read_world(fileName):
    temp_world_arr = []
    world_arr = []
    with open(fileName, "r") as file:
        for line in file:
            temp_world_arr.append(line.strip())
    cols = temp_world_arr[0]
    rows = temp_world_arr[1]
    world = temp_world_arr[2:]      
    
 
    for i in world:
        world_arr.append(list(i))
   
    return cols, rows, world_arr

def main():
    arg1 = sys.argv[1]
    fileName = sys.argv[2]
    print(arg1)
    print(fileName)

    cols, rows, world = read_world(fileName) #parsing through world file
    gen_nodes = 0
    exp_nodes = 0
    start_pos = None #starting pos
    dirty_pos = set() #locations of all dirt spots
    visited = set()

    stack = [State(start_pos, dirty_pos, [])]

    #getting positions of start and dirty cells
    for x, row in enumerate(world):
        for y, c in enumerate(row):
            if c == DIRTY_CELL:
                dirty_pos.add((x,y))

            elif c == START_CELL:
                start_pos = (x, y)
    
    while stack:
        exp_nodes += 1
        current = stack.pop()


        curr_pos = current.position
        x, y = curr_pos
        dirty_set = current.dirty_set
        path = current.path

        if curr_pos in visited: #check/updated visited
            continue
        else: 
            visited.add(curr_pos)

        if dirty_set is None: #done cleaning
            print(path)
            print(f"{gen_nodes} nodes generated")
            print(f"{exp_nodes} nodes expanded")
            return
        
        

        #CLEAN IF NEEDED


        if 0 <= y-1 < cols and world[y+1][x] != BLKD_CELL: 
            gen_node += 1
            path.append("N")
            stack.push(State((x, y+1), dirty_set, path))
        elif 0 <= y+1 < cols:
            gen_node += 1
            path.append("S")
            stack.push(State((x, y-1), dirty_set, path))
        elif 0 <= x-1 < rows:
            gen_node += 1
            path.append("W")
            stack.push(State((x-1, y), dirty_set, path))
        elif 0 <= x+1 < rows:
            gen_node += 1
            path.append("E")
            stack.push(State((x+1, y), dirty_set, path))
        





        north_move = (x, y+1)
        south_move = (x, y-1)
        west_move = (x-1, y)
        east_move = (x+1, y)





            



    print("in mainnn")
    print(world)
    if arg1 == "uniform-cost":
        print("hold")

    elif arg1 == "depth-first":
        print("hold")

    else:
        print("invalid algorithm type, please choose uniform-cost or depth-first")
        exit()

    read_world(fileName)

main()
