def print_obj_tree(obj):
    print("Дерево : ", obj.name, ". Рост : ", obj.rost)


class Tree:
    def __init__(self, string_name_tree, int_rost=0):
        self.name = string_name_tree
        self.rost = int_rost

    def add_rost(self, int_add_rost=10):
        self.rost += int_add_rost


class People():
    def __init__(self, str_name, int_age, bool_candy=True):
        self.name = str_name
        self.age = int_age
        self.candy = bool_candy

    def buy_candy(self):
        self.candy = True

    def eaten_candy(self):
        self.candy = False

class Book:
    def __init__(self,str_name,list_paper):
        self.name = str_name
        self.lists = list_paper

    def print_list(self,int_index_list):
        print(int_index_list," . ",self.lists[int_index_list])

class Mail:
    def __init__(self,str_sender,str_folder,str_mail,str_podp = ""):
        self.sender = str_sender
        self.folder = str_folder
        self.mail = str_mail
        self.podp = str_podp

    def add_podp(self,str_podp):
        str_podp +=str_podp

mail = Mail("asd@gmail.com","asdzxc@gmail.com","hello py")

mail.add_podp("Thender")




people_1 = People("Nick", 20)
people_1.buy_candy()
people_2 = People("Toko", 20, True)
people_2.eaten_candy()
book = Book("Bible",["жыли были","не тужыли","а тут кретсовый поход"])

book.print_list(2)
for _ in [people_1, people_2]:
    if _.candy:
        print(_.name, " have candy")
    else:
        print(_.name, "dont hav candy")
