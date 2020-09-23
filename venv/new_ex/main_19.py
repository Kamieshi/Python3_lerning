from functools import reduce


def fun(a, b):
    return a * b


def print_fun(fun, value):
    print(fun.__name__, " : ", value)


def fun_1(*tuple_obj):
    return reduce(lambda x, y: x + y, tuple_obj, 0)


def fun_2(**dict_obj):
    return reduce(lambda x, y: x * y, dict_obj.values(), 1)


def fun_3(list_number, **default_dict):
    new_list = list_number + list(map(lambda x: x, default_dict.values()))
    return reduce(lambda x, y: x * y, new_list, 1)


def fun_4(*tuple_obj, default_number_1=2, deault_number_2=3):
    return_list = list(tuple_obj) + [default_number_1, deault_number_2]
    return reduce(lambda x, y: x * y, return_list, 1)

def fun_5(*tuple_obj,**dict_obj):
    new_list = list(tuple_obj) + list(dict_obj.values())
    return reduce(lambda x,y:x+y,new_list,0)
print_fun(fun_1, fun_1(1, 2, 3, 4))
print_fun(fun_2, fun_2(one=1, two=2, three=3, fore=4))
print_fun(fun_3, fun_3([10, 2, 2], dwa=2))
print_fun(fun_4, fun_4(2, 3, 4, default_number_1=4))
print_fun(fun_5,fun_5(1,2,3,fore=4,five=5))

required_args = (1,2,3)
default_arg = {'a':4,'b':5}
print_fun(fun_5,fun_5(*required_args,**default_arg))
