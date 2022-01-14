'''
Write a function `cat_builder(name, color, toys)` that returns a cat object
object with the corresponding properties.

Example:

cat_1 = cat_builder('Garfield', 'golden', ['scratching-post', 'yarn'])
print(cat_1) # => { name: 'Garfield', color: 'golden', toys: ['scratching-post', 'yarn'] }

cat_2 = cat_builder('Whiskers', 'rainbow', ['poptarts'])
print(cat_2) # => { name: 'Whiskers', color: 'rainbow', toys: [ 'poptarts' ] }
'''

def cat_builder(name, color, toys):
    cat_object = {"name": name, "color": color, "toys": toys}
    return cat_object

cat_1 = cat_builder('Garfield', 'golden', ['scratching-post', 'yarn'])
print(cat_1) # => { name: 'Garfield', color: 'golden', toys: ['scratching-post', 'yarn'] }

cat_2 = cat_builder('Whiskers', 'rainbow', ['poptarts'])
print(cat_2) # => { name: 'Whiskers', color: 'rainbow', toys: [ 'poptarts' ] }