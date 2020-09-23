import re


def fun_1(str_obj):
    if re.match("^[HBMP][HBMP]\d\d\d\d\d\d\d$", str_obj) is not None:
        return re.match("^([HBMP][HBMP])(\d\d\d\d\d\d\d)$", str_obj).groups()
    return "Bad"


def fun_2(str_obj):
    if re.match("^(Hi|Hello).+$", str_obj) is not None:
        return "Good"
    return "Bad"


def fun_3(str_obj):
    if re.match("^\d\s(\+|-|\*|/)\s\d$", str_obj) is not None:
        return "Good"
    return "Bad"


print(fun_1("HP1234567"))
print(fun_2("Hello bro good"))
print(fun_3("2 / 4"))
