import random
def print_fun(int_obj, out_obj):
    print("Obj_", int_obj, " : ", out_obj)


def fun_1(number_obj):
    try:
        if number_obj <= 34:
            print("<=34")
        else:
            print(">34")
    except Exception as exeption:
        print("Only numbers")
    return "Complite"


def fun_1_2(number_obj):
    if not isinstance(number_obj, int):
        raise Exception("number_obj : only number")
    else:
        if number_obj <= 34:
            print("<=34")
        else:
            print(">34")
    return "Complite"


def fun_2(number_obj_1, number_obj_2):
    try:
        if number_obj_2 + number_obj_1 == 5:
            return (number_obj_1 + number_obj_2) / 2
        else:
            return number_obj_2 + number_obj_1
    except Exception as exeption:
        print("Only number")
    return "complite"

def fun_14_1(list_number):
    sum =0
    for _ in list_number:
        try:
            sum += _
        except Exception as exeption:
            continue
    return sum

print_fun(1, fun_1('1'))
print_fun("1_1", fun_1_2(2))
print_fun(2,fun_2(2,'3'))
print_fun("14_1",fun_14_1([1,2,3,4,2,6]))
