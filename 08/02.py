####Stupid Version - only works for example 1- Fails on the rest as in some examples there will be
###missing digits, and as such calculations wont work.

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

##Input unsorted word - 
# Returns - word sorted alphabetically
def sort_single_word(unsorted_word):
    list_word = list(unsorted_word)
    list_word.sort()
    sorted_word = ''.join(list_word)
    return sorted_word
###LBL => letter by letter
def match_subword_in_word_LBL(subword,word):
    # len length of subword
    ####letter by letter - check if part of word
    ######if matches == length, return true
    subword_list = list(subword)
    subword_length = len(subword_list)
    matches = 0
    for item in subword_list:
        if item in word:
            matches += 1
    if subword_length == matches:
        return True
    else:
        return False
##fetches all strings matching length X
####Returns - sorted list
def fetch_strings_of_length(single_line,string_length):
    unsorted_list_of_words = []
    sorted_list_of_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == string_length):
            unsorted_list_of_words.append(item)
    for item in unsorted_list_of_words:
        sorted_list_of_words.append(sort_single_word(item))
    return sorted_list_of_words
###get letter missing from word that does not exist in subword
def get_missing_letter_in_subword(subword,word):
    word_list = list(word)
    match_found = False
    for item in word_list:
        if item not in subword:
            match_found = True
            return item
    if(match_found == False):
        return None

def get_matching_number(item_to_check,calculated_numbers):
    counter = 0
    for item in calculated_numbers:
        if item_to_check in item and len(item_to_check) == len(item):
            print("Found match for:" + item_to_check + " in===>" + item)
            return counter
        else:
            counter += 1
    return None  
##############################
#####Calculate the given values - that cannot be anything else.
##Always return Sorted words
def calculate_nr_one(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 2):
            return_value = item
    return sort_single_word(return_value)
def calculate_nr_four(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 4):
            return_value = item
    return sort_single_word(return_value)
def calculate_nr_seven(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 3):
            return_value = item
    return sort_single_word(return_value)
def calculate_nr_eight(single_line):
    return_value = ""
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 7):
            return_value = item
    return sort_single_word(return_value)
############################################################
##takes input - single_line string to check
#####+ the string containing the two values of "nr 1"
def calculate_nr_two(single_line,nr_one):
    five_letter_words = []
    sorted_five_letter_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 5):
            five_letter_words.append(item)
    print(five_letter_words)
def calculate_nr_three(single_line,nr_one):
    ##calculated, as only 1 of the nr 5:s contains both the values contained in nr_one.
    print("Calculating nr 3")
    five_letter_words = []
    sorted_five_letter_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 5):
            five_letter_words.append(item)
    print(five_letter_words)
    for item in five_letter_words:
        sorted_five_letter_words.append(sort_single_word(item))
    print("Sorted words")
    print(sorted_five_letter_words)
    found_item = False
    for item in sorted_five_letter_words:
        if nr_one in item:
            #print("Found one===>" + item)
            found_item = True
            return item
    if(found_item == False):
        print("Error in code - unable to calculate NR 3") 
def calculate_nr_nine(single_line,nr_three):
    print("Calculating nr 9")
    six_letter_words = []
    sorted_six_letter_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 6):
            six_letter_words.append(item)
    print(six_letter_words)
    for item in six_letter_words:
        sorted_six_letter_words.append(sort_single_word(item))
    print("Sorted words")
    print(sorted_six_letter_words)
    found_item = False
    for item in sorted_six_letter_words:
        return_bool = match_subword_in_word_LBL(nr_three,item)
        if(return_bool):
            found_item = True
            return item
    if(found_item == False):
        print("Error in code - unable to calculate nr 3")
def calculate_nr_zero(single_line,nr_nine,nr_seven):
    print("Calculating nr 0")
    six_letter_words = []
    sorted_six_letter_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 6):
            six_letter_words.append(item)
    print(six_letter_words)
    for item in six_letter_words:
        sorted_six_letter_words.append(sort_single_word(item))
    print("Sorted words")
    print(sorted_six_letter_words)

    while nr_nine in sorted_six_letter_words: sorted_six_letter_words.remove(nr_nine)
    print(sorted_six_letter_words)
    found_item = False
    for item in sorted_six_letter_words:
        return_bool = match_subword_in_word_LBL(nr_seven,item)
        if(return_bool):
            found_item = True
            return item
    if(found_item == False):
        print("Error in code - unable to calculate nr 0")
