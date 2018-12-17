import re
print("Exersice 1")

result= re.match("^[HBMP][HBMP]\d\d\d\d\d\d\d$","HH1234567")
if result is None:
    print("Не является паспортом")
else:
    print("Является паспортом")

print("Exersice 2")
result=re.match("^(Привет|Добрый|Здравствуй|Хай) человек$","Добрый человек")
if result is None:
    print("Не поздаровался")
else:
    print(result.group(0))

print("Exersice 3")
result =re.match("^\d (\+|\*|/) \d$","2 / 3")
if result is None:
    print("не соответствуют формату 1 + 5")
else:
    print(result.group(0))