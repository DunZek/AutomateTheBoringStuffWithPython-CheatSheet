'''
Summary:
    - A divide-by-zero error happens when Python divides a number by zero.
    - Errors cause the program to crash.
    - An error that happens inside a try block will cause code in the except block to execute. That code can handle
    the error or display a message to the user so that the program can kee going.


'''

def _ZeroDivisionError():  # Computers cannot divide by zero
    def div42by(divide_by):
        try:  # Default statement
            return 42 / divide_by
        except ZeroDivisionError:  # Do this whenever this kind of error popped up.
            print('Error: You tried to divide by zero')

    print(div42by(2))
    print(div42by(12))
    print(div42by(0))  # ZeroDivisionError: division by zero / execute exception in program.
    print(div42by(1))

def _ValueError():  # Expectations of numbers when you got strings.
    print('Wie viele Katzen hast du?')
    num_cats = input()
    try:
        if int(num_cats) >= 4:
            print('Es gibt so viele Katzen!')
        else:
            print('Es gibt nicht viele Katzen.')
    except ValueError:
        print('Du druckst keine Zahl')
