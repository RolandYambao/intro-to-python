# this is a comment

from pickle import TRUE


def add(num, num2):
    '''
    this is suppose to add 2 numbers
    '''

name = "Johnny" 

nothing = None

is_working = True
car_off = False

if nothing:
    print('This is true')
    num = 7
    print('car is off')
elif car_off:
    print('this is the second condition')
    print('this will run if car_off is True')
elif is_working:
    print('This is working')
else:
    print('This is not true...')

# this is another conditional
if is_working:
    print('This is working also')

print(15 / 6)
print(15 // 6)

print("ace of spades".split(" "))
# => ["ace", "of", "spades"]

print("ace-of-spades".split("-"))
# => ["ace", "of", "spades"]

print("ace.of.spades".split("."))
# => ["ace", "of", "spades"]

my_scare = "boo"
my_scare.upper()

# conditional --> this first item that represents
# True, it runs that indented [block]