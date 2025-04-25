import sys
import heapq

class State:
    def __init__(self, position, dirty_set, path, cost = None):
        self.position = position #current position
        self.dirty_set = dirty_set #dirty cells left
        self.path = path #past path
        self.cost = cost

    def __eq__(self, other):
        if self.position == other.position and self.dirty_set==other.dirty_set:
            return True
        return False
    
    def __hash__(self):
        return hash((self.position, frozenset(self.dirty_set)))
    
    def __lt__(self, other):
        return self.cost<other.cost



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
 

    #parse world file
    cols, rows, world = read_world(fileName) 
    cols = int(cols)
    rows = int(rows)


    gen_nodes = 0
    exp_nodes = 0
    start_pos = None #starting pos
    dirty_pos = set() #locations of all dirt spots


    #getting positions of start and dirty cells
    for x1, row in enumerate(world):
        for y1, c in enumerate(row):
            if c == DIRTY_CELL:
                dirty_pos.add((x1,y1))

            elif c == START_CELL:
                start_pos = (x1, y1)
    

    start_state = State(start_pos, dirty_pos, [])
    start_state_pq = State(start_pos, dirty_pos, [], 0)

    if arg1 == "depth-first": #dfs
        visited = set()
        stack = [start_state]
        
        
        while stack:
            current = stack.pop()
            curr_pos = current.position
            x = curr_pos[0]
            y = curr_pos[1]
            dirty_set = current.dirty_set
            path = current.path

            #check/update visited
            if current in visited: 
                continue
            else: 
                exp_nodes += 1
                visited.add(current)

            if len(dirty_set) == 0: #done cleaning
                for a in path:
                    print(a)
                print(f"{gen_nodes} nodes generated")
                print(f"{exp_nodes} nodes expanded")
                return
            

            #if dirty, clean and continue so next iteration will clean
            if curr_pos in dirty_set:
                gen_nodes += 1
                new_dirty_set = dirty_set.copy()
                new_dirty_set.remove(curr_pos)
                stack.append(State(curr_pos, new_dirty_set, path + ["V"]))
                continue


            #adding n, s, w, e moves
            if 0 <= x-1 < rows and world[x-1][y] != BLKD_CELL: 
                gen_nodes += 1
                stack.append(State((x-1, y), dirty_set, path + ["N"]))

            if 0 <= x+1 < rows and world[x+1][y] != BLKD_CELL:
                gen_nodes += 1
                stack.append(State((x+1, y), dirty_set, path + ["S"]))

            if 0 <= y-1 < cols and world[x][y-1] != BLKD_CELL:
                gen_nodes += 1
                stack.append(State((x, y-1), dirty_set, path + ["W"]))

            if 0 <= y+1 < cols and world[x][y+1] != BLKD_CELL:
                gen_nodes += 1
                stack.append(State((x, y+1), dirty_set, path + ["E"]))


    elif arg1 == "uniform-cost":
        
        visited = {} #dictionary with state and cost
        pq = []
        heapq.heappush(pq, (0, start_state_pq)) #starting state has 0 cost
      
        
        while pq:
            cost, current = heapq.heappop(pq)

            curr_pos = current.position
            x = curr_pos[0]
            y = curr_pos[1]
            dirty_set = current.dirty_set
            path = current.path

            if (current.position, frozenset(current.dirty_set)) in visited: #can't use state to check like in prev bc path will be diff
                #check if current path would be cheaper
                if cost < visited[(current.position, frozenset(current.dirty_set))]:
                    visited[(current.position, frozenset(current.dirty_set))] = cost
                else: continue
            
            else:
                exp_nodes += 1
                visited[(current.position, frozenset(current.dirty_set))] = cost

            if len(dirty_set) == 0: #done cleaning
                for a in path:
                    print(a)
                print(f"{gen_nodes} nodes generated")
                print(f"{exp_nodes} nodes expanded")
                return

            #if dirty, clean and continue so next iteration will clean
            if curr_pos in dirty_set:
                gen_nodes += 1
                new_dirty_set = dirty_set.copy()
                new_dirty_set.remove(curr_pos)
                heapq.heappush(pq, (0, State(curr_pos, new_dirty_set, path + ["V"], 0)))
                continue


            #adding n, s, w, e moves
            if 0 <= x-1 < rows and world[x-1][y] != BLKD_CELL: 
                gen_nodes += 1
                heapq.heappush(pq, (cost + 1, State((x-1, y), dirty_set, path + ["N"], cost+1)))

            if 0 <= x+1 < rows and world[x+1][y] != BLKD_CELL:
                gen_nodes += 1
                heapq.heappush(pq, (cost + 1, State((x+1, y), dirty_set, path + ["S"], cost+1)))

            if 0 <= y-1 < cols and world[x][y-1] != BLKD_CELL:
                gen_nodes += 1
                heapq.heappush(pq, (cost + 1, State((x, y-1), dirty_set, path + ["W"], cost+1)))
     
  
            if 0 <= y+1 < cols and world[x][y+1] != BLKD_CELL:
                gen_nodes += 1
                heapq.heappush(pq, (cost + 1, State((x, y+1), dirty_set, path + ["E"], cost+1)))


        



 




main()
