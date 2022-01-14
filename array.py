# map
print('---- map ----')

numbers = [1, 2, 3, 4]
def double_number(num):
    return num + num

result = map(double_number, numbers)
print('before', result)
print('after making it a list', list(result))

result2 = map(lambda x: x + x, numbers)
print('result two --> list', list(result2))

result3 = map(lambda y: y * y, numbers)
print('result three --> list', list(result3))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result4 = map(lambda x, y: x + y, numbers1, numbers2)
print('result four --> list', list(result4))

#####################################################################################################
def triple_number(num):
    return num + num + num

triple_result = map(triple_number, numbers)
print('TRIPLE', list(triple_result))

triple_result2 = map(lambda x: x + x + x, numbers)
print('TRIPLE result two --> list', list(triple_result2))

triple_result3 = map(lambda y: y * y * y, numbers)
print('TRIPLE result three --> list', list(triple_result3))

triple_numbers1 = [1, 2, 3]
triple_numbers2 = [4, 5, 6]
triple_numbers3 = [7, 8, 9]
  
triple_result4 = map(lambda x, y, z: x + y + z , triple_numbers1, triple_numbers2, triple_numbers3)
print('TRIPLE result four --> list', list(triple_result4))
#####################################################################################################

# help(filter)
print('---- filter ----')

ages = [23, 17, 21, 20, 19, 34, 40, 41, 22, 25, 27]

young_folks = list(filter(lambda person_age: person_age < 21, ages))
print('Young Folks', young_folks)

grown_folks = list(filter(lambda person_age: person_age >= 21, ages))
print('Grown Folks', grown_folks)

def is_not_21(person_age):
    if person_age < 21:
        return True
    else:
        return False

def is_21(person_age):
    if person_age >= 21:
        return True
    else:
        return False

young_people = list(filter(is_not_21, ages))
print('Young People', young_people)

grown_people = list(filter(is_21, ages))
print('Grown People', grown_people)

# a list contains both even and odd numbers. 
seq = [0, 1, 2, 3, 5, 8, 13]
  
# result contains odd numbers of the list
result5 = filter(lambda x: x % 2 != 0, seq)
# print(list(result5)) # [1, 3, 5, 13]
  
# result contains even numbers of the list
result6 = filter(lambda x: x % 2 == 0, seq)
# print(list(result6)) # [0, 2, 8]