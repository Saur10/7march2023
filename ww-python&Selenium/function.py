
def func_var_args(*args):
    print(args)

func_var_args(1, 2, '3')


def func_keyword_arg(**kwargs):
    print(kwargs)

func_keyword_arg(keyword1=10, keyword2='foo')



def func_var_args1(a,b,*args):
    print(" a is : " ,a)
    print(" b is : ", b)
    print(" ** args is : ", args)


func_var_args1(1,'3',6,4,5,'two')


def func_keyword_arg2(**kwargs):
    print(kwargs)

func_keyword_arg2(keyword1=10, keyword2='foo',hh='4')






