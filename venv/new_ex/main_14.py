import random


def print_fun(number, data):
    print("Fun_", number, " : ", data)


def fun_1(list_number):
    sum = 0;
    for _ in list_number:
        sum += _
    return sum


def fun_2(list_number):
    return_list = []
    for _ in list_number:
        return_list.append(_ / 2)
    return return_list


def fun_3(list_obj):
    count = 0;
    for _ in list_obj:
        count += 1
    return count


def fun_4(list_number, number):
    for _ in list_number:
        if _ == number:
            return True
    return False


def fun_5(list_number):
    sum = 0
    for _ in list_number:
        sum += _
    return sum / len(list_number)


def fun_6(list_number):
    max = list_number[0]
    for _ in list_number:
        if _ > max:
            max = _
    return max


def fun_7(list_number):
    min = list_number[0]
    for _ in list_number:
        if _ < min:
            min = _
    return min


def fun_8_9(list_numbers):
    list_chet = []
    list_nechet = []
    for _ in list_numbers:
        if _ % 2 == 0:
            list_chet.append(_)
        else:
            list_nechet.append(_)
    return [list_chet, list_nechet]


def fun_10(list_nuber_1, list_numer_2):
    list_return = []
    for _ in list_nuber_1:
        if _ in list_numer_2:
            list_return.append(_)
    return list_return


def fun_11(list_number_1, list_number_2):
    list_return = []
    for _ in list_number_1:
        if not _ in list_number_2:
            list_return.append(_)


def fun_12(numb_obj_1, numb_opj_2):
    numb_return = 1
    for _ in list(range(numb_opj_2)):
        numb_return = numb_obj_1 * numb_return
    return numb_return

    return list_return


def fun_13():
    for x in list(range(11)):
        for y in list(range(11)):
            if not x == 0 or y == 0:
                print(x, " * ", y, " = ", x * y)
    return "Complite"


def fun_14(list_number):
    for _ in list_number:
        count_prob = 3 - len(str(_))
        print(' ' * count_prob + str(_))


def fun_15():
    now_count = 0
    while True:
        x = random.randint(0, 10)
        y = random.randint(0, 10)

        print("У вас ", now_count);
        otvet = input(str(x) + " * " + str(y) + " = ")
        if otvet == "-1":
            break
        elif int(otvet) == x * y:
            now_count += 1
    return "complite"


def fun_16(list_number):
    list_return = [list_number[0], list_number[0]]
    for _ in list_number:
        if _ >= list_return[0]:
            list_return[1] = list_return[0]
            list_return[0] = _

            continue
        if _ > list_return[1] or list_return[0] == list_return[1]:
            list_return[1] = _
    return list_return


def fun_17(int_obj):
    for _ in list(range(int_obj)):
        print('*' * int_obj)
    return "Complite"


def fun_18(int_obj):
    for _ in list(range(int_obj)):
        if _ == 0 or _ == int_obj - 1:
            print('*' * int_obj)
        else:
            print('*', ' ' * (int_obj - 4), '*')
    return "Complite"


def fun_19(int_obj):
    for _ in list(range(int_obj)):
        if _ % 2 == 0:
            print("* " * int_obj)
        else:
            print(" *" * int_obj)
    return "Complite"


def fun_20(int_obj_1, int_obj_2):
    index = int_obj_1
    list_return = []
    while index <= int_obj_2:
        if index % 2 == 0:
            list_return.append(index)
        index += 1
    return list_return


def fun_21(int_obj):
    int_return = 1
    index = 1
    while index <= int_obj:
        int_return = int_return * index
        index += 1
    return int_return


def fun_22(int_sum, int_procent, int_mounth):
    for _ in list(range(int_mounth)):
        int_sum = int_sum + (int_sum * (int_procent / 100))
    return int_sum


def fun_23(int_obj):
    for _ in list(range(int_obj)):
        if _ == 0 or _ == 1:
            continue
        if int_obj % _ == 0:
            return False
    return True


def fun_24(int_obj):
    for _ in list(range(int_obj)):
        print('*' * (_ + 1))
    return "Complite"


def fun_25(int_obj):
    if int_obj % 2 != 0:
        lenth = int_obj
    else:
        lenth = int_obj + 1
    for _ in list(range(lenth)):
        if _ < (lenth - 1) / 2:
            print(' ' * int(((lenth - 1) / 2) - _ - 1), '*' * int(lenth - ((((lenth - 1) / 2) - _) * 2)))
        elif _ == (lenth - 1) / 2:
            print("*" * lenth)
        else:
            print(' ' * int((lenth / 2) - (lenth - _)), '*' * int(lenth - 1 - (((lenth) / 2 - (lenth - _)) * 2)))
    return "Complite"


print_fun(1, fun_1([1, 2, 3, 4]))
print_fun(2, fun_2([1, 2, 3, 4, 5]))
print_fun(3, fun_3([1, 2, 3, 4, 5, 6, 7]))
print_fun(4, fun_4([1, 2, 3, 4, 5], 3))
print_fun(5, fun_5([2, 3, 2, 2, 2, 2, 2]))
print_fun(6, fun_6([1, 2, 3, 4, 0, 1, 0, 22, 0, 1, 22, 3]))
print_fun(7, fun_7([2, 1, -1, 5]))
print_fun('8_9', fun_8_9([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print_fun(10, fun_10([1, 2, 3, 4, 5], [3, 4, 5, 6, 7, 88, 9]))
print_fun(11, fun_11([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 2]))
print_fun(12, fun_12(2, 3))
print_fun(13, fun_13())
print_fun(14, fun_14([1, 23, 123, 1]))
# print_fun(15,fun_15())
print_fun(16, fun_16([20, 30, 5]))
print_fun(17, fun_17(10))
print_fun(18, fun_18(5))
print_fun(19, fun_19(4))
print_fun(20, fun_20(1, 22))
print_fun(21, fun_21(4))
print_fun(22, fun_22(40, 50, 3))
print_fun(23, fun_23(29))
print_fun(24, fun_24(5))
print_fun(25, fun_25(10))
