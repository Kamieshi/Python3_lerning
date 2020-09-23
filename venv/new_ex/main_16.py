from functools import reduce


def print_fun(int_obj, out_obj):
    print("Obj_", int_obj, " : ", out_obj)


def fun_1(list_number):
    def fun(number_obj):
        if number_obj > 100:
            return number_obj * 2
        else:
            return number_obj / 3

    return list(map(fun, list_number))


def fun_2(list_number):
    def fun(number):
        return number % 2 == 0

    return list(filter(fun, list_number))


def fun_3(list_number):
    def fun(number_obj_1, number_obj_2):
        return number_obj_1 + number_obj_2

    return reduce(fun, list_number, 0)


def fun_4_map(fn, list_obj):
    list_return = []
    for _ in list_obj:
        list_return.append(fn(_))
    return list_return


def fun_sum_one(number_obj_1):
    return number_obj_1 + 1


def fun_chet(number_obj):
    return number_obj % 2 == 0


def fun_5_filter(fn, list_obj):
    list_return = []
    for _ in list_obj:
        if fn(_):
            list_return.append(_)
    return list_return


def fun_kvadrat(number_obj):
    print(number_obj)



def fun_6(fn, number_obj_1, number_obj_2):

    for _ in list(range(number_obj_2)):
        fn(number_obj_1)
    return "Complite"

def fun_7(list_number):

    def fun(max_obj,now_obj):
        if max_obj < now_obj:
            return now_obj
        else:
            return max_obj

    return reduce(fun,list_number,list_number[0])

def fun_8_reduce(fun,list_obj,start_obj):
    return_obj = start_obj
    for _ in list_obj:
        return_obj = fun(return_obj,_)
    return return_obj

def fun_summ(number_obj_1,number_obj_2):
    return number_obj_1 + number_obj_2

print_fun(1, fun_1([101, 99]))
print_fun(2, fun_2([1, 2, 3, 4, 5]))
print_fun(3, fun_3([1, 2, 3]))
print_fun(4, fun_4_map(fun_sum_one, [1, 2, 3]))
print_fun(5, fun_5_filter(fun_chet, [1, 2, 3, 4, 5, 6]))
print_fun(6, fun_6(fun_kvadrat, 10, 2))
print_fun(7,fun_7([1,5,2,10,3]))
print_fun(8,fun_8_reduce(fun_summ,[1,2,3],0))
