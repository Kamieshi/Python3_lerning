print("Exersice 13.1")


def Fun1(value):
    if isinstance(value, int):
        if value <= 34:
            print("Дмитрий")
        else:
            print("Наталья")
    else:
        raise Exception("Only Number")


Fun1(2)

print("Exersice 13.2")


def Fun2(valueOne, valueTwo):
    if isinstance(valueOne, int) and isinstance(valueTwo, int):
        if valueOne + valueTwo == 5:
            return (valueTwo + valueOne) / 2
        else:
            return valueOne + valueTwo
    else:
        raise Exception("Only Number")


print(Fun2(2, 4))

print("Exersice 13.3")


def Fun3(stringIn):
    if isinstance(stringIn, str):
        if len(stringIn) < 5:
            print(stringIn)
        else:
            print("Very Long String In")
    else:
        raise Exception("Only string type")


Fun3("123")

import random

print("Exersice 13.5")


def Fun4(valueOne, valueTwo):
    stringForPrint = str(valueOne) + " * " + str(valueTwo) + " = "
    try:
        valueIn = int(input(stringForPrint))
        if valueIn != valueTwo * valueOne:
            print("Подумай!")
            raise Exception("")
        else:
            print("Ok")
            return True
    except Exception as e:
        Fun4(valueOne, valueTwo)


# Fun4(random.randint(1,11),random.randint(1,11))

print("Exeption 13.8")


def Fun5(stringIn):
    if stringIn == "Вася" or stringIn == "Толик" or stringIn == "Петя":
        if stringIn == "Вася" or stringIn == "Петя":
            print("Hi", stringIn)
        else:
            print("Пожелиьс на нолик", stringIn)
    else:
        raise Exception("Я тебя не знаю")


Fun5("Толик")
print("Exersice 14.1")


def Fun6(listNumersIn):
    sum = 0
    try:
        for item in listNumersIn:
            sum += item
    except Exception as e:
        sum = 0
        for item in listNumersIn:
            if isinstance(item, int):
                sum += item
    return sum


print(Fun6([1, 2, 3, "3", 6]))

print("Exersice 14.5")


def Fun7(listNumersIn):
    sum = 0
    try:
        if len(listNumersIn) == 0:
            raise Exception("")
        else:
            for item in listNumersIn:
                sum += item
            return sum
    except Exception as e:
        return " не могу посчитать пустой список"


print(Fun7([]))

print("Exersice 14.6")


def Fun8(listNumersIn):
    maxNumberInListIn = 0
    try:
        if len(listNumersIn) == 0:
            raise Exception("")
        else:
            for item in listNumersIn:
                if item > maxNumberInListIn:
                    maxNumberInListIn = item

            return maxNumberInListIn
    except Exception as e:
        return " не могу посчитать пустой список"


print(Fun8([]))

print("Exersice 14.8")


def Fun9(listIn):
    listOut = []
    try:
        for item in listIn:
            if item % 2 == 0:
                listOut.append(item)
    except Exception as e:
        listOut = []
        for item in listIn:
            if isinstance(item, int) and item % 2 == 0:
                listOut.append(item)
    return listOut


def Fun9_9(listIn):
    listOut = []
    for item in listIn:
        try:
            if item % 2 == 0:
                listOut.append(item)
        except Exception as e:
            print("Пропуск", item)
    return listOut


print(Fun9([1, 2, 3, 4, 5, 6, 6, 6, 6, "8", "qwe", 4]))
print(Fun9_9([1, 2, 3, 4, 5, 6, 6, 6, 6, "8", "qwe", 4]))
