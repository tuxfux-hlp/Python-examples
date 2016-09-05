#!/usr/bin/python
'''
Write a program to count the characters in a string to print output as expected below.
Example: If the input string is aabbbccdeff the expected output is a2b3c2def2.
'''

final_output=[]
my_string = raw_input("please enter the string:")

# spliting the string to a list to read each character one by one.
my_string_split = list(my_string)

# we are walking over each element and counting it. 
for alp in my_string_split:
  count = str(my_string_split.count(alp))  # count function in list and convert to str
  final_output.append(alp)                 # appending the alp to the final_output list
  final_output.append(count)               # appending the count to the final_output list
  while alp in my_string_split:            # searching for the alp on the given string
    my_string_split.remove(alp)           #  remove it where ever we find it.
  count = 0

print final_output
print "".join(final_output)               # converting the list to the string and hence our output


'''
Output of the program

key2gyaan@key2gyaan ~/Documents/git_repositories/tuxfux-hlp/python-examples/questions $ python 01-program.py 
please enter the string:aabbbccdeff
['a', '2', 'b', '3', 'd', '1', 'f', '2']
a2b3d1f2
'''
