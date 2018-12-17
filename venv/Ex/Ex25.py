print("Exersice 1")

def fun1 (list_number):
    return list(map(lambda x:x+100,list_number))
print(fun1([1,2,3]))

print("Exersice 2")

def fun2(list_number):
    return list(filter(lambda x:x%2,list_number))

print(fun2([1,2,3,4]))