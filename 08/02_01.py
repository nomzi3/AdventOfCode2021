fileRead_list = []
input_list = []
output_list = []
with open("input_02_test1.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        #print(line)
        fileRead_list.append(line)

print(fileRead_list)
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

################################################
#############BaseCombinations###################
##calculate combination 1 - length 2
###returns word-combination Sorted
def calculate_nrOne(single_line):
    return fetch_stringsOfLength(single_line,2)
##calculate combination 4 - length 4
###returns word-combination - Sorted
def calculate_nrFour(single_line):
    return fetch_stringsOfLength(single_line,4)
##calculate combination 7 - length 3
###returns word-combination - Sorted
def calculate_nrSeven(single_line):
    return fetch_stringsOfLength(single_line,3)
##calculate combination 8 - length 7
###returns word-combination - Sorted
def calculate_nrEight(single_line):
    return fetch_stringsOfLength(single_line,7)
################################################
################################################
##############Calculate Sixes###################



################################################
################################################

##Take single line as input
####Returns -> list with combinations representing numbers
def calculateNumberValues(single_line):
    print("temp")

for item in fileRead_list:
    print(item)