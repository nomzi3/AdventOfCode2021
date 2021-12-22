input_array = []
with open("input_2.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        ###input will be a str, unless typecast to int.
        input_array.append(int(line))

print(input_array)

###spliding window
####use numbers - group 1, group 2, group 3 etc.

"""
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H"""

###split until you cannot split into 3 anymore....
array_length = len(input_array)
print(array_length)
#print(input_array[array_length-1])
current_iterator = 0
depth_array = []

for x in input_array:
    if(current_iterator+2 >= array_length):
        ##break the array
        break
    else:
        #print("Current=>" + str(current_iterator) + " " + str(input_array[current_iterator]) + " " + str(input_array[current_iterator+1]) + " " + str(input_array[current_iterator+2]))
        total_value = input_array[current_iterator] + input_array[current_iterator+1] + input_array[current_iterator+2]
        print("Current=>" + str(total_value))
        current_iterator += 1
        depth_array.append(total_value)
print(depth_array)



depth_increases = 0
currentIterValue = 0
val1 = 0
val2 = 0
for x in depth_array:
    if(currentIterValue == 0):
        print("first value, skipping")
        val1 = int(x)
        currentIterValue += 1
    elif(currentIterValue > 0):
        val2 = int(x)
        print("Compaing: " + str(val2) + " >>>> " + str(val1))
        if(val2 > val1):
            depth_increases += 1
            print("===>INCREASED")
        elif(val2 == val1):
            print("NO CHANGE<====")
        elif(val2 < val1):
            print("DECREASE<====")
        val1 = int(val2)
print("Done iterating, result====>" + str(depth_increases))