def calculate_nr_six(single_line,nr_nine,nr_zero):
    print("Calculating nr 6")
    six_letter_words = []
    sorted_six_letter_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == 6):
            six_letter_words.append(item)
    print(six_letter_words)
    for item in six_letter_words:
        sorted_six_letter_words.append(sort_single_word(item))
    print("Sorted words")
    print(sorted_six_letter_words)

    while nr_nine in sorted_six_letter_words: sorted_six_letter_words.remove(nr_nine)
    while nr_zero in sorted_six_letter_words: sorted_six_letter_words.remove(nr_zero)

    print(sorted_six_letter_words)
    found_item = False
    if sorted_six_letter_words:
        found_item = True
        return sorted_six_letter_words[0]
    if(found_item == False):
        print("Error in code - unable to calculate nr 6")
def calculate_nr_five(single_line,nr_six,nr_eight):
    print("Calculating nr 5")
    #sorted_six_letter_words = fetch_strings_of_length(single_line,6)
    sorted_five_letter_words = fetch_strings_of_length(single_line,5)
    letter_C = get_missing_letter_in_subword(nr_six,nr_eight)
    if(letter_C):
        for item in sorted_five_letter_words:
            if letter_C not in item:
                return item
    else:
        print("Unable to locate letter C")
def calculate_nr_two(single_line,nr_three,nr_five):
    print("Calculating nr 2")
    sorted_five_letter_words = fetch_strings_of_length(single_line,5)
    while nr_three in sorted_five_letter_words: sorted_five_letter_words.remove(nr_three)
    while nr_five in sorted_five_letter_words: sorted_five_letter_words.remove(nr_five)

    if sorted_five_letter_words:
        return sorted_five_letter_words[0]
    else:
        print("Unable to calculate nr 2")

def calculate_number_values(single_line):
    nr_1 = calculate_nr_one(single_line)
    nr_4 = calculate_nr_four(single_line)
    nr_7 = calculate_nr_seven(single_line)
    nr_8 = calculate_nr_eight(single_line)

    nr_3 = calculate_nr_three(single_line,nr_1)
    print("Nr 3===>" + nr_3)
    nr_9 = calculate_nr_nine(single_line,nr_3)
    print("Nr 9===>" + nr_9)
    nr_0 = calculate_nr_zero(single_line,nr_9,nr_7)
    
    nr_6 = ""
    if(nr_9 and nr_0):
        nr_6 = calculate_nr_six(single_line,nr_9,nr_0)
    nr_5 = ""
    if(nr_6 and nr_8):
        nr_5 = calculate_nr_five(single_line,nr_6,nr_8)
    nr_2 = ""
    if(nr_3 and nr_5):
        nr_2 = calculate_nr_two(single_line,nr_3,nr_5)
    print("Nr 0===>" + nr_0)
    print("Nr 1===>" + nr_1)
    print("Nr 2===>" + nr_2)
    print("Nr 3===>" + nr_3)
    print("Nr 4===>" + nr_4)
    print("Nr 5===>" + nr_5)
    print("Nr 6===>" + nr_6)
    print("Nr 7===>" + nr_7)
    print("Nr 8===>" + nr_8)
    print("Nr 9===>" + nr_9)

    return_array = [nr_0,nr_1,nr_2,nr_3,nr_4,nr_5,nr_6,nr_7,nr_8,nr_9]
    return return_array
    #print(nr_5)
    #print(nr_6)
    #print(nr_1)
    #print(nr_4)
    #print(nr_7)
    #print(nr_8)
    #print(nr_3)
    #print(nr_9)
    
    #nr_2 = calculate_nr_two(single_line,nr_1)
    
def calculate_output_values(single_line,solved_combinations):
    split_it = single_line.split("|")
    print(split_it)
    output_values = split_it[1].strip()
    print(output_values)
    output_list = output_values.split(" ")
    print(output_list)

    result_list = []
    for item in output_list:
        return_result = get_matching_number(sort_single_word(item),solved_combinations)
        if(return_result):
            result_list.append(str(return_result))
        #temp_item = sort_single_word(item)
        #for check_value in solved_combinations:
         #   if temp_item in check_value:
          #      print("Found match===>" + item)
    return result_list

total_output_result = 0
for item in fileRead_list:
    #calculate_nr_one(item)
    combinations = calculate_number_values(item)
    result_list = calculate_output_values(item,combinations)
    full_result = ""
    for result in result_list:
        full_result += result
    #print(full_result)
    #print(combinations)
    #print("results")
    #print(result_list)
    total_output_result += int(full_result)

print(total_output_result)