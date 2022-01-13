##Part 2 of the puzzle
####won't be possible to solve it like we did with part1 - as it fills up the ram instantly.

#TODO
"""
Read from file:
while active:
    read line from file
        ->check if line is empty
            ->we reached the end
        ->get size of line
            ->if less than 50 characters, means its the last line in the file
    ->process 2 characters from line
        ->get insert-value of these 2 characters
            ->add first character, and insert value to write-buffer.
            ->when done processing line - print buffer to output-file - 50 characters at the time.
                ->if any characters left after being done printing, save for next line.
             

    run until last 2 characters in input-string
"""
##Load primary input into string + dict
###Dict for handling the translation-rules
###String for holding the Polymer
#####Return as a Tuple
def load_inputIntoLists(filename):
    fileRead_list = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            fileRead_list.append(line)
    polym = fileRead_list[0]
    fileRead_list.pop(0)
    fileRead_list.pop(0)
    
    translation_dict = {}
    for line in fileRead_list:
        split_line = line.split(" ")
        print(split_line)

        translation_dict[split_line[0]] = split_line[2]
    log_file = polym + "-0.log"
    with open(log_file, 'w') as f:
        f.write(polym)
        #f.write("\n")
    return polym, translation_dict
#Fetches the Insert-value for a 2-char combination
###Returns the insert-value
def get_insertValue(letters_to_match,rule_dict):
    return rule_dict.get(letters_to_match)
##Appends a line to a file - adding a \n for linebreak
def write_line_to_file(file_to_append,line_to_write):
    with open(file_to_append, "a") as f:
        line_to_write += "\n"
        f.write(line_to_write)

###process the write buffer
##makes sure the output is written in a correct manner - 
# until the buffer is empty.
def processWriteBuffer(filename,buffer_to_write):
    print("printing to file")
    items_left_to_print = True
    buffer_left_to_print = len(buffer_to_write)
    start_point = 0
    while items_left_to_print:
        if(buffer_left_to_print < 50):
            write_line_to_file(filename,buffer_to_write[start_point:buffer_left_to_print])
            items_left_to_print = False
        else:
            write_line_to_file(filename,buffer_to_write[start_point:buffer_to_write])
            start_point += buffer_to_write - 1
    

##if end of file - print everything
def processReadBuffer(filename_to_write,read_buffer_to_process,rule_dict,endOfFile):
    write_buffer = ""
    still_running = True
    read_buffer_list = list(read_buffer_to_process)
    cleaned_list = [i for i in read_buffer_list if i != '\n']
    read_buffer_list.clear()
    read_buffer_list = cleaned_list.copy()
    while still_running:
        if len(read_buffer_list) <= 1:
            still_running = False
        else:
            temp_pop = read_buffer_list.pop(0)
            temp_value = temp_pop + read_buffer_list[0]
            insert_value = get_insertValue(temp_value,rule_dict)
            #print("Combination: " + temp_value + " insert_value: " + insert_value)
            write_buffer = write_buffer + temp_pop + insert_value

    read_buffer_remaining = read_buffer_list[0]
    if endOfFile:
        write_buffer += read_buffer_remaining
        read_buffer_remaining = ""
    processWriteBuffer(filename_to_write,write_buffer)
    return read_buffer_remaining
def process_file_results(filename):
    result_dict = {}
    with open(filename, 'r') as f:
        end_of_file = False
        while end_of_file != True:
            line = f.read()
            line.strip()
            if line == '':
                    print('EOF')
                    end_of_file = True
            for letter in line:
                if letter != '\n':
                    if letter in result_dict:
                        result_dict[letter] += 1
                    else:
                        result_dict[letter] = 1
    print(result_dict)
    max_value = max(result_dict.values())
    min_value = min(result_dict.values())
    print("Max: " + str(max_value))
    print("Min: " + str(min_value))
    our_answer = max_value - min_value
    print("Answer to our question===>" + str(our_answer))
def processFile(poly_to_mutate,rule_dict,iterations_to_run):
    
    name_counter = 0
    base_ending = ".log"
    #test_file = "test.txt"
    #write_buffer = ""
    read_buffer = ""
    
    counter = 1
    read_file = ""
    print("Processing file")
    while counter <= iterations_to_run:
        print("Starting process -> iteration: " + str(counter))
        read_file = poly_to_mutate + "-" + str(name_counter) + base_ending
        print("Read File Name==> " + read_file)
        name_counter += 1
        write_file = poly_to_mutate + "-" + str(name_counter) + base_ending
        print("Write File Name==> " + write_file)
        with open(read_file, 'r') as f_read:
            end_of_file = False
            #if read_file == "1.log":
                #print("testing")
            while end_of_file != True:
                line = f_read.read()
                line.strip()
                if line == '':
                    print('EOF')
                    read_buffer = processReadBuffer(write_file,read_buffer,rule_dict,True)
                    end_of_file = True
                else:
                    read_buffer += line
                    read_buffer = processReadBuffer(write_file,read_buffer,rule_dict,False)
        print("Remaining in Read-buffer for run: " + read_buffer)
        print("Done with Iteration: " + str(counter))
        
        #read_file = write_file
        counter += 1
    file_to_process = poly_to_mutate + "-" + str(name_counter) + base_ending
    process_file_results(file_to_process)


polymer_string, translation_rules = load_inputIntoLists("02_input.txt")

print(polymer_string)
print(translation_rules)

processFile(polymer_string,translation_rules,40)


