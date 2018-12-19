from functools import reduce


def sort(list_in):
    list_out = list_in
    index = 0
    chek = 0
    while True:
        if list_out[index] > list_out[index + 1]:
            list_out[index], list_out[index + 1] = list_out[index + 1], list_in[index]
            chek = 1
        index += 1
        if index == len(list_out) - 1 and chek == 0:
            break
        elif index == len(list_out) - 1 and chek == 1:
            index = 0
            chek = 0
    return list_out


def calc_max():
    number_list = []
    while True:
        try:
            item = (input("Введите число либо нажите Enter для завершения ввода :"))
            number_list.append(float(item))
        except ValueError:
            if item == "":
                break
            else:
                print("Не соответствует формату Float")

    print("Числа:", number_list, "\nКоличество:", len(number_list), "\nСумма:",
          reduce(lambda x, y: x + y, number_list, 0))
    number_list = sort(number_list)
    if len(number_list) % 2 == 0:
        mediana = (number_list[int(len(number_list) / 2) - 1] + number_list[int(len(number_list) / 2)]) / 2
    else:
        mediana = number_list[int(len(number_list) / 2)]
    print("Наименшее:", number_list[0])
    print("Набольшее:", number_list[len(number_list) - 1])
    print("\nСреднее", reduce(lambda x, y: x + y, number_list, 0) / len(number_list))
    print("Медиана", mediana)
