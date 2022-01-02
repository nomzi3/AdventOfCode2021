import pprint
#import sys
fileRead_list = []
with open("input_01.txt", "r") as f:
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
##check position x/y if adjacent
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
def check_ifLowerThanUp(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos-1][x_pos]:
        return True
    else:
        return False
def check_ifLowerThanDown(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos+1][x_pos]:
        return True
    else:
        return False
def check_ifLowerThanLeft(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos][x_pos-1]:
        return True
    else:
        return False
def check_ifLowerThanRight(list_to_check,x_pos,y_pos):
    if list_to_check[y_pos][x_pos] < list_to_check[y_pos][x_pos+1]:
        return True
    else:
        return False
def check_ifLower(list_to_check,x_pos,y_pos):
    print("<----------------------------------->")
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
riskLevel = 0
for i in range(0,len(twoD_Array)):
    for j in range(0,len(twoD_Array[i])):
        isLower = check_ifLower(twoD_Array,j,i)
        if(isLower):
            riskLevel += twoD_Array[i][j] + 1
        #print(twoD_Array[i][j])
        #string_test += str(twoD_Array[i][j])
    #print(string_test)    
print(riskLevel)
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

