###slightly different from 01

##life support rating = oxygen generator rating * C02 Scrubber rating

##oxygen generator rating = most common bit criteria
######if 0 o 1 is equal in a pos, keep 1
##C02 scrubber rating = least common bit criteria
######if 0 o 1 is equal in a pos, keep 0
######################################################

####Loop through list, find most common/least common of left-most pos.
#######keep all numbers matching this, discard the rest
###loop through next pos, repeat until only 1 value remains
##############################################

def calc_CommonBit(check_list,iterNumber,calcOption):
    common_bit = 0
    for elem in check_list:
        line = list(elem)
        if(int(line[iterNumber]) == 0):
            common_bit -= 1
        elif(int(line[iterNumber]) == 1):
            common_bit += 1
    if(calcOption == "most"):
        if(common_bit >= 0):
            return 1
        elif(common_bit < 0):
            return 0
    elif(calcOption == "least"):
        if(common_bit < 0):
            return 1
        elif(common_bit >= 0):
            return 0

def remove_CommonBit(check_list,iterNumber,keepValue):
    ##if keepValue is X, keep all numbers with keepValue, at iterNumber position
    ##return list of accepted numbers
    return_list = []
    print("Remove items not matching")
    print("Input: array")
    print(check_list)
    for item in check_list:
        line = list(item)
        if(int(line[iterNumber]) == keepValue):
            print("Found match:" + item)
            return_list.append(item)
    print("Return list:")
    print(return_list)
    return return_list

def generate_value(list_to_check,most_or_least):
    return_value = ""
    stillChecking = True
    temp_list = list_to_check
    iteration = 0
    while(stillChecking):
        if(len(temp_list) == 1):
            print("found a single digit, returning")
            return_value = temp_list[0]
            stillChecking = False
            break
        check_value = calc_CommonBit(temp_list,iteration,most_or_least)
        temp_list = remove_CommonBit(temp_list,iteration,check_value)
        iteration += 1
    return return_value

def generate_lifesupport_rating(oxygen_gen_rating,c02_scrub_rating):
    #gamma_rate_int = int(gamma_rate, base = 2)
    #epsilon_rate_int = int(epsilon_rate, base = 2)
    oxygen_int = int(oxygen_gen_rating, base = 2)
    c02_int = int(c02_scrub_rating, base = 2)
    return oxygen_int * c02_int
input_list = []
#updated_list = []
#most_common_bit = 0
iterator = 0
with open("input_02.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        input_list.append(line)
oxygen_rating = generate_value(input_list,"most")
c02_rating = generate_value(input_list,"least")
lifesupport_rating = generate_lifesupport_rating(oxygen_rating,c02_rating)
print("Life support rating:>" + str(lifesupport_rating))
#print("end of the line:" + generate_value(input_list,"least"))
#print("Life Support Rating===>" + str(generate_lifesupport_rating()))
#returnValue = calc_CommonBit(input_list,iterator,"most")
#print(returnValue)
"""
return_list = remove_CommonBit(input_list,iterator,returnValue)
print(input_list)
print(return_list)
iterator += 1
returnValue = calc_CommonBit(return_list,iterator,"most")
print(returnValue)
return_list = remove_CommonBit(return_list,iterator,returnValue)
print(return_list)
iterator += 1
returnValue = calc_CommonBit(return_list,iterator,"most")
print(returnValue)
return_list = remove_CommonBit(return_list,iterator,returnValue)
print(returnValue)
"""

###TODO 
####add function: remove all numbers not containing X
######where X may be least, or most common bit.

###run-loop:
####input: most/least, list to run it on
######returns: single value which will be the oxygen generator rating, or CO2 scrubber rating





"""
for elem in input_list:
    line = list(elem)
    if(int(line[iterator]) == 0):
        most_common_bit -= 1
    elif(int(line[iterator]) == 1):
        most_common_bit += 1
if(most_common_bit >= 0):
    print("Most common bit===>1")
elif(most_common_bit < 0):
    print("Most common bit===>0")
"""
"""
for elem in input_list:
    line = list(elem)
    if(int(line[iterator]) == 1):
        updated_list.append(elem)
"""
##print(input_list)
##print(updated_list)