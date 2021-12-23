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
        if(common_bit <= 0):
            return 1
        elif(common_bit > 0):
            return 0
            
input_list = []
updated_list = []
#most_common_bit = 0
iterator = 0
with open("input_02_test.txt", "r") as f:
    lines = f.read().splitlines()
    for line in lines:
        input_list.append(line)
returnValue = calc_CommonBit(input_list,iterator,"least")
print(returnValue)
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