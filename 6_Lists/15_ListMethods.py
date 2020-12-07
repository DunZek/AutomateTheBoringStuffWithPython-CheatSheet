"""
Lesson 15. List Methods

index()
append()
insert()
remove()
sort()

"""

# Methods are functions that belong to certain objects. They cannot be called on their own
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')  # Returns the index position if the argument exists. Otherwise it will raise an exception.

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')  # Returns the index position of the first object.
