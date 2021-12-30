fileRead_list = []
input_list = []
output_list = []
with open("input_01.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        #print(line)
        fileRead_list.append(line)

print(fileRead_list)

for item in fileRead_list:
    temp_Split = item.split("|")
    #print(temp_Split)
    temp_input = temp_Split[0].strip()
    temp_output = temp_Split[1].strip()
    input_list.append(temp_input)
    output_list.append(temp_output)

#print(input_list)
#print(output_list)
###################################################
###for output list only, count the nr of combinations of the "unique" numbers
###
# 1 -> 2
# 4 -> 4
# 7 -> 3
# 8 -> 7
total_count = 0
for item in output_list:
    temp_list = item.split(" ")
    #print(temp_list)
    for i in temp_list:
        if(len(i) == 2):
            print(str(i) + " possible nr 1")
            total_count += 1
        elif(len(i) == 4):
            print(str(i) + " possible nr 4")
            total_count += 1
        elif(len(i) == 3):
            print(str(i) + " possible nr 7")
            total_count += 1
        elif(len(i) == 7):
            print(str(i) + " possible nr 8")
            total_count += 1
print("Total count==>" + str(total_count))