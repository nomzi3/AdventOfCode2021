fileRead_list = []
with open("input_02.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        #print(line)
        fileRead_list.append(line)
print(fileRead_list)
##Check value of illegal character
##Return its value
##if no match on item, return 0
def calculateValue_illegalCharacter(item):
    if item == ')':
        return 3
    elif item == ']':
        return 57
    elif item == '}':
        return 1197
    elif item == '>':
        return 25137
    else:
        return 0
##Check if bracket is a opening bracket
###Return true/false
def checkIfMatch_openBracket(item):
    if item == '(':
        return True
    elif item == '[':
        return True
    elif item == '{':
        return True
    elif item == '<':
        return True
    else:
        return False
##Check if open bracket matches closing bracket - given in input
#####Return true/false
def checkIfMatch_closingBracket(open_bracket,closing_bracket):
    if open_bracket == '(' and closing_bracket == ')':
        return True
    elif open_bracket == '[' and closing_bracket == ']':
        return True
    elif open_bracket == '{' and closing_bracket == '}':
        return True
    elif open_bracket == '<' and closing_bracket == '>':
        return True
    else:
        return False
##check if line is corrupted
##Returns 0 if False
##Else - return Value of first illegal character
##
def checkLine_corrupted(single_line):
    ##open bracket list - first in, first out
    open_bracket_list = []
    for item in single_line:
        ##if open-bracket, insert it into position 0
        if(checkIfMatch_openBracket(item)):
            open_bracket_list.insert(0,item)
        #closing bracket
        else:
            ##we should trust our input, but I don't
            if not open_bracket_list:
                print("List is empty")
                return 0
            #We located an illegal closing bracket - returning the value and exiting
            elif not checkIfMatch_closingBracket(open_bracket_list[0],item):
                print("Bracket__: " + item + " not matching__: " + open_bracket_list[0])
                return calculateValue_illegalCharacter(item)
            #legal closing bracket - pop it from our FIFO list and continue.
            elif checkIfMatch_closingBracket(open_bracket_list[0],item):
                print("Closing bracket matching a Open Bracket - removing")
                open_bracket_list.pop(0)
    return 0
#################################################################
###############################Part2#############################
##Return value of our incomplete character
def calculateValue_incompleteCharacter(item):
    if item == '(':
        return 1
    elif item == '[':
        return 2
    elif item == '{':
        return 3
    elif item == '<':
        return 4
    else:
        return 0
def calculate_incompleteLineScore(fifo_list):
    total_score = 0
    for item in fifo_list:
        total_score = total_score * 5 + calculateValue_incompleteCharacter(item)
    return total_score
##Works through an incomplete line (we trust our input)
##Returns autocomplete score of the line
#####if 0 returned, it crashed or no extra work required. still, print the list in this case
def checkLine_incomplete(single_line):
    #FIFO list - first in, first out
    open_bracket_list = []
    for item in single_line:
        #if open-bracket, insert into FIFO list
        if(checkIfMatch_openBracket(item)):
            open_bracket_list.insert(0,item)
        ##closing bracket
        else:
            #we should trust our input, but I don't
            if not open_bracket_list:
                print("List is empty, exiting")
                return 0
            #Located an illegal closing bracket - should not happen in thise case
            elif not checkIfMatch_closingBracket(open_bracket_list[0],item):
                print("Bracket__: " + item + " not matching__: " + open_bracket_list[0])
                return 0
            # legal closing bracket, pop it from our FIFO list and continue
            elif checkIfMatch_closingBracket(open_bracket_list[0],item):
                #print("Closing bracket matching a Open Bracket - removing----")
                open_bracket_list.pop(0)
    print(open_bracket_list)
    return calculate_incompleteLineScore(open_bracket_list)
total_value = 0
incomplete_lines = []
for item in fileRead_list:
    print("##############################")
    return_value = checkLine_corrupted(item)
    if return_value != 0:
        total_value += return_value
    else:
        incomplete_lines.append(item)
        
    #if return_value == False:
     #   print("False")
incomplete_value = 0
incomplete_value_list = []
for item in incomplete_lines:
    return_value = checkLine_incomplete(item)
    if return_value != 0:
        print(return_value)
        incomplete_value_list.append(return_value)
        incomplete_value += return_value
print("Total CORRUPTED Value:" + str(total_value))
print("Total INCOMPLETE value:" + str(incomplete_value))
print(incomplete_value_list)
incomplete_value_list.sort()
length_of_incomplete_list = len(incomplete_value_list)
print(length_of_incomplete_list)
value_to_print = int((length_of_incomplete_list-1)/2)
print("Middle of the pack value====>" + str(incomplete_value_list[value_to_print]))
