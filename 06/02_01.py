###why overwork your computer to solve the problem, when you can simply add the fishes together?

new_fish_timer = 8
fish_array = []
s_list = [0,0,0,0,0,0,0,0,0,0]
total_days_to_run = 256
#sort the input-fishes, and count them.
def sort_our_fishes(unsorted_list,sorted_list):
    
    for item in unsorted_list:
        sorted_list[item] += 1
    return sorted_list

with open("input_01.txt", "r") as f:
    line = f.read().splitlines()
    #print(line)

    line = line[0].split(",")
    #print(line)
    for l in line:
        fish_array.append(int(l))
##Change the day - update the list, and add newly hatched fishes.
###returns updated list
def dayChanger(fish_list):
    temp_fish_list = [0,0,0,0,0,0,0,0,0,0]
    for i in range(1,9):
        temp_fish_list[i-1] += fish_list[i]
    temp_fish_list[6] += fish_list[0]
    temp_fish_list[8] += fish_list[0]
    return temp_fish_list

###Breed fishes, for X amount of days
##prints the day-changes
####returns the full list.
def fish_breeder(initial_list,days_to_run):
    print("Initial state:", *initial_list,sep=',')
    day_counter = 1
    total_counter = 0
    for i in range(day_counter,days_to_run+1):
        initial_list = dayChanger(initial_list)
        for item in initial_list:
            total_counter += int(item)
        print("Day " + str(i) + "->" + str(total_counter))
        total_counter = 0
    return initial_list

s_list = sort_our_fishes(fish_array,s_list)

updated_list = fish_breeder(s_list,total_days_to_run)
total_fishes = 0
for item in updated_list:
    total_fishes += int(item)

print("Final count===>" + str(total_fishes))
