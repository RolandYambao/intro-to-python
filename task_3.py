# 5
age = 25
if (age > 30):
    print('older than 30')
else:
    print('younger than 30') # younger than 30

# 6
str = 'food'
if (len(str) > 10):
    print('long string')
else:
    print('short string') # short string
if (str[0] == 'p'):
    print('starts with p')

# 7
num = 21
if (num % 3 == 0):
    print('divisible by 3') # divisible by 3
elif (num % 5 == 0):
    print('divisible by 5')

# 8
num = 12
if (num % 3 == 0):
    print('divisible by 3') # divisible by 3
if (num % 5 == 0):
    print('divisible by 5')

# 9
str = 'Assembly General'
if (str[0] == str[0].upper()):
    print('starts with a capital!'); # starts with a capital!
if (str[len(str) - 1] == str[len(str) - 1].upper()):
    print('ends with a capital!')

# 10
num = 25
if (num > 0):
    print('positive'); # positive
elif (num < 0):
    print('negative')
else:
    print(0)
if (num % 2 == 0):
    print('even"')
else:
    print('odd'); # odd
