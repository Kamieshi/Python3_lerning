print("Exersice 1")
class Building:
    def __init__(self, adres):
        self.adres=adres

    def info(self):
        print(self.adres)

class Shop_center(Building):
    def __init__(self,name,time_open, time_clos, adres,status=False):
        self.name=name
        self.time_open=time_open
        self.time_close=time_clos
        self.statatus=status
        super().__init__(adres)

    def info(self):
        print("name {}, time open {}, time close{}, adress {}, status {}".format(self.name,self.time_open,self.time_close,self.adres,self.statatus))



class School(Shop_center):
    def __init__(self,name,time_open, time_clos, adres,type,count_lerning_piple,status=False):
        super().__init__(name,time_open,time_clos,adres,True)
        self.type = type;
        self.count_lerning_people=count_lerning_piple

    def add_count(self,delta):
        self.count_lerning_people+=delta

    def del_count(self,delta):
        self.count_lerning_people-=delta

    def info(self):
        print(print("name {}, type {}, time open {}, time close{}, adress {},count {}, status {}".format(self.name,self.type,self.time_open,self.time_close,self.adres,self.count_lerning_people,self.statatus)))


buld= Building("Bobr")

test= Shop_center("Galieo","9:00","23:00","Bobr.strit",True)

schol= School("№23","08:00","19:00","HZ adres","БАзовая",45,True)

buld.info()
test.info()
schol.add_count(5)
schol.info()

print("Exersice 2")
class Factorial:
    def __proschet(self,value):
        rec=1
        index=0
        while index<value:
            rec=rec*(index+1)
            index+=1
        return rec

    def calcilate(self,value):
        return (self.__proschet(value))

fact=Factorial()
print(fact.calcilate(5))

print("Exersice 3")
class Bank:
    def __init__(self,deposits):
        self.deposits=deposits

    def __add__(self, other):
        result=Bank(self.deposits+other.deposits)
        return result

    def info(self):
        print(self.deposits)

bank_one=Bank([22,33,44])
bank_two=Bank([55,66,77])
bank_three=bank_one+bank_two
bank_three.info()




