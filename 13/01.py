
##Load input into a list
###Return two lists:
#####->cordinates
#####->Fold instructions
def load_inputIntoLists(filename):
    fileRead_list = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            fileRead_list.append(line)
    cord_list = []
    instr_list = []
    for line in fileRead_list:
        if 'fold' in line:
            split_line = line.split(" ")
            print(split_line[2])
            cords = split_line[2].split("=")
            cords[1] = int(cords[1])
            instr_list.append(cords)
        elif line != "":
            split_line = line.split(",")
            for item in split_line:
                item = int(item)
            cord_list.append(split_line)
    return cord_list, instr_list
def convert_stringListToInt(listToIterate):
    return_list = []
    for item in listToIterate:
        temp_list = []
        item1 = int(item[0])
        item2 = int(item[1])
        temp_list.append(item1)
        temp_list.append(item2)
        return_list.append(temp_list)
    return return_list
def remove_duplicatesFromList(listToIterate):
    return_list = []

    for item in listToIterate:
        if item not in return_list:
            return_list.append(item)
        #if item in return_list:
         #   print("Found duplicate")
        #else:
            

    return return_list
def fold_by_X(listToIterate,x_value):
    return_list = []

    for item in listToIterate:
        if int(item[0]) > int(x_value):
            temp_list = []
            distance_from_fold = int(item[0]) - int(x_value)
            temp_x_value = int(item[0]) - (2 * int(distance_from_fold))
            temp_list.append(temp_x_value)
            temp_list.append(item[1])
            return_list.append(temp_list)
        else:
            return_list.append(item)
    return return_list
def fold_by_Y(listToIterate,y_value):
    return_list = []

    for item in listToIterate:
        if int(item[1]) > int(y_value):
            print("item that will be folded: " + str(item[1]))
            temp_list = []
            distance_from_fold = int(item[1]) - int(y_value)
            print("Distance that will be folded:" + str(distance_from_fold))
            temp_y_value = int(item[1]) - (2 * int(distance_from_fold))
            print("new y value==>" + str(temp_y_value))
            temp_list.append(item[0])
            temp_list.append(temp_y_value)
            return_list.append(temp_list)
        else:
            return_list.append(item)

    return return_list
def execute_folds(listToIterate,fold_instructions):
    working_list = listToIterate.copy()
    for item in fold_instructions:
        print(item)
        if item[0] == 'x':
            temp_list = fold_by_X(working_list,item[1])
            working_list.clear()
            working_list = temp_list.copy()
        elif item[0] == 'y':
            temp_list = fold_by_Y(working_list,item[1])
            working_list.clear()
            working_list = temp_list.copy()
    print(working_list)
    temp_list = remove_duplicatesFromList(working_list)
    working_list.clear()
    working_list = temp_list.copy()
    print("length===>" + str(len(working_list)))
        

###Modified the input-text, as I over-complicated and solved the whole thing before I had to
cordinate_list, instruction_list = load_inputIntoLists("01_input_modified.txt")
print("Cordinate list")
print(cordinate_list)
print("Instruction list")
print(instruction_list)
converted_list = convert_stringListToInt(cordinate_list)
cordinate_list.clear()
cordinate_list = converted_list.copy()
execute_folds(cordinate_list,instruction_list)