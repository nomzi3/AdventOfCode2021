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
#####Calculate the given values - that cannot be mis-managed.
def calculate_nr_one(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 2):
            return_value = item
    return return_value
def calculate_nr_four(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 4):
            return_value = item
    return return_value
def calculate_nr_seven(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 7):
            return_value = item
    return return_value
def calculate_nr_eight(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 8):
            return_value = item
    return return_value
############################################################
##takes input - single_line string to check
#####+ the string containing the two values of "nr 1"
def calculate_nr_two(single_line,nr_one):
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 2):
            print(item)
def calculate_number_values(single_line):
    nr_1 = calculate_nr_one(single_line)
    nr_4 = calculate_nr_four(single_line)
    nr_7 = calculate_nr_seven(single_line)
    nr_8 = calculate_nr_eight(single_line)
    
for item in fileRead_list:
    #calculate_nr_one(item)
    calculate_number_values(item)
"""
possible_a_list = ['a','b','c','d','e','f','g']
possible_b_list = ['a','b','c','d','e','f','g']
possible_c_list = ['a','b','c','d','e','f','g']
possible_d_list = ['a','b','c','d','e','f','g']
possible_e_list = ['a','b','c','d','e','f','g']
possible_f_list = ['a','b','c','d','e','f','g']
possible_g_list = ['a','b','c','d','e','f','g']
"""
"""
five_letter_words = []
six_letter_words = []
#full list
for item in fileRead_list:
    temp_list = item.split(" ")
    #go through words in the single line
    for i in temp_list:
        t_list = list(i)
        #print(t_list)
        #individual letters of words
        if(len(i) == 5):
            five_letter_words.append(i)
        elif(len(i) == 6):
            six_letter_words.append(i)
        #for letter in t_list:
         #   print(letter)
          #  if letter in possible_f_list:
           #     possible_f_list.remove(letter)

#print(possible_f_list)
        #if(len(i) == 5):
         #   print(i)
print(five_letter_words)
sorted_five_letter_words = []
for word in five_letter_words:
    #print(word)
    temp_word = list(word)
    #print(temp_word)
    temp_word.sort()
    #print(temp_word)
    temp_word = ''.join(temp_word)
    print(temp_word)
    sorted_five_letter_words.append(temp_word)

print(five_letter_words)
print(sorted_five_letter_words)
#print(six_letter_words)
"""