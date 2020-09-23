from functools import reduce
import math


def add_print(fn):
    def wripper(*arg):
        print("input ", arg)
        print("output", fn(*arg))

    return wripper

def capitolize_wrapper(fn):
    def wrapper(*input_obj):
        return_obj = fn(*input_obj).capitalize()
        return return_obj
    return wrapper

def fun_2_wripper(fn):
    def wripper(*input_obj):
        result = fn(*input_obj)
        result = fn(result)
        return result
    return wripper

@fun_2_wripper
def fun_2(list_obj):
    result=[]
    for _ in list_obj:
        result.append(_*2)
    return result

def fun_3_wrapper(fn):
    def wraooer(input_obj):
        if input_obj <0:

            return "<0"
        else:
            return fn(input_obj)
    return wraooer


@fun_3_wrapper
def fun_3(long_int_obj):
    return math.sqrt(long_int_obj)

@add_print
def sum(*int_number):
    return reduce(lambda x, y: x + y, int_number, 0)

@capitolize_wrapper
def fun_1(str_obj):
    temp = str_obj.split(' ')
    return temp[1] + ' ' + temp[0]


print(fun_3(-1))

print(list(filter(lambda x:x%2==0,[1,2,3,4])))
