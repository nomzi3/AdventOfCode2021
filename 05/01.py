import pprint
cord_dict = {}

##TODO:
####2D array?
#####array[x][y]
#######dynamically allocated?
#######print out all locations inbetween the cords

###start by adding our input to a dict.
with open("input_01_test.txt", "r") as f:
    counter = 0
    lines = f.read().splitlines()
    for line in lines:
        split_line = line.split("->")
        temp_array = []
        for item in split_line:
            temp_array.append(item.strip())
        cord_dict[counter] = temp_array
        counter += 1
        #print(temp_array)
pprint.pprint(cord_dict)