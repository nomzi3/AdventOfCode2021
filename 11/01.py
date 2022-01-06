##10x10 octopi's
##Numbers representing energy lvls
####if number greater than 9 - flash and reset nr to 0
##############
# step per round
###1. increase energy lvl by 1 for each number
### if any octi has energy above 9, flash
#####->flash increases energy of all 9 surrounding octi by 1
#####->any new octi going above 9, will flash again - repeating
### max 1 flash per octi, per round.
####once all done with the round,set energy lvl to 0 for all octi that flashed that round.
import pprint

###Load our input - store as 2-D array
#####return 2-D array
def load_inputListIntoTwoDArray(filename):
    fileRead_list = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            fileRead_list.append(line)
    return_Array = []
    for line in fileRead_list:
        tempArray = []
        for digit in line:
            tempArray.append(int(digit))
        return_Array.append(tempArray)
    return return_Array
###
###Check if cords are OOB
####Return True/False
def check_ifCordIsOOB(listToCheck,x_pos,y_pos):
    print("x-pos:" + str(x_pos))
    print("y-pos:" + str(y_pos))
    if y_pos < 0 or y_pos >= len(listToCheck):
        print("out of range===>" + str(y_pos))
        return True
    elif x_pos < 0 or x_pos >= len(listToCheck[y_pos]):
        print("out of range+++>" + str(x_pos))
        return True
    else:
        return False
    
###Generate our 9 cords to increase energy lvl
#####remove any cords OOB
##Return list of cords
def generate_energyCordsToIncrease(listTocheck,x_pos,y_pos):
    energyCordlist = []
    energyCordlist.append([x_pos-1,y_pos-1])
    energyCordlist.append([x_pos,y_pos-1])
    energyCordlist.append([x_pos+1,y_pos-1])
    energyCordlist.append([x_pos-1,y_pos])
    energyCordlist.append([x_pos+1,y_pos])
    energyCordlist.append([x_pos-1,y_pos+1])
    energyCordlist.append([x_pos,y_pos+1])
    energyCordlist.append([x_pos+1,y_pos+1])
    returnlist = []
    for item in energyCordlist:
        inBounds = check_ifCordIsOOB(listTocheck,item[0],item[1])
        if not inBounds:
            returnlist.append(item)
    return returnlist
###increases daily energy in the list
####return updated list
def increase_dailyEnergy(listToiterate):
    temp_list = listToiterate[:]
    #pprint.pprint(temp_list)
    for i in range(0,len(temp_list)):
        for j in range(0,len(temp_list[i])):
            temp_list[i][j] += 1

    return temp_list
##create and return a base-list of 0's - size of list entered
def create_baseList(listToCopy):
    temp_list = []
    for i in range(0,len(listToCopy)):
        part2_list = []
        for j in range(0,len(listToCopy[i])):
            part2_list.append(0)
            #temp_list[i][j] = 0
        temp_list.append(part2_list)
    return temp_list
##Check octi at limit
#####WORK IN PROGRESS
##If you find one, run generate energy cords
####append it to the temp-list
###set "still running" to True
####set the "blown" octi to X
#####continue
###Once iteration done - append temp list to list - reset temp-list
#####continue until no more "blown" octi appears and still running is set to False.

###return updated list.
def check_octiAtLimit(listToIterate):
    temp_list = create_baseList(listToIterate)
    for i in range(0,len(listToIterate)):
        for j in range(0,len(listToIterate[i])):
            if listToIterate[i][j] > 9:
                print("Found one")
###run day changer - handles game logic for updating the Day
#####return updated list
def run_dayCanger(listToIterate):
    print("###################")
    pprint.pprint(listToIterate)
    return_list = increase_dailyEnergy(listToIterate)
    check_octiAtLimit(listToIterate)
    pprint.pprint(return_list)
    print("@@@@@@@@@@@@@@@@@@@")
    return return_list

#########################################################################
twoD_Array = load_inputListIntoTwoDArray("input_01_test.txt")

daysToRun = 1
for i in range(0,daysToRun):
    return_list = run_dayCanger(twoD_Array)
    #pprint.pprint(return_list)


#temp_list = create_baseList(twoD_Array)
#print(temp_list)



#generate_energyCordsToIncrease(twoD_Array,0,0)
#generate_energyCordsToIncrease(twoD_Array,4,4)
#print(len(twoD_Array[0]))
#print(len(twoD_Array))