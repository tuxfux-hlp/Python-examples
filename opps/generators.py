#!/usr/bin/python

# List comprehension
# iterator - memory consuming object - lesser performance.
my_values =  [value*value for value in [1,2,3,4,5]]
print my_values
print type(my_values)

# generator - not memory consuming object - more performace
my_values =  (value*value for value in [1,2,3,4,5])
print my_values
print type(my_values)


'''
def square_of_numbers(obj):
  result=[]
  for value in obj:
    result.append(value*value)
  return result

def square_of_generate(obj):
  for value in obj:
    yield value*value

my_numbers = [1,2,3,4,5]  # List of the numbers

for value in square_of_generate(my_numbers):
  print value


#print square_of_numbers(my_numbers)   # memory
m = square_of_generate(my_numbers)
print type(m)
print m.next()
print m.next()
print m.next()
print m.next()
print m.next()
print m.next()
'''
