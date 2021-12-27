
fish_array = []
new_fish_timer = 8
total_days_to_run = 80
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
def dayChanger(fish_list):
    new_fish_array = []
    for i in range(0,len(fish_list)):
        if(fish_list[i] == 0):
            new_fish_array.append(int(new_fish_timer))
            fish_list[i] = 7
        fish_list[i] -= 1
    for newfish in new_fish_array:
        fish_list.append(newfish)
        #print(fish_list[i])
    return fish_list
def fish_breeder(initial_list,days_to_run):
    print("Initial state:", *initial_list,sep=',')
    day_counter = 1
    for i in range(day_counter,days_to_run+1):
        initial_list = dayChanger(initial_list)
        #print("Day " + str(i) + "->", *initial_list,sep=",")
        print("Day " + str(i) + "->" + str(len(initial_list)))
    return initial_list

updated_list = fish_breeder(fish_array,total_days_to_run)
print("Final count===>" + str(len(updated_list)))
