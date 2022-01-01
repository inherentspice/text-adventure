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
        101: 'You coward. COme back later',
        50: 'In front of you are doors to two rooms. The room on the left is full of chatting people. The room on your right is empty and has food and drinks, and a library of for you to read. Which way do you go? (type 25 for left/ type 70 for right)',
        25: 'The faces of the people shift and shimmer in the light. You recognize them. Work friends. Do you discuss managements\' new policy on water bottles in the work space or the weather? (water/weather)',
        70: 'You sit in a comfy chair. Pick up a book by Stephen Hawking. As you crack the spine, a voice whispers to you, \'Come over to the mirror.\' What do you do? (ignore/follow)' }


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
        print('please put in only either '+value1+' or '+value2)

beginning = proceed(beginning,50,101)
proceed(beginning,25,70)









