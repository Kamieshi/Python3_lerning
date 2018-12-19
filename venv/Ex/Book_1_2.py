from functools import reduce

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
    number_list.sort()
    print("Наименшее:", number_list[0])
    print("Набольшее:", number_list[len(number_list) - 1])
    print("\nСреднее", reduce(lambda x, y: x + y, number_list, 0) / len(number_list))
