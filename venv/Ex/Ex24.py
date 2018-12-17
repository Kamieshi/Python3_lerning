print("Exersice 1")


def first_item_capitalize(function):
    def capital(string_in):
        string_in = function(string_in)
        return string_in.capitalize()

    return capital


@first_item_capitalize
def swap_words(words):
    tmp = words.split(' ')
    return tmp[1] + ' ' + tmp[0]


print(swap_words("qwe asd"))

print("Exersice 2")


def two_milt_on_2(function):
    def mult(list):
        result = function(list)
        return function(result)

    return mult


@two_milt_on_2
def mult_on_2(ls):
    result = []
    for x in ls:
        result.append(x * 2)
    return result


print(mult_on_2([1, 2, 3, 4]))

print("Exersice 3")

import math


def obertka(function):
    def chek(number):
        if number > 0:
            return function(number)
        else:
            print("нельзя отрицательные")
            return -1

    return chek


@obertka
def my_sqrt(x):
    return math.sqrt(x)


print(my_sqrt(-5))
