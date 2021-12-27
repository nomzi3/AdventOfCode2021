###TODO
#def function to move ALL crabs into position X
####calculate distance required for all crabs - return
######def function to calculate position to move crabs to
####test each by calling move function, store result
###return -> lowest possible result


###FYI - this is a really stupid way of solving it, but hey, it works.
pos_list = []


with open("input_01.txt", "r") as f:
    i = f.readline()
    pos_list = i.split(",")
print(pos_list)

def moveCrabsIntoPositionCost(crab_list,targetPos):
    total_count = 0
    for item in crab_list:
        if int(item) < targetPos:
            difference = targetPos - int(item)
            total_count += difference
        else:
            difference = int(item) - targetPos
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


"""
total_count = 0
for i in pos_list:
    total_count += int(i)
print("Total:" + str(total_count))
print("Nr of items:" + str(len(pos_list)))
print("Median___>" + str(total_count / len(pos_list)))
"""
"""
total_count = len(pos_list)
print(total_count)
if(total_count % 2 == 0):
    print(pos_list[int(total_count/2)])
    print(pos_list[int(total_count/2)+1])
else:
    print("no")
"""