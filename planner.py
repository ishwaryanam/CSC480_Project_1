import sys



EMPTY_CELL = "-"
BLKD_CELL = "#"
DIRTY_CELL = "*"
START_LOC = "@"

def read_world(fileName):
    temp_world_arr = []
    with open(fileName, "r") as file:
        for line in file:
            temp_world_arr.append(line.strip())
    cols = temp_world_arr[0]
    rows = temp_world_arr[1]
    world = temp_world_arr[2:]      
    print(cols)

    return cols, rows, world

def main():
    arg1 = sys.argv[1]
    fileName = sys.argv[2]
    print(arg1)
    print(fileName)

    cols, rows, world = read_world(fileName)

    if arg1 == "uniform-cost":
        print("hold")

    elif arg1 == "depth-first":
        print("hold")

    else:
        print("invalid algorithm type, please choose uniform-cost or depth-first")
        exit()

    read_world(fileName)

main()
