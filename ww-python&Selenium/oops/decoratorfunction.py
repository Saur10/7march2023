
# Decorator function

def add(x):
    return x+1

def fun(funct,a):
    result=funct(a)
    return result

aa=fun(add,3)
print(aa)



















#
# def my_decorator_func(func):
#
#     def wrapper_func():
#         # Do something before the function.
#         func()
#         # Do something after the function.
#     return wrapper_func
#
#
# @my_decorator_func
# def my_func():
#
#     pass
#
#
#
# def my_fun(a):
#     print("decorator function")
#
# @my_fun
# def ch_f():
#     pass
#
#
# # # Python program to illustrate functions
# # # can be treated as objects
# # def shout(text):
# #     return text.upper()
# #
# #
# # print(shout('Hello'))
# #
# # yell = shout
# #
# # print(yell('Hello'))
