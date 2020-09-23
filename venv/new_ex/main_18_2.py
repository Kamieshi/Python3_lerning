def print_fun(fun,value):
    print(fun.__name__," : ",value)

def fun_1(number_obj,default_numb_obj = 7):
    return number_obj * default_numb_obj

def fun_2(list_number,default_list_number = [1,2,3]):
    return_list = []
    for _ in list(range(len(list_number))):
        return_list.append(list_number[_] + default_list_number[_])
    return return_list

def fun_3(nunmber_obj, default_number_obj = 2, default_dict ={"divisor":3}):
    return (nunmber_obj + default_number_obj)/default_dict["divisor"]

print_fun(fun_1, fun_1(1))
print_fun(fun_1, fun_1(2,5))
print_fun(fun_2,fun_2([1,2,3]))
print_fun(fun_2,fun_2([1,2,3],[2,3,4]))
print_fun(fun_3,fun_3(2))
print_fun(fun_3,fun_3(2,4,{"divisor":2}))