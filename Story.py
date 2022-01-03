# Top 15 most common words in the psychological test:
# [like 16] [people 15] [enjoy 11] [others 9] [make 8] [it 7] [new 7] [important 6]
# [time 5] [would 5] [life 5] [things 4] [avoid 4] [work 4] [think 3]
# Now use these as basis for text-adventure

'''class Tree:
    def __init__(self, val):
        if val != None:
            self.val = val
        else:
            self.val = None

        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Tree(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def printValues(self):
        if self.left:
            self.left.printValues()
        print(self.val)
        if self.right:
            self.right.printValues()

start = Tree(100)
start.left = Tree(50)
start.right = Tree(101)
start.insert(25)
start.insert(70)
'''

'''
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
    '''

'''
"Would you like to explore the inner reaches of your mind? (yes/no)"
'In front of you are doors to two rooms. The room on the left is full of chatting people. The room on your right is empty and has food and drinks, and a library of for you to read. Which way do you go? (left/right)'
The faces of the people shift and shimmer in the light. You recognize them. Work friends. Do you discuss managements' new policy on water bottles in the work space or the weather? (water/weather)
You sit in a comfy chair. Pick up a book by Stephen Hawking. As you crack the spine, a voice whispers to you, 'Come over to the mirror.' What do you do? (ignore/follow)
'''

'''
100: yes or no
50: yes => left or right
101: no => out
25: left => water or weather
70: right => voice - ignore or follow
'''
dict = {100:'Would you like to explore the inner reaches of your mind? (type 50 for yes/ type 101 for no)',
        101: 'You coward. Come back later',
        50: 'In front of you are doors to two rooms. The room on the left is full of chatting people. The room on your right is empty and has food and drinks, and a library of for you to read. Which way do you go? (type 25 for left/ type 70 for right)',
        25: 'The faces of the people shift and shimmer in the light. You recognize them. Work friends. Do you discuss managements\' new policy on water bottles in the work space or the weather? (type 2 for water bottles/type 24 for weather',
        70: 'You sit in a comfy chair. Pick up a book by Stephen Hawking. As you crack the spine, a voice whispers to you, \'Come over to the mirror.\' What do you do? (choose 97/96)',
        2: '“Jameson reamed me out on Friday,” you say. “Can’t believe they’ll only let us drink during break.” Silence falls over the group. Fingers fidget, legs shift. Finally, Max, speaks: “Yeah, well, I guess it all comes down to how important it is to you.” (type 4 for not important/ type 22 for important)',
        4: 'You laugh. “Haha.” Your laugh is not your own. It’s a stranger’s laugh, in a stranger’s life, among people whose faces you don’t care for. “I guess it doesn’t matter.” You look down at your watch. “Jeez, look at the time!” (type 6 for go home to partner/ type 20 for go to bar)',
        6: 'Bed envelops you. Partner has eyes, face. Recognizable, comfortable. They are warm. You are warm with them. You are safe.'}


try:
    beginning = int(input(dict[100]))
    assert beginning == 50 or beginning == 101
except:
    print("please type 50 for yes and 101 for no")



def proceed(beginning, value1,value2):
    try:
        if int(beginning) == value1:
            result = int(input(dict[value1]))
            beginning = result
            return result
            
        elif int(beginning) == value2:
            result = int(input(dict[value2]))
            beginning = result
            return result
        assert int(beginning) == value1 or int(beginning) == value2
    except AssertionError:
        print('please put in only either '+str(value1)+' or ' + str(value2))

beginning = proceed(beginning,50,101)
beginning = proceed(beginning,25,70)
beginning = proceed(beginning,2,24)
beginning = proceed(beginning,4,22)








