import re


def fun_1(str_obj):
    if re.match("^a\d+c$", str_obj) is not None:
        return "fn1 Good"

    return "fn_1 bad"


def fun_2(str_obj):
    if re.match("^a\d*c$", str_obj) is not None:
        return "fn_2 Good"

    return "fn_2 bad"


def fun_3(str_email):
    try:
        str = re.match("^((\w|\.)+)@.+$", str_email).groups()[0]
    except Exception as e:
        raise Exception("Onlyt Email")
    return str


def fun_4(str_obj):
    try:
        tag = re.match("^<(\w+).+>$", str_obj).groups()[0]
        return str_obj.replace('<' + tag + '>', '')
    except Exception as e:
        return "Не найден тег"


def fun_5(str_obj):
    try:
        return re.match("^\d\d-\d\d-\d\d\s\d\d:(\d\d):\d\d$", str_obj).groups()[0]
    except Exception as e:
        return "no time"


def fun_6(str_obj):
    numbers = re.match("^(-?.+)\s(-|\+|\*|/)\s(-?.+)$", str_obj).groups()
    num_1, num_2 = float(numbers[0]), float(numbers[2])
    return_dict = {'*': num_1 * num_2,
                   '/': num_1 / num_2,
                   '+': num_1 + num_2,
                   '-': num_1 - num_2}
    return return_dict[numbers[1]]


print(fun_1("a234546546c"))

print(fun_2("a12c"))
print(fun_3("rusack.dmitr.free@gmail.com"))
print(fun_4("<good>kilogram<good>"))
print(fun_5("22-88-55 66:13:22"))
print(fun_6("10 * -6"))
