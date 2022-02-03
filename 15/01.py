import pprint


def load_inputAndSplitLineIntoTwoDArray(filename):
    """Load our input file 
    - Return 2D-list [y][x] format"""
    fileRead_list = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            fileRead_list.append(line)
    return_Array = []
    for line in fileRead_list:
        #split_line = line.split("-")
        split_line = list(line)
        return_Array.append(split_line)
    return return_Array
def generate_new_pos(current_pos):
    """Generate new pos, from current pos
    - Returns list of possible positions"""
    current_x = current_pos[1]
    current_y = current_pos[0]
    print("Current Pos:")
    print(current_pos)
    pos1 = [current_y-1,current_x]
    pos2 = [current_y+1,current_x]
    pos3 = [current_y,current_x-1]
    pos4 = [current_y,current_x+1]
    return_array = [pos1,pos2,pos3,pos4]
    return return_array
def check_if_move_isLegal(board,new_positions):
    print("temp")
#loads input into 2D-list
## board_list[y][x] to fetch value of cordinates
board_list = load_inputAndSplitLineIntoTwoDArray("input_01_test.txt")
pprint.pprint(board_list)

generated_list = generate_new_pos([0,0])

print(generated_list)


