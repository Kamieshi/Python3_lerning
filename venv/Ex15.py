print("Exersice 1")


def Fun1(List):
    sum = 0
    index = 0
    while index < len(List):
        sum += List[index]
        index += 1
    return sum


print(Fun1([1, 2, 3]))

print("Exersice 2")


def Fun2(List):
    ListOut = []
    index = 0
    while index < len(List):
        ListOut.append(List[index] / 2)
        index += 1
    return ListOut


print(Fun2([2, 4, 6]))

print("Exersice 4")


def Fun4(ListFirst, value):
    rec = False
    index = 0
    while index < len(ListFirst):
        if ListFirst[index] == value:
            rec = True
            break
        index += 1
    return rec


print(Fun4([1, 2, 3, 4, 5], 6))

print("Exersice 5")


def Fun5(listIn):
    sr = 0;
    index = 0
    while index < len(listIn):
        sr += listIn[index]
        index += 1
    return sr / len(listIn)


print(Fun5([2, 2, 2, 2, 3]))

print("Exersice 6")


def Fun6(listIn):
    maxValue = listIn[0]
    index = 0
    while index < len(listIn):
        if maxValue < listIn[index]:
            maxValue = listIn[index]
        index += 1
    return maxValue


print(Fun6([1, 2, 3, 6, 3, 2]))

print("Exersice 7")


def Fun7(listIn):
    minValue = listIn[0]
    index = 0
    while index < len(listIn):
        if minValue > listIn[index]:
            minValue = listIn[index]
        index += 1
    return minValue


print(Fun7([2, 3, 1, 3, 4]))

print("Exersice 8")


def Fun8(listIn):
    listOut = []
    index = 0
    while index < len((listIn)):
        if listIn[index] % 2 == 0:
            listOut.append(listIn[index])
        index += 1
    return listOut


print(Fun8([1, 2, 3, 4, 5, 5]))

print("Exersice 9")


def Fun9(listIn):
    listOut = []
    index = 0
    while index < len((listIn)):
        if listIn[index] % 2 != 0:
            listOut.append(listIn[index])
        index += 1
    return listOut


print(Fun9([1, 2, 3, 4, 5, 5]))

print("Exersice 10")


def Fun10(listInOne, listInTwo):
    listOut = []
    indexForListOne = 0
    indexForListTwo = 0
    while indexForListOne < len(listInOne):
        while indexForListTwo < len(listInTwo):
            if listInOne[indexForListOne] == listInTwo[indexForListTwo]:
                listOut.append(listInOne[indexForListOne])
            indexForListTwo += 1
        indexForListTwo = 0
        indexForListOne += 1
    return listOut


print(Fun10([1, 2, 3, 4], [3, 4, 5, 6, 1]))

print("Exersice 11_1")


def Fun11_1(listInOne, listInTwo):
    listOut = []
    indexForListInOne = 0
    while indexForListInOne < len(listInOne):
        if listInOne[indexForListInOne] in listInTwo:
            indexForListInOne += 1
        else:
            listOut.append(listInOne[indexForListInOne])
            indexForListInOne += 1
    return listOut


print(Fun11_1([1, 2, 3, 4, 5], [2, 3]))

print("Exersice 11_2")


def Fun11_2(valueOne, valueTwo):
    index = 0
    rec = 0
    while index < valueTwo:
        rec += valueOne
        index += 1
    return rec


print(Fun11_2(8, 2))

print("Exersice 12")


def Fun12(valueOne, valueTwo):
    index = 0
    rec = valueOne
    while index < valueTwo:
        rec = Fun11_2(rec, valueOne)
        index += 1
    return rec


print(Fun12(2, 4))
print("Exersice 14")


def Fun13():
    indexOne = 1
    indexTwo = 1
    while indexOne < 11:
        while indexTwo < 11:
            print(indexOne, "*", indexTwo, "=", indexOne * indexTwo)
            indexTwo += 1
        indexTwo = 1
        indexOne += 1


Fun13()

print("Exersice 14")


def Fun14(listIn):
    listStr = []
    index = 0
    while index < len(listIn):
        listStr.append(str(listIn[index]))
        index += 1
    index = 0
    while index < len(listStr):
        if len(listStr[index]) == 4:
            print("  ", listStr[index])
        else:
            if len(listStr[index]) == 3:
                print("   ", listStr[index])
            else:
                if len(listStr[index]) == 2:
                    print("    ", listStr[index])
                else:
                    if len(listStr[index]) == 1:
                        print("     ", listStr[index])
        index += 1


Fun14([1, 2, 3, 222, 4444, 12, 332])

print("Exersice 15")


def Fun15():
    point = 0
    index = 1
    valueOne = 0
    valueTwo = 0
    result = 0
    string = ""
    while index < 6:
        print("У вас", point, " очков", " , попытка", index, "из", 6)
        valueOne = int(input("Первое число "))
        valueTwo = int(input("Второе число "))
        strring = str(valueOne) + " * " + str(valueTwo) + " = "
        result = int(input(strring))
        if result == valueOne * valueTwo:
            point += 1
            print("Правильно")
        else:
            print("Не прваильно")
        index += 1


print("Exersice 16")


def Fun16(listNumbersIn):
    maxFirstNumber = listNumbersIn[0]
    maxSecondNumber = listNumbersIn[0]
    indexForlistNumberIn = 0
    while indexForlistNumberIn < len(listNumbersIn):
        if listNumbersIn[indexForlistNumberIn] > maxFirstNumber:
            maxFirstNumber = listNumbersIn[indexForlistNumberIn]
        indexForlistNumberIn += 1
    indexForlistNumberIn = 0
    while indexForlistNumberIn < len(listNumbersIn):
        if listNumbersIn[indexForlistNumberIn] > maxSecondNumber and listNumbersIn[
            indexForlistNumberIn] < maxFirstNumber:
            maxSecondNumber = listNumbersIn[indexForlistNumberIn]
        indexForlistNumberIn += 1

    return [maxFirstNumber, maxSecondNumber]


print(Fun16([1, 2, 44, 4, 5, 22, 1, 33, 442, 21, 222]))

print("Exersice 17")


def Fun17(value):
    index = 0
    while index < value:
        print("*" * value)
        index += 1


Fun17(55)

print("Exersice 18")


def Fun18(value):
    index = 0
    while index < value:
        if (index == 0 or index == value - 1):
            print("*" * value)
        else:
            print("*", " " * value, "*")
        index += 1


Fun18(10)

print("Exersice 19")


def Fun19(value):
    index = 0
    while index < value:
        if index % 2 == 0:
            print(" *" * value)
        else:
            print("* " * value)
        index += 1


Fun19(10)

print("Exersice 20")


def Fun20(valueOne, valueTwo):
    while valueOne <= valueTwo:
        if valueOne % 2 == 0:
            print(valueOne)
        valueOne += 1


Fun20(1, 13)

print("Exersice 21")


def Fun21(value):
    result = 1
    index = 1;
    while index <= value:
        result = result * (index)
        index += 1
    return result


print(Fun21(2))

print("Exersice 22")


def Fun22(valueSum, valueProc, valueTime):
    index = 0
    result = 0
    while index < valueTime:
        result = valueSum * (valueProc / 100)
        valueSum += result
        index += 1
        print(valueSum - result, "   |   ", valueSum)


Fun22(10000, 12, 36)

print("Exersice 23")


def Fun23(value):
    index = 2;
    result = True
    while index < value:
        if value % index == 0:
            result = False
            break
        index += 1
    return result


print(Fun23(11))
