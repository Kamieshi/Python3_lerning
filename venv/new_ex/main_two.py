import random
def print_fun(number, print_return):
    print("Fun ", number, " : ", print_return)


def fun_1():
    if int(input("Year: ")) <= 34:
        print("<34")
    else:
        print(">34")


def fun_2():
    num_1 = int(input("Num_1 : "))
    num_2 = int(input("Num_2 : "))
    if num_1 + num_2 == 5:
        return float((num_1 + num_2) / 5)
    else:
        return num_2 + num_1


def fun_3():
    strint_obj = input("String : ")
    if len(strint_obj) > 5:
        return ">5"
    else:
        return "<5"


def fun_4():
    number_1 = int(input("num_1 : "))
    number_2 = int(input("num_2 : "))
    if number_1 > number_2:
        return number_1+ number_2
    else:
        return number_1*number_2

def fun_5():
    int_obj_1 = random.randint(1,10);
    int_obj_2 = random.randint(1,10);
    otvet = float(input(str(int_obj_1) + " * " + str(int_obj_2) + " = "))
    return otvet == int_obj_1*int_obj_2;

def fun_6():
    print("a. Bobr")
    print('b. minsk')
    otver = input("Столица рб : ")
    return otver=='b'

def fun_7(string_obj):
    print(string_obj)
    new =string_obj.replace(input("Какое слово заменить?: "),input("Каким словом заменить : "))
    return new


def fun_8():
    list_name_true = ['Вася','Петя']
    list_name_false = ['Толик']
    name = input("Имя : ")
    if name in list_name_true:
        print("hi")
    elif name in list_name_false:
        print("tolyk")
    else:
        print('naher pshol')

def fun_9():
    string_obj = input("Введите дату : ")
    day = int(string_obj.split('.')[0])
    mounth = int(string_obj.split('.')[1])
    year =  int(string_obj.split('.')[2])
    print(day,' ',mounth,' ',year)
    dict_lenth_mounth = {'1':31,'2':28,'3':31,'4':30,
                         '5':31,'6':30,'7':31,'8':31,
                         '9':30,'10':31,'11':30,'12':31}
    return day >0 and day<= dict_lenth_mounth[str(mounth)] and mounth > 0 and mounth <=12 and year>0 and year<9999


print_fun(9, fun_9())