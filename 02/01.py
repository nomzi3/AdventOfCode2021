##start hor_pos at 0
##start depth_pos at 0

##possible inputs:
#####forward X
#======>increase hor_pos by X
#####down X
#======>increase depth_pos by X
#####up X
#======>decrease depth_pos by X

###at end, multiply hor_pos with depth_pos




##take input from file, check if it is forward, down, or up at start of line.
###fetch value, print out action
#####repeat....

action_list = []
hor_pos = 0
depth_pos = 0

with open("input_01.txt", "r") as f:
    words = f.read().splitlines()

    for word in words:
        action_list.append(word)

print(action_list)

for x in action_list:
    split_word = x.split(' ')
    print(split_word)
    if(split_word[0] == 'forward'):
        print("FORWARD===>" + str(split_word[1]))
        hor_pos += int(split_word[1])
    elif(split_word[0] == 'down'):
        print("DOWN====>" + str(split_word[1]))
        depth_pos += int(split_word[1])
    elif(split_word[0] == 'up'):
        print("UP=====>" + str(split_word[1]))
        depth_pos -= int(split_word[1])

print("Hor_Pos===>" + str(hor_pos))
print("Depth_Pos===>" + str(depth_pos))

end_result = hor_pos * depth_pos
print("End result===>" + str(end_result))
