"""
NOTE: Python programs are just
text files with the .py extension.

NOTE: Python executes from top to
bottom. Along the way, Python ignores
comments and blank lines

This program says hello and asks
for my name:
"""

# Call the print function,
# our argument is 'Hello world!'
print('Hello world!')

print('What is your name?')
# Python waits for the user to type
my_name = input()
print('It is good to meet you, '
      + my_name)
print('The length of your name is:')
print(len(my_name))  # "length()"

print('What is your age?')
my_age = input()
print('You will be ' + str(int(
    my_age) + 1) + ' in a year.')

"""
str(), int(), and float() return
their respective values -> They
convert between data types
"""
