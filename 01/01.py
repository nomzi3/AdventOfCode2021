
inputArray = []

with open("01_input.txt", "r") as f:
    lines = f.read().splitlines()
    
    for line in lines:
        #print(line)
        inputArray.append(line)

###skip first value, set to val1
#####next iteration, compare to val1
#########fetch result
####set val1 to val2, repeat until end of list.


depth_increases = 0
currentIterValue = 0
val1 = 0
val2 = 0
for x in inputArray:
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
        val1 = int(val2)
print("Done iterating, result====>" + str(depth_increases))

###amount of values to be checked
print(len(inputArray))

###learning for the future - reason why first version failed -> 
#####forgetting to typecast the input as int, rather than string.
######all compare functions worked, except when comparing above 1000 with sub 1000.