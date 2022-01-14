'''
Write a function `does_key_exist(obj, key)` that takes in an object and a
key and returns true if the key is inside the object and false if the
key is not inside the object.

Examples:

obj_1 = {'company': 'General Assembly', 'course': 'Software Engineering Immersive'}
print(does_key_exist(obj_1, 'company')) # => True
print(does_key_exist(obj_1, 'name')) # => False
'''

def does_key_exist(obj, key):
    for thing in obj:
        if key in obj:
            return True
        else:
            return False

obj_1 = {'company': 'General Assembly', 'course': 'Software Engineering Immersive'}
print(does_key_exist(obj_1, 'company')) # => True
print(does_key_exist(obj_1, 'name')) # => False