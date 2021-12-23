####calculate Power consumption

###Gamme rate: find most common bit for each position
###Epsilon rate: find least common bit for each position
##=====>Epsilon should be the oposite of the Gamma Rate

###Power consumption: Gamma * Epsilon, in base 10

#######################################################
##Read to memory?

gamma_rate_arr = []
with open("input_01.txt", "r") as f:
    lines = f.read().splitlines()

    #print(len(lines[0]))
    binary_length = len(lines[0])
    length_iterator = 0
    while length_iterator < binary_length:
        gamma_rate_arr.append(0)
        length_iterator += 1
    print("Gamma rate arr===>" + str(gamma_rate_arr))
    for line in lines:
        list_line = list(line)
        print(list_line)
        iterator = 0
        for digit in list_line:
            if(int(digit) == 0):
                gamma_rate_arr[iterator] -= 1
            elif(int(digit) == 1):
                gamma_rate_arr[iterator] += 1
            iterator += 1

gamma_rate = ""
epsilon_rate = ""
for x in gamma_rate_arr:
    if(x > 0):
        gamma_rate += str(1)
        epsilon_rate += str(0)
    elif(x < 0):
        gamma_rate += str(0)
        epsilon_rate += str(1)
print("Gamma rate==>" + gamma_rate)
print("Epsilon Rate==>" + epsilon_rate)

gamma_rate_int = int(gamma_rate, base = 2)
epsilon_rate_int = int(epsilon_rate, base = 2)

print("Gamma rate int:" + str(gamma_rate_int))
print("Epsilon rate int:" + str(epsilon_rate_int))

power_consumption = gamma_rate_int * epsilon_rate_int
print("Power consumption of the submarine===>" + str(power_consumption))