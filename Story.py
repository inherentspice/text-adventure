# Top 15 most common words in the psychological test:
# [like 16] [people 15] [enjoy 11] [others 9] [make 8] [it 7] [new 7] [important 6]
# [time 5] [would 5] [life 5] [things 4] [avoid 4] [work 4] [think 3]
# Now use these as basis for text-adventure

beginning = input("Would you like to explore the inner reaches of your mind? (yes/no)")
if beginning == 'Yes'.lower().strip():
    two = input('In front of you are doors to two rooms. The room on the left is full of chatting people. The room on your right is empty and has food and drinks, and a library of for you to read. Which way do you go? (left/right)')
    if two == "Left".lower().strip():
        three = input("The faces of the people shift and shimmer in the light. You recognize them. Work friends. Do you discuss managements' new policy on water bottles in the work space or the weather? (water/weather)")
        if three == "water".lower().strip():
            print('k')
        else:
            print('jk')
    elif two == "Right".lower().strip():
        three_a = input("You sit in a comfy chair. Pick up a book by Stephen Hawking. As you crack the spine, a voice whispers to you, 'Come over to the mirror.' What do you do? (ignore/follow)")
        if three_a == 'ignore'.lower().strip():
            print('m')
        else:
            print('ol')
    else:
        print('sorry')
else:
    print('You coward. Come back later.')


