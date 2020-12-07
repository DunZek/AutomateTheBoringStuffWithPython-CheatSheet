
print('Hello')

# How to escape particular characters
print("Hello Alice's daughter")
print('Hello Alice\'s daughter')

"""
Escape characters:
\' -> Single quote
\" -> Double quote
\t -> Tab
\n -> Newline (line break)
\\ -> Backslash

Raw strings:
- Like strings, but begin with
an 'r' character 
- literally print any backslashes
in the string and ignore escape
characters
"""

print(r'Hello')
# They can include backslashes
# without having to use escape
# characters

"""
Multi-line string:
- Begins and ends with 3 quote
characters
"""
# Demonstration
print("""
This
is a valid
string statement
""")

"""
Strings are like lists, as each
character in a string correspond
to an index, as if it were a list
of characters:
"""

spam = 'Hallo Welt!'
print(spam[0:5])  # "Hallo"
print(spam[-1])  # "!"
print('Hallo' in spam)  # True
