# Built-in Functions
print()
len('spam')

"""
Python also comes with the Standard
Library -> a set of modules that
Python is pre-installed with
- You must import the module with an
import statement
"""
# For example:
import random as r

# Random integer from 1 to 10
r.randint(1, 10)

"""
NOTE: The dot at the end of calling
the class tells Python to look for
the name of the function that 
succeeds it
"""

# You can import multiple modules
# import sys, os, math

# You can also import everything
from random import *
# and do this without calling
randint(1, 10)

"""
You can break a Python program
early-on before Python reaches
the exit of the code by using
the "sys" module
"""

# sys.exit()

"""
Modules that are installed by "pip"
are called Third-party modules ->
these are modules that do not come
with the Standard Library

pip:
- A program that is used in the
terminal to managa Python packages

In the terminal, we installed the
"pyperclip" module; a module that
allows us to copy and paste text
to and from the clipboard:
"""

import pyperclip

# How to copy this string into
# the clipboard
pyperclip.copy('Hello world!')
pyperclip.paste()