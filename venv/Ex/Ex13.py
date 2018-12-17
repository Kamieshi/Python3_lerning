import random

print("Exersice 1")
def Fun1(value):
    if(value <= 34):
        print("Dim")
    else:
        print("Nat")

Fun1(40)

print("Exersice 2")
def Fun2(value1,value2):
    if(value1+value2==5):
        return (value2+value1)/2
    else:
        return value2+value1

print(Fun2(2,2))

print("Exersice 3")
def Fun3(string):
    if(len(string)<5):
        print(string)
    else:
        print("строка сильно большая, я устал")

Fun3("123467")

print("Exersice 4")
def Fun4():
    value1=float(input("Ввудите первое число: "))
    value2=float(input("Введите второе число: "))
    if(value1>value2):
        print(value2+value1)
    else:
        print(value1*value2)

Fun4()

print("Exersice 5")
def Fun5():
    value1=random.randint(1,10);
    value2=random.randint(1,10);
    print(value1," * ",value2," = ")
    value3=int(input())
    if(value2*value1==value3):
        print("Верно")
    else:
        print("Неверно")

Fun5()

print("Exersice 6")
def Fun6():
    print("Столица РБ:")
    print("a: Бульбасти")
    print("b: Лондон")
    print("c: Минск")
    valueIn=input("Ответ: ")
    if(valueIn=="c" or valueIn=="с"):
        print("Верно")
    else:
        print("Невнрно")

print("Exersice 7")
def Fun7(string):
    print(string)
    valueIn=input("Какое слово заменить? ")
    valueOut=input("Каким? ")
    print(string.replace(valueIn,valueOut))

Fun7("123456789")

print("Exersice 8")
def Fun8(name):
    if(name=="Вася" or name=="Петя"):
        print("Привет братаны")
    else:
        if(name=="Толик"):
            print("поделись на нолик")

Fun8(input("Введите имя :"))

print("Exersice 9")
def Fun9(color1,color2,value):
    if(color1=="черный" and color2=="синий"):
        print("мне не нравиться ", value+45)
    else:
        if(color1=="зеленый" or color2=="зеленый" or color1=="красный" or color2=="красный"):
            print("Красиво ", value -7)

Fun9("черный","синий",45)