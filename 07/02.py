pos_list = []


with open("input_02.txt", "r") as f:
    i = f.readline()
    pos_list = i.split(",")
print(pos_list)
##accumulatedc cost
####1st step - cost 1
####2nd step - cost 2
####3rd step - cost 3
def stepCost(stepsRequired):
    accumulated_cost = 0
    #stepNr = 1
    for i in range(1,stepsRequired+1):
        accumulated_cost += int(i)
    return accumulated_cost

def moveCrabsIntoPositionCost(crab_list,targetPos):
    total_count = 0
    for item in crab_list:
        
        if int(item) < targetPos:
            difference = targetPos - int(item)
            difference = stepCost(difference)
            total_count += difference
        else:
            difference = int(item) - targetPos
            difference = stepCost(difference)
            total_count += difference
    return total_count

def calculatePosForCrabs(crab_list):
    temp_list = []
    result_list = []
    for item in crab_list:
        temp_pos = int(item)
        temp_list.append(temp_pos)
    temp_list.sort()
    for item in temp_list:
        print(item)
    lowest_range = int(min(temp_list))
    highest_range = int(max(temp_list))
    #print("lowest nr-->", str(min(temp_list)))
    #print("highest nr->", str(max(temp_list)))
    for i in range(lowest_range,highest_range+1):
        movement_cost = moveCrabsIntoPositionCost(temp_list,i)
        print("testing->" + str(i) + ":=>" + str(movement_cost))
        result_list.append(movement_cost)
    return result_list


#movement_cost = moveCrabsIntoPositionCost(pos_list,)
#print(movement_cost)
full_list = calculatePosForCrabs(pos_list)

full_list.sort()
print("Lowest cost=>" + str(full_list[0]))