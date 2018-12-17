import pandas
from pandas import DataFrame

df = pandas.read_csv("../Data/titanic.csv")

print("Exersice 1")

print(df.columns)

print("Exersice 2")

print("Всего записей в списке", df.shape[0], "\n Находилось на борту",
      df[(df["Pclass"] == 1) | (df["Pclass"] == 2) | (df["Pclass"] == 3)].shape[0])

print("Exersice 3")

print("Мужчин было", df[df["Sex"] == "male"].shape[0])

print("Exersice 4")

print("Выжило", int(df[df["Survived"] == 1].shape[0] * 100 / df.shape[0]), "%")

print("Exersice 5")


def male_vs_famel(male_count, famel_count):
    if male_count > famel_count:
        return "мужчин больше"
    elif famel_count > male_count:
        return "женщин больше"
    elif famel_count == male_count:
        return "поровну"


print("На борту было", male_vs_famel(df[df["Sex"] == "male"].shape[0], df[df["Sex"] == "female"].shape[0]),
      df[df["Sex"] == "male"].shape[0], "vs", df[df["Sex"] == "female"].shape[0])

print("Exersice 6")

print("Из выживших мужчинами было",
      int(df[(df["Sex"] == "male") & df["Survived"] == 1].shape[0] * 100 / df[df["Survived"] == 1].shape[0]))

print("Exersice 7")

for item in list(range(1, 4)):
    print("Умерло", df[(df["Pclass"] == item) & (df["Survived"] == 0)].shape[0], "человек", item, "класса")
