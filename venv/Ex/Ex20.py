print("Exersice 1")


def fun1(*items):
    sum = 0
    for item in items:
        sum += item
    return sum

tuple_in=(2,2,2,2,2)
print(fun1(*tuple_in))

print("Exersice 2")


def fun2(**items):
    result = 1
    for item in items.values():
        result = item * result
    return result


dic_in={"one":5,"two":2}
print(fun2(**dic_in))

print("Exersice 3")


def fun3(velue_one, **dic_in):
    sum = velue_one
    for item in dic_in.values():
        sum += item
    return sum


print(fun3(1,**dic_in))

print("Exersice 4")


def fun4(*list_in, value_one=2):
    result = 1;
    for item in list_in:
        result = result * item
    return result * value_one


print(fun4(*tuple_in))

print("Exersice 5")


def fun5(*list_in, **dec_in):
    sum = 0
    for item in list_in:
        sum += item
    for item in dec_in.values():
        sum += item
    return sum


print(fun5(*tuple_in,**dic_in))
