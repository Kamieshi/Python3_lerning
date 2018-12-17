import random
print("Exersice 1")
def Fun1(List):
    summ=0;
    for x in List:
        summ+=x
    return  summ

print(Fun1([1,2,3]))

print("Exersice 2")
def Fun2(ListIn):
    ListOut=[]
    for x in ListIn:
        ListOut.append(x/2)
    return  ListOut

print( Fun2([2,4,6]))
print("Exersice 3")

def Fun3(List):
    LEN=0
    for x in List:
        LEN+=1;
    return LEN;
print(Fun3([1,2,3,4,5]))

print("Exersice 4")
def Fun4(List,Value):
    for item in List:
        if item == Value:
            return True
    return False

print(Fun4([1,2,3,5],5))

print("Exersice 5")
def Fun5(List):
    summ=0
    for item in List:
        summ+=item
    return summ/len(List)

print(Fun5([5,5,5,6]))
print("Exersice 6")
def Fun6(List):
    max=List[0]
    for item in List:
        if item>max :
            max=item
    return  max
print(Fun6([2,6,1,-1]))

print("Exersice 7")
def Fun7(List):
    min=List[0]
    for item in List:
        if item<min:
            min = item
    return  min
print(Fun7([0,1,2,-5,3]))

print("Exersice 8")
def Fun8(List):
    Chet=[]
    for item in List:
        if item%2==0:
            Chet.append(item)
    return  Chet
print(Fun8([1,2,3,4,5,6]))

print("Exersice 9")
def Fun9(List):
    dChet=[]
    for item in List:
        if item%2!=0 :
            dChet.append(item)
    return  dChet
print(Fun9([1,2,3,4,5]))
print("Exersice 10")
def Fun10(ListFirst,ListLast):
    tugez=[]
    for itemListFirst in ListFirst:
        for itemListLast in ListLast:
            if itemListFirst==itemListLast:
                tugez.append(itemListFirst)
    return tugez

print(Fun10([1,2,3,4],[3,4,5,6,7]))

print("Exersice 11")
def Fun11(ListFirst,ListLast):
    DeletedList=[]
    for itemListFirst in ListFirst:
        if itemListFirst in ListLast:
            continue
        else:
            DeletedList.append(itemListFirst)

    return DeletedList

print(Fun11([1,2,3,4],[2,3]))

print("Exersice 12/2")
def Fun121(value1, value2):
    umn=0;
    for item in list(range(value1)):
        umn+=value2
    return umn
print(Fun121(10,3))

print("Exersice 12")
def Fun12(value1,value2):
    rez=0
    for item1 in list(range(value1)):
        for item2 in list(range(value2)):
            rez+=value1
    return  rez;
print(Fun12(2,3))

print("Exersice 13")
def Fun13():
    for item1 in list(range(11)):
        for item2 in list(range(11)):
            print(item1," * ",item2," = ",item1*item2)

Fun13()

print("Exersice 14")
def Fun14(List):
    tempList=[]
    for item in List:
        tempList.append(str(item))
    for item in tempList:
        if len(item)==4:
            print("  ",item)
        else:
            if len(item) == 3:
                print("   ",item)
            else:
                if len(item)==2:
                    print("    ",item)
                else:
                    if len(item)==1:
                        print("     ",item)

Fun14([2,33,1111,323,2312,0,1231,43,2])

print("Exersice 15")
def Fun15():
    x=1
    count=0
    value1=0
    value2=0
    value3=0
    while x<6:
        print("попытка ",x,"/",5,"Правильных ответов", count)
        value1=random.randint(0,11)
        value2=random.randint(0,11)
        print("сколько будет ",value1," * ",value2)
        value3=int(input())
        if(value3==value2*value1):
            print("Правильно")
            count+=1
        else:print("Неправильно")
        x+=1



print("Exersice 16")
def Fun16(List):
    FirstMax=List[0]
    LastMax=List[0]
    for item in List:
        if item >FirstMax and item> LastMax:
            FirstMax=item
    for item in List:
            if  item>LastMax and item <FirstMax:
                LastMax=item
    return [FirstMax,LastMax]

print(Fun16([1,2,3,4,5,6,-1,3123,-21,-123,3222]))

print("Exersice 17")
def Fun17(value):
    for item in list(range(value)):
        print("*"*value)

Fun17(5)

print("Exersice 18")
def Fun18(value):
    for item in list(range(value)):
        if item!=0 and item!=value-1:
            print("*"," "*(len(list(range(value)))-2),"*")
        else: print("*"*value)

Fun18(3)

print("Exersice 19")
def Fun19(value):
    for item in list(range(value)):
        if(item%2==0):
            print(" *"*value)
        else:
            print("* "*value)

Fun19(5)

print("Exersice 20")
def Fun20(value1,value2):
    List=[]
    for item in list(range(value2-value1)):
        if (value1+item)%2==0:
            List.append(value1+item)
    return List
print(Fun20(1,10))

print("Exersice 21")
def Fun21(value):
    fac=1;
    for item in list(range(value+1)):
        if item !=0:
            fac=fac*item
    return fac
print(Fun21(4))

print("Exersice 22")
def Fun22(value1,value2,value3):
    for item in list(range(value3)):
        print("сумма в начале месяца ", value1,"процент ",value2,"месяц ", item+1)
        value1=value1+(value1*(value2/100))
        print("сумма в конце месяца ", value1, "процент ", value2, "месяц ", item + 1)
    return [value1]

Fun22(40,50,3)

print("Exersice 23")
def Fun23(value):
    Bool=False
    for item in list(range(value)):
        if item!=0 and value%item==0 and item!=value and item!=1:
            return False
    return True

print(Fun23(4))

print("Exersice 24")
def Fun24(value):
    for item in list(range(value)):
        print(item*"*")
Fun24(5)

print("Exersice 25")






