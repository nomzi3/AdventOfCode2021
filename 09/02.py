import pprint
#import sys
fileRead_list = []
with open("input_02.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        #print(line)
        fileRead_list.append(line)

pprint.pprint(fileRead_list)
#tempArray = []
twoD_Array = []
###create the 2d-array with ints
for line in fileRead_list:
    tempArray = []
    for digit in line:
        tempArray.append(int(digit))
    twoD_Array.append(tempArray)
###print the array
for i in range(0,len(twoD_Array)):
    string_test = ""
    for j in range(0,len(twoD_Array[i])):
        #print(twoD_Array[i][j])
        string_test += str(twoD_Array[i][j])
    print(string_test)
#print("size of array:" + str(sys.getsizeof(twoD_Array)))

###########################################
##check position x/y if adjacent to the edge
##Direction -> 'up','down','left','right'
#Return true/false
def check_ifAdjacent(list_to_check,x_pos,y_pos,direction):
    if direction == 'up':
        #print("up")
        if y_pos == 0:
            return True
        else:
            return False
    elif direction == 'down':
        #print("down")
        if y_pos == len(list_to_check)-1:
            return True
        else:
            return False
    elif direction == 'left':
        #print("left")
        if x_pos == 0:
            return True
        else:
            return False
    elif direction == 'right':
        #print("right")
        #if x_pos == len(twoD_Array[y_pos])-1:
        #if x_pos == list_to_check[y_pos][len(list_to_check[y_pos])-1]:
        if x_pos == len(list_to_check[y_pos])-1:
        #if x_pos == len(list_to_check[y_pos][len(list_to_check[x_pos]-1)]):
            return True
        else:
            return False
    else:
        print("Unable to fetch direction")
##Check if lower than UP
####Return True/False
def check_ifLowerThanUp(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos-1][x_pos]:
        return True
    else:
        return False
##Check if lower than DOWN
####Return True/False
def check_ifLowerThanDown(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos+1][x_pos]:
        return True
    else:
        return False
##Check if lower than LEFT
####Return True/False
def check_ifLowerThanLeft(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos][x_pos-1]:
        return True
    else:
        return False
##Check if lower than RIGHT
####Return True/False
def check_ifLowerThanRight(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos][x_pos+1]:
        return True
    else:
        return False

##Check if pos is a Lowpoint
###Return True/False
def check_ifLower(list_to_check,x_pos,y_pos):
    #print("<----------------------------------->")
    #print("X_PoS==>" + str(x_pos))
    #print("Y_Pos==>" + str(y_pos))
    lowerThanUp = False
    lowerThanDown = False
    lowerThanLeft = False
    lowerThanRight = False
    boolList = []
    if check_ifAdjacent(list_to_check,x_pos,y_pos,'up'):
        lowerThanUp = True
    else:
        lowerThanUp = check_ifLowerThanUp(list_to_check,x_pos,y_pos)
    if check_ifAdjacent(list_to_check,x_pos,y_pos,'down'):
        lowerThanDown = True
    else:
        lowerThanDown = check_ifLowerThanDown(list_to_check,x_pos,y_pos)
    if check_ifAdjacent(list_to_check,x_pos,y_pos,'left'):
        lowerThanLeft = True
    else:
        lowerThanLeft = check_ifLowerThanLeft(list_to_check,x_pos,y_pos)
    if check_ifAdjacent(list_to_check,x_pos,y_pos,'right'):
        lowerThanRight = True
    else:
        lowerThanRight = check_ifLowerThanRight(list_to_check,x_pos,y_pos)
    #print(lowerThanUp)
    #print(lowerThanDown)
    #print(lowerThanLeft)
    #print(lowerThanRight)
    #if lowerThanLeft and lowerThanRight and lowerThanUp and lowerThanRight == True:
     #   print("Tersting")
    boolList.append(lowerThanUp)
    boolList.append(lowerThanDown)
    boolList.append(lowerThanLeft)
    boolList.append(lowerThanRight)
    #print(sum(boolList))
    if(sum(boolList)) == 4:
        print("X_PoS==>" + str(x_pos))
        print("Y_Pos==>" + str(y_pos))
        return True
    else:
        return False
    #print("###############################")

#########################################
####Part 2###############################
##Check if cord contains 9 (high point)
###Return True/False
def check_ifCordContainsNine(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] == 9:
        return True
    else:
        return False

###Fetch adjacent cordinates, UP, DOWN, LEFT, RIGHT
##Returns - List of valid cords
def fetch_adjacentCordinates(list_to_check,x_pos,y_pos):
    return_list = []
    print("Fetching adjacent cords")
    if not check_ifAdjacent(list_to_check,x_pos,y_pos,'up'):
        print("Not1")
        cord_to_test = [x_pos,y_pos-1]
        print(cord_to_test)
        print("Checking Up-cord for value9...Value-->" + str(list_to_check[cord_to_test[1]][cord_to_test[0]]))
        if not check_ifCordContainsNine(list_to_check,cord_to_test[0],cord_to_test[1]):
            print("Valid Cord")
            return_list.append(cord_to_test)
    if not check_ifAdjacent(list_to_check,x_pos,y_pos,'down'):
        print("Not2")
        cord_to_test = [x_pos,y_pos+1]
        print(cord_to_test)
        print("Checking Down-cord for value9...Value-->" + str(list_to_check[cord_to_test[1]][cord_to_test[0]]))
        if not check_ifCordContainsNine(list_to_check,cord_to_test[0],cord_to_test[1]):
            print("Valid Cord")
            return_list.append(cord_to_test)
    if not check_ifAdjacent(list_to_check,x_pos,y_pos,'left'):
        print("Not3")
        cord_to_test = [x_pos-1,y_pos]
        print(cord_to_test)
        print("Checking Left-cord for value9...Value-->" + str(list_to_check[cord_to_test[1]][cord_to_test[0]]))
        if not check_ifCordContainsNine(list_to_check,cord_to_test[0],cord_to_test[1]):
            print("Valid Cord")
            return_list.append(cord_to_test)
    if not check_ifAdjacent(list_to_check,x_pos,y_pos,'right'):
        print("Not4")
        cord_to_test = [x_pos+1,y_pos]
        print(cord_to_test)
        print("Checking Down-cord for value9...Value-->" + str(list_to_check[cord_to_test[1]][cord_to_test[0]]))
        if not check_ifCordContainsNine(list_to_check,cord_to_test[0],cord_to_test[1]):
            print("Valid Cord")
            return_list.append(cord_to_test)
    return return_list
## Calculate the basin based on lowpoint: x/y pos
###Return - list of cords part of basin
def calculate_basin(full_list,x_pos,y_pos):
    basin_list = []
    basin_list.append([x_pos,y_pos])
    #iter_list = []
    #iter_list.append([x_pos,y_pos])
    #basin_list = iter_list[:]
    print("##############################")
    print("calculating basin from Cords:")
    print("x pos:" + str(x_pos))
    print("y pos:" + str(y_pos))
    print(basin_list)
    notDoneRunning = True

    while(notDoneRunning):
        newItemAdded = False
        iter_list = basin_list[:]
        for item in iter_list:
            return_list = fetch_adjacentCordinates(full_list,item[0],item[1])
            #print(return_list)
            for cord in return_list:
                if cord not in basin_list:
                    basin_list.append(cord)
                    print("Adding cord to basin list:")
                    print(cord)
                    newItemAdded = True
        if newItemAdded == False:
            notDoneRunning = False
    return basin_list

            
## Locates all basins - based on our low points
###Returns - list of all basins, and its cords.
def locate_basins(full_list,low_point_list):
    basins_list = []
    #iter_list = low_point_list[:]
    for item in low_point_list:
        return_list = calculate_basin(full_list,item[0],item[1])
        print("--------------------------")
        print("Return list")
        print(return_list)
        basins_list.append(return_list)
    return basins_list

def calculate_finalScore(list_of_basins):
    print("calculating final score:")
    length_list = []
    for item in list_of_basins:
        length = int(len(item))
        length_list.append(length)
    length_list.sort(reverse=True)
    print(length_list)
    final_score = 1
    for i in range(0,3):
        final_score *= length_list[i]
    print("Final score:" + str(final_score))
#########################################

low_value_list = []
for i in range(0,len(twoD_Array)):
    for j in range(0,len(twoD_Array[i])):
        isLower = check_ifLower(twoD_Array,j,i)
        if(isLower):
            positions = [j,i]
            low_value_list.append(positions)
print(low_value_list)
list_of_all_basins = locate_basins(twoD_Array,low_value_list)
#print(list_of_all_basins)
print("####################################################")
for item in list_of_all_basins:
    print(item)
    print("length:" + str(len(item)))
calculate_finalScore(list_of_all_basins)
#fetch_adjacentCordinates(twoD_Array,item[1],item)
#for item in low_value_list:
#    fetch_adjacentCordinates(twoD_Array,item[1],item[0])
"""
test1 = [1,0]
test2 = [9,0]
if test1 in low_value_list:
    print("testing1")
if test2 in low_value_list:
    print("testing2")
"""
"""
return_value = check_ifAdjacent(twoD_Array,0,0,"left")
print(return_value)
return_value = check_ifAdjacent(twoD_Array,9,0,"right")
print(return_value)
return_value = check_ifAdjacent(twoD_Array,0,0,"up")
print(return_value)
return_value = check_ifAdjacent(twoD_Array,0,4,"down")
print(return_value)
"""

