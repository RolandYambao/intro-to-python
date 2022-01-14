'''
Write a function tripler(array) that takes in an array and returns a new array
containing 3 times every element of the original array.

Examples:

print(tripler([1,2,3])) # => [ 3, 6, 9 ]
print(tripler([4,1,7])) # => [ 12, 3, 21 ]
'''

def tripler(arr):
    result = []

    for num in arr:
        result.append(num * 3)

    return result

print(tripler([1,2,3]))
print(tripler([4,1,7]))