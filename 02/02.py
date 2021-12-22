## down X increases your aim by X units.
##    up X decreases your aim by X units.
##    forward X does two things:
##        It increases your horizontal position by X units.
##        It increases your depth by your aim multiplied by X.

action_list = []
aim = 0
hor_pos = 0
depth_pos = 0
with open("input_02.txt", "r") as f:
    words = f.read().splitlines()

    for word in words:
        action_list.append(word)

for x in action_list:
    split_word = x.split(' ')
    print(split_word)
    if(split_word[0] == 'forward'):
        hor_pos += int(split_word[1])
        print("FORWARD===>" + str(split_word[1]))
        depth_pos += int(split_word[1]) * aim
        print("Aim==>" + str(aim) + " new depth==>" + str(depth_pos))
    elif(split_word[0] == 'down'):
        print("DOWN====>" + str(split_word[1]))
        aim += int(split_word[1])
        print("New AIM==>" + str(aim))
    elif(split_word[0] == 'up'):
        print("UP=====>" + str(split_word[1]))
        aim -= int(split_word[1])
        print("New AIM==>" + str(aim))

print("Hor_Pos===>" + str(hor_pos))
print("Depth_Pos===>" + str(depth_pos))

end_result = hor_pos * depth_pos
print("End result===>" + str(end_result))
"""

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

"""