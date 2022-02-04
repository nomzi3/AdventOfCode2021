import pprint
import copy

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
    #print("Current Pos:")
    #print(current_pos)
    pos1 = [current_y-1,current_x]
    pos2 = [current_y+1,current_x]
    pos3 = [current_y,current_x-1]
    pos4 = [current_y,current_x+1]
    return_array = [pos1,pos2,pos3,pos4]
    return return_array
def check_if_move_isLegal(board,new_positions):
    """check if generated moves are legal
    - Return list of legal moves"""
    #print("Checking positions")
    #print(new_positions)
    return_list = []
    for new_pos in new_positions:
        #print(new_pos)
        #if new_pos[0] < 0 or new_pos[0] >= len(board) and new_pos[1] < 0 or new_pos[1] >= len(board[0]):
         #   return_list.append(new_pos)
        if new_pos[0] < 0 or new_pos[0] >= len(board):
            pass
            #print(f"{new_pos} Out of Y range")
        elif new_pos[1] < 0 or new_pos[1] >= len(board[0]):
            pass
            #print(f"{new_pos} Out of X range")
        else:
            return_list.append(new_pos)
    #print("Legal moves")
    #print(return_list)
    return return_list



#loads input into 2D-list
## board_list[y][x] to fetch value of cordinates
board_list = load_inputAndSplitLineIntoTwoDArray("input_01_test.txt")
pprint.pprint(board_list)


#generated_positions = generate_new_pos([0,0])
#legal_moves = check_if_move_isLegal(board_list,generated_positions)
#print(legal_moves)

finished_runs = []
isLoopRunning = True
backlog = [[[0,0]]]
counter = 0
finish_cords = [len(board_list)-1,len(board_list[0])-1]
#print(finish_cords)
while isLoopRunning:
    print(f'backlog_length: {len(backlog)}')
    #pprint.pprint(backlog)
    runningLog = []
    runningLog = copy.deepcopy(backlog)
    backlog.clear()

    for path in runningLog:
        last_pos = path[-1]
        possible_positions = generate_new_pos(last_pos)
        #print(possible_positions)
        legal_moves = check_if_move_isLegal(board_list,possible_positions)
        #print(legal_moves)
        
        
        
        for new_pos in legal_moves:
            if new_pos not in path:
                new_path = copy.deepcopy(path)
                new_path.append(new_pos)
                if new_path[-1] == finish_cords:
                    finished_runs.append(new_path)
                    isLoopRunning = False
                else:
                    backlog.append(new_path)
        
    if len(backlog) == 0 or counter >= 50:
        isLoopRunning = False
    else:
        counter += 1
        print(counter)

pprint.pprint(finished_runs)