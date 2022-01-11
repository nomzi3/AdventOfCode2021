from collections import Counter
## idea of how to solve it
"""
find the start-points - add each to 1 list
Go through the list(s). For the last item, find all matches.
    ->for each unique path, create a new list and add to backlog
    ->continue on the main path, check the next match...etc.
        ->continue until we either hit the end, or a dead end (as per rules).
    ->once main path done, continue on the backlog for the other paths, they should now be unique.

    ->once no paths left in backlog, end and return results.
"""
###Load our input - store as list containing connecting paths
#####return 2D-list
def load_inputAndSplitLineIntoTwoDArray(filename):
    fileRead_list = []
    with open(filename, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            fileRead_list.append(line)
    return_Array = []
    for line in fileRead_list:
        split_line = line.split("-")
        return_Array.append(split_line)
    return return_Array
## Find startpoints of our input
###return as a list with sorted start-points
def find_startPoints(listToCheck):
    return_list = []
    for item in listToCheck:
        if 'start' in item:
        #if item[0] == 'start' or item[1] == 'start':
            temp_list = []
            if item[0] == 'start':
                temp_list.append(item[0])
                temp_list.append(item[1])
            else:
                temp_list.append(item[1])
                temp_list.append(item[0])
            return_list.append(temp_list)
            #return_list.append(item)
    return return_list
##Find all options in listToCheck, that is connected with firstOption
####Return - list with matches
def find_nextOptionsInList(listToCheck,nextOption):
    return_list = []
    for item in listToCheck:
        if nextOption in item:
            return_list.append(item)
    return return_list
def check_ifNextOptionIsStart(listToCheck):
    #if listToCheck[len(listToCheck)-1] == 'start':
    if 'start' in listToCheck:
        #print(listToCheck)
        #print("Found start")
        return True
    return False

def check_ifLastItemFailsList(listToCheck):
    last_item_in_list = listToCheck[len(listToCheck)-1]
    if last_item_in_list.isupper():
        return False
    elif last_item_in_list.islower():
        counted_items = Counter(listToCheck)
        if counted_items[last_item_in_list] > 1:
            return True
        else:
            return False

##Main loop - will search for all paths from start to end
###Returns - nothing - will print out the result though...
def search_forAllPaths(listToCheck):
    backlog_list = []
    running_list = []
    paths_completed = []
    paths_failed = []
    running_list = find_startPoints(listToCheck)
    print("start points")
    print(running_list)
    still_Running = True
    ##run until no more paths available to explore
    while still_Running:
        run_oneMoreRun = False
        for item in running_list:
            last_item_in_item = item[len(item)-1]
            ##find all connected paths to the last element in each path
            connected_option_list = find_nextOptionsInList(twoD_Array,last_item_in_item)
            print(connected_option_list)
            
            ##for each connected item
            for next_item in connected_option_list:
                #check if next item is a start - if so ignore it
                if not check_ifNextOptionIsStart(next_item):
                    temp_list = item.copy()
                    ##might be a stupid way of doing it, but it works
                    ###appends the next item in our path to the backlog-list
                    #_>will create 1 new list per option we fetched that is legal
                    if next_item[0] == last_item_in_item:
                        temp_list.append(next_item[1])
                    elif next_item[1] == last_item_in_item:
                        temp_list.append(next_item[0])
                    backlog_list.append(temp_list)
                    
        running_list.clear()
        #backlog contains all lists that was generated throughout the run
        for item in backlog_list:
            #if the list is completed
            if 'start' in item and 'end' in item:
                paths_completed.append(item)
            #check if we entereed the same small cave twice.
            elif check_ifLastItemFailsList(item):
                paths_failed.append(item)
            
            else:
                ##if we still have unprocessed items - run one more time
                run_oneMoreRun = True
                running_list.append(item)
        backlog_list.clear()
        if not run_oneMoreRun:
            still_Running = False
    print("paths completed")
    print(paths_completed)
    print("number of completed routes__>" + str(len(paths_completed)))
    print("number of failed paths===>" + str(len(paths_failed)))
    #print("paths failed")
    #print(paths_failed)
    ##remove completed option in the backlog-list
    ####check if it contains both end and start -> add to paths_completed
    ######else - check if last item in list is small, AND, if the same letter already exists in list
    #########if not - add list to running_list

twoD_Array = load_inputAndSplitLineIntoTwoDArray("input_01.txt")
print(twoD_Array)
search_forAllPaths(twoD_Array)

#testlist2 = ['A','B','C','d','d']
#testlist1 = ['A','B','C','d','a','A','d']

#print(check_ifLastItemFailsList(testlist2))
#print(check_ifLastItemFailsList(testlist1))
#input_options = find_startPoints(twoD_Array)
#print(input_options)
#next_state = find_nextOptionInList(twoD_Array,'A')
#print(next_state)

