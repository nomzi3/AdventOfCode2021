
fish_array = []
s_list = [0,0,0,0,0,0,0,0,0,0]

def sort_our_fishes(unsorted_list,sorted_list):
    
    for item in unsorted_list:
        sorted_list[item] += 1
    return sorted_list

with open("input_01_test.txt", "r") as f:
    line = f.read().splitlines()
    #print(line)

    line = line[0].split(",")
    #print(line)
    for l in line:
        fish_array.append(int(l))
print(fish_array)

s_list = sort_our_fishes(fish_array,s_list)

print(s_list)