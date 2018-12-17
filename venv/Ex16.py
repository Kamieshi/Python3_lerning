from functools import reduce

print("Exersice 1")


def Fun1(value):
    if value > 100:
        return value * 2
    else:
        return value / 3


def Fun1_1(listIn):
    return list(map(Fun1, listIn))


print(Fun1_1([33, 99, 100, 200]))

print("Exersice 2")


def Fun2(value):
    return value % 2 == 0


def Fun2_2(listIn):
    return list(filter(Fun2, listIn))


print(Fun2_2([1, 2, 3, 4, 5, 6, 6]))

print("Exersice 3")


def Fun3(valueOne, valueTwo):
    if valueOne > valueTwo:
        return valueOne
    else:
        return valueTwo


def Fun3_3(listIn):
    from functools import reduce
    return int(reduce(Fun3, listIn))


print(Fun3_3([2, 3, 1, 4, 21, 23, 0, 1, 2]))

print("Exersice 4")


def Fun4(velue):
    return "Привет " + velue


def Fun4_4(listIn):
    return list(map(Fun4, listIn))


print(Fun4_4(["Петя", "Вася", "Катя"]))

print("Exersice 5")


def Fun5(velue):
    return len(velue) < 5


def Fun5_5(listIn):
    return list(filter(Fun5, listIn))


print(Fun5_5(["Petr", "Maria", "Yan", "Dmitry"]))

print("Exersice 6 ????????????????????/")


def Fun6(x):
    return x + 10


def Fun6_6(Fun, x, z):
    return Fun(x) * z


print(Fun6_6(Fun6, 1, 3))

print("Exersice 7")


def Fun7(velueOne, velueTwo):
    return velueOne + velueTwo


def Fun7_7(strIn):
    listOut = strIn.split(" ")
    listOut = list(map(lambda x: x + " ", listOut))
    from functools import reduce
    return str(reduce(Fun7, listOut, "Когда то "))


print(Fun7_7("все мы были молоды"))
