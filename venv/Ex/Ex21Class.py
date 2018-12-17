print("Exersice 1")
class People:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex

print("Exersice 2")
class Tree:
    def __init__(self, name, growth):
        self.name = name
        self.growth = growth

    def growth_up(self, growth_up):
        self.growth += growth_up

    def print_info(self):
        print(self.name, self.growth)

print("Exersice 3")
class Home:
    def __init__(self,map,coutn_room):
        self.map=map
        self.coutn_room=coutn_room

print("Exersice 4")
class Book:
    def __init__(self,name,aotur):
        self.name=name
        self.aotur=aotur

print("Exersice 5")
class Case_messeg:
    def __init__(self,input,output,meseg):
        self.input=input
        self.output=output
        self.meseg=meseg

mail = Case_messeg("Jhon","Martin",[123,222,33])

print(mail.__sizeof__())


