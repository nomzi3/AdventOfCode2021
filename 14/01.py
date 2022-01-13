from collections import Counter
"""
pair insertion rules
if xx exists, insert y inbetween

insertion occurs for the whole sequence, at the same time

##take input polymer -> split into section of 2 (overlapping)
->insert letter as per insertion rules
    ->merge back into one string
end goal: run above for X iterations
"""

##Load input into string + dict
###Dict for handling the translation-rules
###String for holding the Polymer
#####Return as a Tuple
def load_inputIntoLists(filename):
    fileRead_list = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            fileRead_list.append(line)
    polym = fileRead_list[0]
    fileRead_list.pop(0)
    fileRead_list.pop(0)
    
    translation_dict = {}
    for line in fileRead_list:
        split_line = line.split(" ")
        print(split_line)

        translation_dict[split_line[0]] = split_line[2]
    return polym, translation_dict

##Split the poly int working sizes - for rule-processing
###Return - list with values to match
def split_polymerIntoWorkingSizes(poly_string):
    counter = 0
    split_poly = list(poly_string)
    check_list = []
    
    length = len(split_poly)-1
    
    while(counter < length):
        temp_string = ""
        #temp_list.append(split_poly[counter])
        #temp_list.append(split_poly[counter+1])
        temp_string += split_poly[counter]
        temp_string += split_poly[counter+1]
        check_list.append(temp_string)
        counter += 1
    return check_list
##Calculate our insert values
####return - list with inserts
def insert_calculation(match_list,rule_dict):
    pair_insert_list = []
    for item in match_list:
        insert_value = rule_dict.get(item)
        pair_insert_list.append(insert_value)
    return pair_insert_list

##Get final polymer-string
####Returns the result string
def get_finalPolymer(poly_string,ins_results):
    #counter = 0
    split_poly = list(poly_string)
    result_string = split_poly.pop(0)
    for i in range(0,len(split_poly)):
        result_string += ins_results[i]
        result_string += split_poly[i]
    #print(result_string)
    return result_string
def running_function(poly_string,trans_rules,iterationsToRun):
    temp_poly_string = poly_string
    counter = 1
    print("Template:  " + temp_poly_string)
    for i in range(1,iterationsToRun+1):
        polymer_match_list = split_polymerIntoWorkingSizes(temp_poly_string)
        #print(polymer_match_list)
        insert_results = insert_calculation(polymer_match_list,trans_rules)
        #print(insert_results)
        temp_poly_string = get_finalPolymer(temp_poly_string,insert_results)
        print("After step " + str(i) + ": " + temp_poly_string)
        print("Length: " + str(len(temp_poly_string)))
    counted_letters = Counter(temp_poly_string)
    print(counted_letters)
    max_value = max(counted_letters.values())
    min_value = min(counted_letters.values())
    print("Max: " + str(max_value))
    print("Min: " + str(min_value))
    our_answer = max_value - min_value
    print("Answer to our question===>" + str(our_answer))

polymer_string, translation_rules = load_inputIntoLists("01_input.txt")

print(polymer_string)
print(translation_rules)

running_function(polymer_string,translation_rules,10)
##################################
"""
polymer_match_list = split_polymerIntoWorkingSizes(polymer_string)
print(polymer_match_list)
insert_results = insert_calculation(polymer_match_list,translation_rules)
print(insert_results)
get_finalPolymer(polymer_string,insert_results)
"""