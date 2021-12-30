fileRead_list = []
input_list = []
output_list = []
with open("input_02_test1.txt", "r") as f:
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


##############################
possible_a_list = ['a','b','c','d','e','f','g']
possible_b_list = ['a','b','c','d','e','f','g']
possible_c_list = ['a','b','c','d','e','f','g']
possible_d_list = ['a','b','c','d','e','f','g']
possible_e_list = ['a','b','c','d','e','f','g']
possible_f_list = ['a','b','c','d','e','f','g']
possible_g_list = ['a','b','c','d','e','f','g']

for item in fileRead_list:
    temp_list = item.split(" ")
    for i in temp_list:
        t_list = list(i)
        print(t_list)
        for letter in t_list:
            print(letter)
            if letter in possible_f_list:
                possible_f_list.remove(letter)

print(possible_f_list)
        #if(len(i) == 5):
         #   print(i)