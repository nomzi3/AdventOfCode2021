###TODO
#def function to move ALL crabs into position X
####calculate distance required for all crabs - return
######def function to calculate position to move crabs to
####test each by calling move function, store result
###return -> lowest possible result
pos_list = []

with open("input_01_test.txt", "r") as f:
    i = f.readline()
    pos_list = i.split(",")
print(pos_list)



"""
total_count = 0
for i in pos_list:
    total_count += int(i)
print("Total:" + str(total_count))
print("Nr of items:" + str(len(pos_list)))
print("Median___>" + str(total_count / len(pos_list)))
"""

total_count = len(pos_list)
print(total_count)
if(total_count % 2 == 0):
    print(pos_list[int(total_count/2)])
    print(pos_list[int(total_count/2)+1])
else:
    print("no")