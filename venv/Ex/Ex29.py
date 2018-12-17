import re
def print_result(res):
    if res is None:
        print("не соответствуют формату")
    else:
        print(result.group(0))

print("Exersice 1")
result = re.match("^a\d+c$","a12c")
print_result(result)
print("Exersice 2")
result= re.match("^a(\d+|)c$","a456c")
print_result(result)
print("Exersice 3")
def get_domain(strirng_in):
    result = re.match("^\w+@(.+)$",strirng_in).groups()
    return result[0]
def get_login(string_in):
    result = re.match("^(\w+|.)@.+$", string_in).groups()
    return result[0]
mail="logintadadada@gmaail.com"
try:
    print("Login:",get_login(mail))
    print("Domain:",get_domain(mail))
except Exception as e:
    print("Only email")


print("Exersice 4")
def get_value(string):
    result= re.match("^<.+>(.+)<.+>$",string).groups()
    return result[0]

print(get_value("<tag>info tag<tag>"))

print("Exersice 5")

def get_minuts(string):
    try:
        result= re.match("^.+\d+:(\d+):\d+$",string).groups()
        return result[0]
    except Exception as e:
        return "Non time"


print(get_minuts("tatata 22:44:66"))

print("Exersice 6")
def calc(string):
    listing = re.match("^(.+) (\+|-|\*|/) (.+)$",string).groups()
    value_one=float(listing[0])
    value_two=float(listing[2])
    print(value_one,value_two)
    print(listing)
    if listing[1] == "+":
        return  value_two+value_one
    else:
        if listing[1]=="-":
            return value_one-value_two
        else:
            if listing[1]== "*":
                return  value_one*value_two
            else:
                return value_one/value_two

print(calc("25.6 - 0.6"))







