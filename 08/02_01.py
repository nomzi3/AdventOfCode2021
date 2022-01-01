fileRead_list = []

with open("input_02.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        fileRead_list.append(line)

##Input unsorted word - 
# Returns - word sorted alphabetically
def sort_singleWord(unsorted_word):
    list_word = list(unsorted_word)
    list_word.sort()
    sorted_word = ''.join(list_word)
    return sorted_word
##fetches all strings matching length X
####Returns - sorted list
def fetch_stringsOfLength(single_line,string_length):
    unsorted_list_of_words = []
    sorted_list_of_words = []
    split_line = single_line.split(" ")
    for item in split_line:
        if(len(item) == string_length):
            unsorted_list_of_words.append(item)
    for item in unsorted_list_of_words:
        sorted_list_of_words.append(sort_singleWord(item))
    return sorted_list_of_words
##fetch output-list from our input-string
####Returns - sorted list
def fetch_outputList(single_line):
    unsorted_list_of_words = []
    sorted_list_of_words = []
    split_line = single_line.split("|")
    #print(split_line)
    output_string = split_line[1].strip()
    #output_list = list(output_string)
    output_list = output_string.split(" ")
    #print(output_list)
    for item in output_list:
        unsorted_list_of_words.append(item)
    for item in unsorted_list_of_words:
        sorted_list_of_words.append(sort_singleWord(item))
    return sorted_list_of_words
    #return True
################################################
#############BaseCombinations###################
##calculate combination 1 - length 2
###returns sorted string
def calculate_nrOne(single_line):
    return_value = fetch_stringsOfLength(single_line,2)
    return return_value[0]
##calculate combination 4 - length 4
###returns sorted string
def calculate_nrFour(single_line):
    return_value = fetch_stringsOfLength(single_line,4)
    return return_value[0]
##calculate combination 7 - length 3
###returns sorted string
def calculate_nrSeven(single_line):
    return_value = fetch_stringsOfLength(single_line,3)
    return return_value[0]
##calculate combination 8 - length 7
###returns sorted string
def calculate_nrEight(single_line):
    return_value = fetch_stringsOfLength(single_line,7)
    return return_value[0]
################################################
###############Translate Basecombinations#######
###translates the base-combinations (1,4,7,8)
######returns list of combinations.
def translate_baseCombinations(single_line):
    return_list = []
    return_list.append(calculate_nrOne(single_line))
    return_list.append(calculate_nrFour(single_line))
    return_list.append(calculate_nrSeven(single_line))
    return_list.append(calculate_nrEight(single_line))
    #print(calculate_nrOne(single_line))
    #print(calculate_nrFour(single_line))
    #print(calculate_nrSeven(single_line))
    #print(calculate_nrEight(single_line))
    return return_list
################################################
##############Calculate Value###################
##Calculates the value of a 5-letter word
####Returns - Number
def calculate_value_Fives(single_word,value_of_CF,value_of_BD,value_of_A,value_of_EG):
    letter_counter = 0
    for letter in value_of_BD:
        if letter in single_word:
            letter_counter += 1
        if(letter_counter == 2):
            return 5
    letter_counter = 0
    for letter in value_of_EG:
        if letter in single_word:
            letter_counter += 1
        if(letter_counter == 2):
            return 2
    letter_counter = 0
    for letter in value_of_CF:
        if letter in single_word:
            letter_counter += 1
        if(letter_counter == 2):
            return 3
    print("Unable to locate the value of 5")
    #if value_of_BD in single_word:
     #   return 5
    
    #elif value_of_EG in single_word:
     #   return 2
    #elif value_of_CF in single_word:
     #   return 3
    #else:
     #   print("Unable to locate the value of 5")
##Calculates the value of a 6-letter word
####Returns - Number
def calculate_value_Sixes(single_word,value_of_CF,value_of_BD,value_of_A,value_of_EG):
    #print("Single Word==>" + single_word)
    for letter in value_of_CF:
        if letter not in single_word:
            return 6
    for letter in value_of_BD:
        if letter not in single_word:
            return 0
    for letter in value_of_EG:
        if letter not in  single_word:
            return 9
    print("Unable to calculate value of Six-letter-word")
##fetches the number value of the word combination
####Returns - Number
def fetch_valueOf_wordCombination(single_word,value_of_CF,value_of_BD,value_of_A,value_of_EG):
    #print("testing")
    if(len(single_word) == 2):
        return 1
    elif(len(single_word) == 4):
        return 4
    elif(len(single_word) == 3):
        return 7
    elif(len(single_word) == 7):
        return 8
    elif(len(single_word) == 5):
        return_value = calculate_value_Fives(single_word,value_of_CF,value_of_BD,value_of_A,value_of_EG)
        return return_value
    elif(len(single_word) == 6):
        return_value = calculate_value_Sixes(single_word,value_of_CF,value_of_BD,value_of_A,value_of_EG)
        return return_value
def calculate_value_CF(base_combinations):
    return base_combinations[0]
def calculate_value_BD(base_combinations):
    value_CF = calculate_value_CF(base_combinations)
    value_CFoBD = base_combinations[1]
    #print(value_CFoBD)
    temp_value_CFoBD = list(value_CFoBD)
    #temp_value_CF = list(value_CF)
    #print(temp_value_CFoBD)
    for letter in value_CF:
        temp_value_CFoBD.remove(letter)
    #print(temp_value_CFoBD)
    value_BD = ''.join(temp_value_CFoBD)
    return value_BD
def calculate_value_A(base_combinations):
    value_CF = calculate_value_CF(base_combinations)
    value_CFoA = base_combinations[2]
    #temp_value_CF = list(value_CF)
    temp_value_CFoA = list(value_CFoA)
    for letter in value_CF:
        temp_value_CFoA.remove(letter)
    value_A = ''.join(temp_value_CFoA)
    return value_A
def calculate_value_EG(base_combinations):
    value_CF = calculate_value_CF(base_combinations)
    value_BD = calculate_value_BD(base_combinations)
    value_A = calculate_value_A(base_combinations)
    temp_value_CFBDAEG = list(base_combinations[3])
    
    for letter in value_CF:
        temp_value_CFBDAEG.remove(letter)
    for letter in value_BD:
        temp_value_CFBDAEG.remove(letter)
    for letter in value_A:
        temp_value_CFBDAEG.remove(letter)
    value_EG = ''.join(temp_value_CFBDAEG)
    return value_EG
##Calculates the output-value - E.g. "1234"
####Returns this number
def calculate_outputValue(single_line,base_combinations):
    print("test")
    value_CF = calculate_value_CF(base_combinations)
    value_BD = calculate_value_BD(base_combinations)
    value_A = calculate_value_A(base_combinations)
    value_EG = calculate_value_EG(base_combinations)

    print("Value CF==>" + value_CF)
    print("Value BD==>" + value_BD)
    print("Value A===>" + value_A)
    print("Value EG==>" + value_EG)
    output_list = fetch_outputList(single_line)
    result_string = ""
    for item in output_list:
        return_value = fetch_valueOf_wordCombination(item,value_CF,value_BD,value_A,value_EG)
        if(return_value == None):
            print("None Found:" + item)
        result_string += str(return_value)
        #print(return_value)
    #print(output_list)
    #print(value_CF)
    #print(value_BD)
    #print(value_A)
    #print(value_EG)
    #value_A = 
    return int(result_string)
counter = 1
total_output_value = 0
for item in fileRead_list:
    #print(item)
    #print("Test")
    print("Iteration==>" + str(counter))
    base_combinations = translate_baseCombinations(item)
    #print(base_combinations)
    output_value = calculate_outputValue(item,base_combinations)
    print(output_value)
    total_output_value += output_value
    counter += 1
print("Total output value====>" + str(total_output_value))