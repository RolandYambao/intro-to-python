'''
Write a function `adults(people)` that takes in an array of person
objects. The function should return an array containing the names of
those who have an age of 18 or higher.

Example:

ppl = [
  {'name': 'Khalid Robinson', 'age': 22},
  {'name': 'Ariel Winter', 'age': 20},
  {'name': 'Post Malone', 'age': 25},
  {'name': 'Willow Smith', 'age': 17}
]

print(adults(ppl)); # => [ 'Khalid Robinson', 'Post Malone' ]
'''

def adults(people):
  legal_adult = []
  for i in range(0,len(people)):
    if (people[i]['age'] >= 18):
      legal_adult.append(people[i]['name'])
  return legal_adult

ppl = [
  {'name': 'Khalid Robinson', 'age': 22},
  {'name': 'Ariel Winter', 'age': 20},
  {'name': 'Post Malone', 'age': 25},
  {'name': 'Willow Smith', 'age': 17}
]

print(adults(ppl)); # => [ 'Khalid Robinson', 'Post Malone' ]