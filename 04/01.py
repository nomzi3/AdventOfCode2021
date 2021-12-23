drawing_numbers = []
input_list = []
with open("input_01_test.txt", "r") as f:
    #input = f.read().splitlines()
    #for i in input:
     #   print(i)
    input_list = f.readlines()



drawing_numbers = input_list[0].strip()
print(drawing_numbers)

###TODO:
# read file, split into functional bits.
####put drawing numbers into an array
##gameboards sort in some fashion?

###