'''
Write a function odd_range(end) that takes in a number and returns an array 
containing all positive odd numbers up to `end`.

Examples:

print(odd_range(13)) # => [ 1, 3, 5, 7, 9, 11, 13 ]
print(odd_range(6)) # => [ 1, 3, 5 ]
''' 

def odd_range(end):
    odd_array = []
    for i in range(0, end):
        if (i % 2 != 0 and i > 0):
            odd_array.append(i)
    return odd_array; 

print(odd_range(13))
print(odd_range(6))