print("Exersice 1")


def fun1(value_one, value_two=1):
    return value_two * value_one


print(fun1(5))

print("Exersice 2")


def fun2(list_in_one, list_in_two=[0, 1, 2, 3]):
    return list_in_two + list_in_one


print(fun2([4, 5, 6]))

print("Exersice 3")
def fun3(number_in_one,number_in_two=2,dic_in={"divisor":5}):
    return (number_in_one+number_in_two)/dic_in["divisor"]
print(fun3(3))




