import copy


drawing_numbers = []
input_list = []
with open("input_01.txt", "r") as f:
    input_list = f.readlines()
    
##removes any whitespace from input array
def removeWhiteSpacesFromArray(the_list):
    new_array = []
    for item in the_list:
        if item != "":
            new_array.append(int(item))
    return new_array
##generates our boards, returns a dict
def generateBoards(list_to_check):
    board_number = 1
    increment_counter = 1
    newline_counter = 0
    return_dict = {}
    while(increment_counter < len(list_to_check)):
        next_entry = list_to_check[increment_counter].strip()
        if(next_entry == ''):
            newline_counter += 1
            if(newline_counter > 1):
                break
            print(newline_counter)
            increment_counter += 1
        elif(newline_counter == 1):
            #i = 5
            local_dict = {}
            for i in range(0,5):
                #print(list_to_check[increment_counter].strip())
                generated_row = list_to_check[increment_counter].strip()
                generated_row = generated_row.split(' ')
                #print(generated_row)
                #print("removing empty entries")
                cleaned_array = removeWhiteSpacesFromArray(generated_row)
                local_dict[i] = cleaned_array
                increment_counter += 1
            newline_counter = 0
            #print(local_dict)
            return_dict[board_number] = local_dict
            board_number += 1
    return return_dict

##returns true, or false if ANY matches are found
def removeDrawnNumbFromBoard(dict_to_check,drawn_number):
    match_found = False
    for i in range(1,len(dict_to_check.keys()) + 1):
        #print(dict_to_check[i])
        for y in range(0,len(dict_to_check[i].keys())):
         #   print(dict_to_check[i][y])
            for x in range(0,5):
                if(dict_to_check[i][y][x] == int(drawn_number)):
          #          print("Found a match")
                    dict_to_check[i][y][x] = "X"
                    match_found = True
            #if(dict_to_check[i][y] == int(drawn_number)):
             #   print("Found a match")
    #print(dict_to_check)
    #print("number of boards?")
    #print(len(dict_to_check.keys()))
    #print(drawn_number)
    return match_found
###if no winner, return 0 (no such board exists)
###else, return the winning board for the ROW
def checkIfWinner_Row(dict_to_check):
    winner_found = 0
    print(dict_to_check)
    for i in range(1,len(dict_to_check.keys()) + 1):
        print("number:" + str(i))
        for y in range(0,len(dict_to_check[i].keys())):
            for x in range(0,5):
                if(dict_to_check[i][y][x] == "X"):
                    #print(dict_to_check[i][y])
                    isWinner = checkRowForWinner(dict_to_check[i][y])
                    if(isWinner):
                        winner_found = i
                        return winner_found
    return winner_found
#check if the row contains only X
##if: return True
##else: return False
def checkRowForWinner(list_to_check):
    isWinner = 0
    for i in range(0,5):
        #print(list_to_check[i])
        if(list_to_check[i] == "X"):
            isWinner += 1
    if(isWinner == 5):
        return True
    else:
        return False
##Iterate through the dict, if it finds a X - iterate and see if a column winner is found
####returns 0 if no matches
####else, return the ID of the board that is the winner.
def checkIfWinner_Column(dict_to_check):
    winner_found = 0
    for i in range(1,len(dict_to_check.keys()) + 1):
        for y in range(0,len(dict_to_check[i].keys())):
            for x in range(0,5):
                if(dict_to_check[i][y][x] == "X"):
                    isWinner = checkColumnForWinner(dict_to_check,i,x)
                    if(isWinner):
                        winner_found = i
                        return winner_found
    return winner_found
##check if a column within the board contains a winner
###return True if 5 matches
###else, return False
def checkColumnForWinner(dict_to_check,board_id,X_position):
    isWinner = 0
    for i in range(0,5):
        if(dict_to_check[board_id][i][X_position] == "X"):
            isWinner += 1
    if(isWinner == 5):
        return True
    else:
        return False
    return False

##calculate the final score
###return winning score
def calculateScore(winning_board,finalNumber):
    winningScore = 0
    #print(winning_board)
    for i in range(0,len(winning_board.keys())):
        for x in range(0,5):
            if(winning_board[i][x] != "X"):
                winningScore += winning_board[i][x]
    winningScore *= int(finalNumber)
    return winningScore

##generate the draw list of drawn numbers
drawing_numbers = input_list[0].strip()
draw_list = drawing_numbers.split(',')
print(drawing_numbers)

###generate our boards from the input data
generated_board_dict = generateBoards(input_list)
#backup_board_dict = generated_board_dict
##make a deep copy of our original board
backup_board_dict = copy.deepcopy(generated_board_dict)

winner_not_yet_found = True


###Go through our draw numbers, until we find a winner
for number in draw_list:
    ##if match found, check if winner generated
    match_Found = removeDrawnNumbFromBoard(generated_board_dict,number)
    if(match_Found):
        winner_found_ROW_BoardID = checkIfWinner_Row(generated_board_dict)
        if(winner_found_ROW_BoardID == 0):
            print("no winner found for rows")
        else:
            print("Winner found - winning board:" + str(winner_found_ROW_BoardID))
            print(backup_board_dict[winner_found_ROW_BoardID])
            print("Final Score:" + str(calculateScore(generated_board_dict[winner_found_ROW_BoardID],number)))
            break
        
        winner_found_COLUMN_BoardID = checkIfWinner_Column(generated_board_dict)
        if(winner_found_COLUMN_BoardID == 0):
            print("no winner found for columns")
        else:
            print("winner found - winning board:" + str(winner_found_COLUMN_BoardID))
            print(backup_board_dict[winner_found_COLUMN_BoardID])
            print("Final Score:" + str(calculateScore(generated_board_dict[winner_found_COLUMN_BoardID],number)))
            break


###TODO:
# read file, split into functional bits.
####part1 - drawing numbers - Array
####part2 - gameboards - dict
######read from newline to newline
############if entry is completely empty (just a newline), read the next 5 lines as a gameboard. 
############if 2 newlines in a row (empty rows), exit input-reading.
###########################
####game logic:
######loop through the draw_numbers, until a winner is found (or list ends)
#########call func1: remove the drawn number from the board - replace with X
#########call func2: check if any winners. Split into row/column?
##################PROBLEM - CAN MULTIPLE BOARDS WIN AT THE SAME TIME, AND DO WE CHECK FOR IT?
#############if winner found, return and call "score-func".