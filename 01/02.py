input_array = []
with open("02_input_test.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        input_array.append(line)

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

