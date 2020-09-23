from functools import reduce


class Build:
    def __init__(self, int_max_col=0):
        self.max_col = int_max_col

    def add_max_col(self, int_add_col):
        self.max_col += int_add_col


class School(Build):
    def __init__(self, int_max_col, str_type):
        super().__init__(int_max_col)
        self.type = str_type


class Shop_center(Build):
    def __init__(self, int_max_col, str_name):
        self.name = str_name
        super().__init__(int_max_col)


class Factorial():
    def __factorial(self, list_number):
        return reduce(lambda x, y: x * y, list_number, 1)

    def fact(self, list_number):
        return self.__factorial(list_number)


class Bank:
    def __init__(self, list_dict_people_deposit):
        self.peoples = list_dict_people_deposit

    def __add__(self, other):

        for _ in self.peoples:
            other.peoples.append(_)
        return other

    def print_Bank(self):
        for _ in self.peoples:
            print(_["name"]," : ",_["deposit"])


deposit_1 = [{"name": "name_1", "deposit": 100}, {"name": "name_2", "deposit": 200}, {"name": "name_3", "deposit": 20}]
deposit_2 = [{"name": "name_4", "deposit": 1}, {"name": "name_5", "deposit": 500}, {"name": "name_6", "deposit": 220}]

bank_1 = Bank(deposit_1)
bank_2 = Bank(deposit_2)

bank = bank_1 + bank_2

bank.print_Bank()
