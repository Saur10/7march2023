'''
 Decorator >>
 
Python decorators allow you to change the behavior of a function without modifying the function itself.

Basically, a decorator takes in a function, adds some functionality and returns it
'''


# def print_msg(message):
#     greet="Hello"
#
#     def printer():
#         print(greet , message)
#
#     return printer
#
# # abc=print_msg("world")
# # abc()
# @print_msg("world")
# def xw():
#     pass
# xw()

def display_info(func):

    def inner():
        print(" executing  :: ",func.__name__, " function ")
        func()
        print("executed !!!")

    return inner

# abc=display_info(printer)
# abc()
@display_info
def printer():
    print("hello world")

printer()



