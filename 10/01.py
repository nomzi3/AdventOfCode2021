fileRead_list = []
with open("input_01.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        #print(line)
        fileRead_list.append(line)
print(fileRead_list)
##Check value of illegal character
##Return it
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
    #print(single_line)
    open_bracket_list = []
    for item in single_line:
        #print(item)
        #print(checkIfMatch_openBracket(item))
        #return_value = checkIfMatch_openBracket(item)
        #if(return_value):
        if(checkIfMatch_openBracket(item)):
            #open_bracket_list.append(item)
            open_bracket_list.insert(0,item)
        else:
            #print("Closing bracket")
            if not open_bracket_list:
                print("List is empty")
                return 0
            elif not checkIfMatch_closingBracket(open_bracket_list[0],item):
                print("Bracket__: " + item + " not matching__: " + open_bracket_list[0])
                return calculateValue_illegalCharacter(item)
            elif checkIfMatch_closingBracket(open_bracket_list[0],item):
                print("Closing bracket matching a Open Bracket - removing")
                open_bracket_list.pop(0)
        #if it matches a open-bracket, add to open-bracket list
        ###if matching closing bracket - check last item in open-bracket list.
        #####if matching, remove it from the open_bracket_list, and continue.
        ###if open_bracket_list is empty, or not matching the last open bracket - return True
        ###
        ###if running until end of single_line, and no corrupted, return False.
        #print(open_bracket_list)
    return 0
total_value = 0
for item in fileRead_list:
    print("##############################")
    return_value = checkLine_corrupted(item)
    total_value += return_value
    #if return_value == False:
     #   print("False")
print("Total Value:" + str(total_value))