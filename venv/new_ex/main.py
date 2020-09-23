def print_fun(numb, value):
    print("fun_", numb, " : ", value)


def fun_1(arg_1, arg_2):
    return arg_1 + arg_2


def fun_2(arg):
    return arg * 4


def fun_3(arg_1, arg_2, arg_3):
    return (arg_1 + arg_2 + arg_3) / 3


def fun_4():
    return 7


def fun_5(float_arg):
    return float_arg % 5


def fun_6(flaot_arg_1, float_arg_2):
    return {'1': flaot_arg_1, '2': float_arg_2, 'sum': flaot_arg_1 + float_arg_2}


def fun_7(dict_obj):
    return 8 in dict_obj or 4 in dict_obj


def fun_8(dict_obj_1, dict_obj_2):
    return dict_obj_1[1] / dict_obj_2[0]


def fun_9(string_obj):
    return string_obj.replace(' ', "privet")


def fun_10(string_obj):
    return string_obj.split(' ')[1]


def fun_11(list_obj):
    list_obj[0] = list_obj[3]
    return list_obj


def fun_12(dict_obj):
    dict_obj['a'] = 86
    return dict_obj


def fun_13(dict_obj):
    del dict_obj['b']
    return dict_obj


def fun_14(list_float):
    list_float[3] += 33
    return list_float


def fun_15(list_float):
    list_float.append(list_float[0] + list_float[-1])
    return list_float


def fun_16(dict_float):
    dict_float['c'] = dict_float['a'] + 45
    return dict_float


def fun_17(list_float):
    list_float[1] = list_float[0]
    return list_float


def fun_18(dict_float, float_ogj):
    del dict_float['a']
    dict_float['c'] = float_ogj
    return dict_float


def fun_19(list_float):
    return [list_float[0], list_float[-1]]


def fun_20(dict_obj):
    return [dict_obj['b'], dict_obj['m']]

def fun_21(float_obj,list_float):
    return [float_obj] + list_float

def fun_22(string_obj):
    return len(string_obj.split(' '))

def fun_23(string_obj):
    return string_obj.split(' ')[1] + ' ' + string_obj.split(' ')[0]

print_fun(1, fun_1(1, 2))
print_fun(2, fun_2(2))
print_fun(3, fun_3(2, 3, 4))
print_fun(4, fun_4())
print_fun(5, fun_5(26))
print_fun(6, fun_6(2, 3))
print_fun(7, fun_7([1, 2, 3, 8, 2]))
print_fun(8, fun_8([1, 6, 3, 4], [2, 3, 4, 5]))
print_fun(9, fun_9("1 2 3 4 5 "))
print_fun(10, fun_10("one two three"))
print_fun(11, fun_11([1, 2, 3, 4, 5]))
print_fun(12, fun_12({'a': 12, 'b': 22}))
print_fun(13, fun_13({'a': 1, 'b': 32}))
print_fun(14, fun_14([1, 2, 3, 4, 5, 6]))
print_fun(15, fun_15([1, 2, 3, 4]))
print_fun(16, fun_16({'a': 1, 'b': 2}))
print_fun(17, fun_17([1, 2, 3]))
print_fun(18, fun_18({'a': 1, 'b': 'we'}, 12))
print_fun(19, fun_19([1, 2, 3, 4]))
print_fun(20, fun_20({'a':1,'b':2,'m':3}))
print_fun(21, fun_21(0,[1,2,3]))
print_fun(22, fun_22('one two three'))
print_fun(23,fun_23('one two'))

