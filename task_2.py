# 1
idx = 'abcde'.index('D') # Impossible
idx = idx + 11
print(idx) 
idx * 2
print(idx)

# 2
num = 33
is_even = num % 2 == 0
print(is_even) # False
print(not is_even) # True

# 3
str_1 = 'marker'
num = len('whiteboard') - len(str_1)
print(num) # 4
str_2 = 'bootcamp'
print(str_2[num].upper()) # C
char = str_2[num].lower() # c
print(char + '!') # c!

# 4
sentence = 'welcome to bootcamp prep'
last_char  = sentence[len(sentence) - 1]
print(last_char) # p
print(sentence.index(last_char)) # 18