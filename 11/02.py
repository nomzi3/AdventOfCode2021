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
    #print("x-pos:" + str(x_pos))
    #print("y-pos:" + str(y_pos))
    if y_pos < 0 or y_pos >= len(listToCheck):
        #print("out of range===>" + str(y_pos))
        return True
    elif x_pos < 0 or x_pos >= len(listToCheck[y_pos]):
        #print("out of range+++>" + str(x_pos))
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
    temp_list = listToiterate.copy()
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
#####takes octi list - iterates until no more energy overloads available
###return updated list.
def check_octiAtLimit(listToIterate):
    blown_list = create_baseList(listToIterate)
    #run_again = False
    isRuning = True
    ###Run until no more flashes occur this round
    while isRuning:
        temp_list = create_baseList(listToIterate)
        
        run_again = False
        for y in range(0,len(listToIterate)):
            for x in range(0,len(listToIterate[y])):
                ###if energy lvl is above 9, but has yet to blow
                if listToIterate[y][x] > 9 and blown_list[y][x] != 'X':
                    #print("Found one")
                    run_again = True
                    energy_cords_to_run = generate_energyCordsToIncrease(listToIterate,x,y)
                    ###Add energy to all surrounding octi
                    for item in energy_cords_to_run:
                        temp_list[item[1]][item[0]] += 1
                    ##Keep track of blown octi with the blown_list
                    blown_list[y][x] = 'X'
        ###Add our energy from this round to the list
        for y in range(0,len(temp_list)):
            for x in range(0,len(temp_list[y])):
                listToIterate[y][x] += temp_list[y][x]
        ##if no active energy surges this round, exit and return
        if run_again != True:
            isRuning = False
    ###For all blown octi, set their energy lvl to 0
    for y in range(0,len(blown_list)):
        for x in range(0,len(blown_list)):
            if blown_list[y][x] == 'X':
                listToIterate[y][x] = 0
    return listToIterate
###run day changer - handles game logic for updating the Day
#####return updated list
def run_dayCanger(listToIterate):
    return_list = listToIterate.copy()
    
    #pprint.pprint(listToIterate)
    return_list = increase_dailyEnergy(return_list)
    #pprint.pprint(return_list)
    return_list = check_octiAtLimit(return_list)
    #pprint.pprint(return_list)
    
    #return_list = []
    return return_list
##Counts the energy flashes of the round
###Returns integer
def count_energyFlashes(listToIterate):
    total_flashes = 0
    for y in range(0,len(listToIterate)):
        for x in range(0,len(listToIterate)):
            if listToIterate[y][x] == 0:
                total_flashes += 1
    return total_flashes
#########################################################################
########################Part2############################################

twoD_Array = load_inputListIntoTwoDArray("input_01.txt")
total_flashes = 0
daysToRun = 100 
print("Prior to any steps")
pprint.pprint(twoD_Array)
##Basic loop - ran for DaysToRun during part 1

##Changes for part 2
synchronizedFlashStillSearching = True
dayCounter = 1
while synchronizedFlashStillSearching:
    print("Day==>" + str(dayCounter))
    return_list = run_dayCanger(twoD_Array)
    flashes_this_round = count_energyFlashes(return_list)
    if(flashes_this_round == 100):
        print("Synchronized flash this round")
        pprint.pprint(return_list)
        synchronizedFlashStillSearching = False
    dayCounter += 1
    twoD_Array = return_list.copy()



#temp_list = create_baseList(twoD_Array)
#print(temp_list)



#generate_energyCordsToIncrease(twoD_Array,0,0)
#generate_energyCordsToIncrease(twoD_Array,4,4)
#print(len(twoD_Array[0]))
#print(len(twoD_Array))