import re

print("Exersice 1")
result = re.match(r" ", " ")
if result is None:
    print("Не является пробелом")
else:
    print("Является пробелом")
print(result.group(0))

print("Exersice 2")
result = re.match("^\d$", "4")
if result is None:
    print("Не является цифрой")
else:
    print("Является цифрой")

print("Exersice 3")
result = re.match("^\d\d$", "22")
if result is None:
    print("Не является двухзначным числом")
else:
    print("Является двухзначным числом")

print("Exersice 4")

result = re.match("^\s\s\s$", "   ")
if result is None:
    print("Не является тремя пробелами")
else:
    print("Является тремя пробелами")
print("Exersice 5")
result = re.match("^a\dv$","a5v")
if result is None:
    print("Не является a<некоторая цифра>v")
else:
    print("Является a<некоторая цифра>v")


