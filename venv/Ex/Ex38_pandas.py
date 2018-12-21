import pandas

info = pandas.read_csv('../Data/info.csv')
marks = pandas.read_csv('../Data/marks.csv')

print("Exersice 1")
print(info.merge(marks, left_on='id', right_on='id2').shape[0])

print("Erersice 2")

print(marks.merge(info, left_on='id2', right_on='id').shape[0])

print("Exersice 3")

df = info.merge(marks, left_on='id', right_on='id2')
df2 = df[df['race'] == 'group A']
print(df2['math'].sum() /
      df2.shape[0])

print("Exersice 4")

print(info.merge(marks, left_on='id', right_on='id2', how='outer').shape[0])

print("Exersice 5")

print(info.merge(marks, left_on='id', right_on='id2', how='left').shape[0])

print("Exersice 6")

print(marks.merge(info, left_on='id2', right_on='id', how='left').shape[0])
