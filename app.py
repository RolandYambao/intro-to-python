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
# conditional --> this first item that represents
# True, it runs that indented [block]

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

print("eggs" in "green eggs and ham")

food = "eggs"
print(food in "green eggs and ham")
print(len(food)) #4

statement = "my code rules"[3:9]
print(statement)

if 7 == 7:
    print('This is 7')
else:
    print('This is the second condition')

if 7 != 6:
    print('We are not the same')
else:
    print('This is the second condition')

if not 7:
    print('This is 7')
else:
    print('This is the second condition')

arr = [1, "two", 3, "four", True, False, "hello"]
print(arr[1])
print(arr[-1])

one_through_ten = list(range(10))
print(one_through_ten)

three_through_ten = list(range(3, 10))
print(three_through_ten)

a = [1, 23, 12, 99, 82]
a.sort()
print(a)

a.append(88)
print('After adding 88', a)

a.insert(1, 77)
print('After inserting 77 at index 1', a)

if 33 in a:
    print('This Michael Jordan number!')
else:
    print('Not in there...')

print('Is 7 a digit???', '7'.isdigit())

cat = {
  "name": 'Hamlet',
  "breed": 'American Shorthair',
  "fav_food": 'Prosciutto'
}

cat["name"] = "Garfield"
# 'Hamlet'

print('Do not feed to cat...', cat["fav_food"])
# 'Prosciutto'

print('this is  my cat breed', cat.get("breed"))
print(cat.get("name"))
cat["age"] = 3
print(cat.get("age"))
# help(dict)

print('ITEMS', cat.items())
print('KEYS', cat.keys())

cat_keys = list(cat.keys())
print(cat_keys)

# # String Interpolation
# state = "Washington State"
# year = 1889
# n = 42
# my_message = f"{state} was the {n}th state to join the union in {year}."
# print(my_message)

# # 2
# location = "California"
# number = 6
# my_second_message = f"{location} is the {number}th largest economy in the world."
# print(my_second_message)

# # 3
# topic = 'Inflation'
# num = 7
# y = 1982
# my_third_message = "{} is at {} percent. Highest since {}".format(topic, num, y)
# print(my_third_message)

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}{st_nd_rd_th(n)} state to join the union in {year}."
print(my_message)