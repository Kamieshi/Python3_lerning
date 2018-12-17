print("Exersice 1")


class Tree:
    def __init__(self, name, growth):
        self.name = name
        self.growth = growth

    def growth_up(self, growth_up):
        self.growth += growth_up

    def print_info(self):
        print(self.name, self.growth)


print("Exersice 2")


class People:
    def __init__(self, name, sex, eaten_candy=[]):
        self.name = name
        self.sex = sex
        self.eaten_candy = eaten_candy

    def eat_candy(self, candy):
        self.eaten_candy += candy

    def info(self):
        print(self.name)
        print(self.sex)
        print("Сьедено :")
        for item in self.eaten_candy:
            print(item)


people_one = People("Jack", "Man")
people_one.eat_candy(["Gold Key", "Irisochka"])
people_one.info();

print("Exersice 3")


class Book:
    def __init__(self, name, aotur, paper_count):
        self.name = name
        self.aotur = aotur
        self.paper = []
        index = 0;
        while index < paper_count:
            self.paper.append(index)
            index += 1

    def info_book_full(self):
        print(self.name, self.aotur, len(self.paper))

    def select_paper(self, paepr):
        print(self.name, self.aotur, self.paper[paepr])


book_one = Book("Lukiar", "Chernovik", 233)
book_one.info_book_full()
book_one.select_paper(22)

print("Exersice 4")


class Case_messeg:
    def __init__(self, input, output, meseg,ps=""):
        self.input = input
        self.output = output
        self.meseg = meseg
        self.ps=ps;

    def add_ps(self):
        self.ps+="С уважением "+ self.input

    def info(self):
        print("Отправитель: ", self.input)
        print("Получатель: ",self.output)
        print("Текста письма :")
        print(self.meseg)
        print(self.ps)


meseg_one=Case_messeg("Dzmitry","Ksenia","Привет как дела")
meseg_one.add_ps()
meseg_one.info()

print("Exersice 5")
import datetime
class Time:
    def __init__(self,month,day,year):
        self.day=datetime.date(year,month,day)

    def add_day(self,day):
        self.day+= datetime.timedelta(days=day)

    def info(self):
        print(self.day.isoformat())

time_one=Time(1,1,2019)
time_one.add_day(40)
time_one.info()





