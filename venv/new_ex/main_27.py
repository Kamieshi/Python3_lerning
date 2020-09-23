import re


def fun_1(str_obj):
    for _ in str_obj:
        if re.match("^\s$", str_obj) is not None:
            return True
    return False

def fun_2(str_obj):
    for _ in str_obj:
        if re.match("^\d$",_) is not None:
            return "Цифры есть"
    return "Нету цифр"

def fun_3(str_obj):
    if re.match("^\d\d$",str_obj) is not None:
        return "Две цифры"
    return "не дву цифры"

def fun_5(str_obj):
    if re.match("^a\dv$",str_obj) is not None:
        return "Являтся"
    return "Не является"


print(fun_1('asd 2'))
print(fun_2("asd"))
print(fun_3("222"))
print(fun_5("a4c"))
