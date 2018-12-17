def dict(a,b):
    d={"a":a,"b":b,"sum":a+b}
    return d
print(dict(1,2))

print("--------------")

def FalsIfTrue(a):
    return 4 in a or 8 in a
print(FalsIfTrue([2,3,6]))

print("--------------")

def delSpis(a,b):
    return a[len(a)-1]/b[0]

print(delSpis([0,2,3,1,10],[2,3]))

print("--------------")

def Probel(a):
    return a.replace(" ","privet")

print(Probel("jjkjkj kjjkjk"))

print("--------------")

def returnTwoSlovo(a):
    return a.split(" ")[1]

print(returnTwoSlovo("odin dwa tri"))

print("--------------")

def PervNaChet(a):
    a[0]=a[3]
    return a

print(PervNaChet([1,2,3,4,5]))

print("--------------")

def zamNaKey(a):
    a["a"]=86
    return a

print(zamNaKey({"a":1,"b":2}))

print("--------------")

def DelBforKey(a):
    del a["b"]
    return a

print(DelBforKey({"a":1,"b":2}))

print("--------------")

def AddTwoElemSumTWOTWO(a):
    a[1]+=33
    return a

print(AddTwoElemSumTWOTWO([1,2,3,4]))


print("Exersice 15")

def Fun15(a):
    return a+[a[0]+(len(a))]

print(Fun15([1,2,3,4]))

print("Exersice 16")
def Fun16(a):
    a["c"]=a["a"]+45
    return a

print(Fun16({"a":0,"b":1}))

print("Exersice 17")
def Fun17(a):
    a[0]=a[1]
    return a

print(Fun17([0,1,2,3]))

print("Exersice 18")
def Fun18(Dic,value):
    del Dic["a"]
    Dic["c"]=value
    return Dic

print(Fun18({"a":1,"b":2}, 0))

print("Exersice 19")
def Fun19(List):
    return [List[0],List[len(List)-1]]

print(Fun19([0,1,2,3,4,5]))

print("Exersice 20")
def Fun20(Dic):
    return [Dic["b"],Dic["m"]]

print(Fun20({"a":0,"b":1,"c":2,"m":3}))

print("Exersice 21")
def Fun21(List,Value):
    return [Value]+List

print(Fun21([1,2,3,4],0))


print("Exersice 22")
def Fun22(a,b):
    return [a]+b

print(Fun22(0,[1,2,3]))


print("Exersice 23")
def Fun23(a):
    b=a.split(" ")
    return len(b)-1
print(Fun23("asd asd asd zxc as "))


print("Exersice 24")
def Fun24(a):
    b=a.split(" ")
    return b[1] + " " + b[0]

print(Fun24("123 456"))



