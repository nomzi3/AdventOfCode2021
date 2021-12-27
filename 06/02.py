import numpy as np

fish_array = []
new_fish_timer = 8
total_days_to_run = 18
with open("input_01_test.txt", "r") as f:
    line = f.read().splitlines()
    #print(line)

    line = line[0].split(",")
    #print(line)
    for l in line:
        fish_array.append(int(l))
    #
    # lines = f.read().splitlines()
    #for line in lines:
        #print(line)
#print(len(fish_array))
#print(fish_array)

#x = []
#for i in range(5):
  #  y = numpy.array([0, 1, 2, 3])
 #   x.append(y)

#x = numpy.array(x)

##TODO
####change the "full list" to use numpy
######any new fish, add them to a normal list, append them into the full list on a day to day basis.
def dayChanger(fish_list):
    new_fish_array = []
    #new_fish_array = np.empty(new_fish_array)
    for fish in fish_list:
        if(fish == 0):
            new_fish_array.append(int(new_fish_timer))
            fish = 7
        fish -= 1
    """
    for i in range(0,len(fish_list)):
        if(fish_list[i] == 0):
            new_fish_array.append(int(new_fish_timer))
            fish_list[i] = 7
        fish_list[i] -= 1
    """
    tempArray = []
    tempArray.append(fish_list)
    tempArray.append(new_fish_array)
    
    x = np.array(tempArray)
    #for newfish in new_fish_array:
     #   fish_list = np.append(fish_list, newfish)
        #print(fish_list[i])
    #return fish_list
    return x
def fish_breeder(initial_list,days_to_run):
    print("Initial state:", *initial_list,sep=',')
    day_counter = 1
    for i in range(day_counter,days_to_run+1):
        initial_list = dayChanger(initial_list)
        #print("Day " + str(i) + "->", *initial_list,sep=",")
        print("Day " + str(i) + "->" + str(len(initial_list)))
    return initial_list

nparray = np.array(fish_array)
#print(nparray)
#print(type(nparray))

updated_list = fish_breeder(nparray,total_days_to_run)
print("Final count===>" + str(len(updated_list)))
"""new_array = []
new_array = np.empty(new_array)
print(np.size(new_array))
print(type(new_array))
print(new_array)
test_value = 1
new_array = np.append(new_array, test_value)
print(np.size(new_array))
print(new_array)

print(new_array[0])"""
"""
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
###if you pass any numbers into np.array, it will convert into an array.
arr2 = np.array((1,2,3,4,5))
print(arr2)
"""