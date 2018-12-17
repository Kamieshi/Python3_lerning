def fun(value):
    list = [[0 for item in range(value)] for item in range(value)]


value = 5
if value % 2 != 0:
    center = int((value - 1) / 2)
else:

    center = int(value / 2)
    value += 1

list = [[0 for item in range(value)] for item in range(value)]

list[center][center] = 1
index_for_x = 0
index_for_y = 0

while index_for_y < value:
    list[index_for_y][center] = 0
    list[center][index_for_y] = 0
    index_for_y += 1
temp_matrix = [[0 for item in range(center + 1)] for item in range(center + 1)]
index_for_y = 0
while index_for_y < center + 1:
    while index_for_x < center + 1:
        if index_for_x + index_for_y >= center:
            list[index_for_y][index_for_x] = 1
            temp_matrix[index_for_y][index_for_x] = 1
        else:
            temp_matrix[index_for_y][index_for_x] = 0
        index_for_x += 1
    index_for_x = 0
    index_for_y += 1

index_for_y = 0
index_for_x = 0

while index_for_y <= center:
    while index_for_x <= center:
        list[index_for_x + center][index_for_y] = temp_matrix[center - index_for_x][index_for_y]
        index_for_x += 1
    index_for_x = 0
    index_for_y += 1

index_for_y = 0
index_for_x = center

while index_for_y <= center:
    while index_for_x < value:
        list[index_for_y][index_for_x] = temp_matrix[index_for_y][center - (index_for_x - center)]
        index_for_x += 1
    index_for_x = center
    index_for_y += 1

index_for_y = center
index_for_x = center

while index_for_y < value:
    while index_for_x < value:
        list[index_for_y][index_for_x] = temp_matrix[center - (index_for_y - center)][center - (index_for_x - center)]
        index_for_x += 1
    index_for_x = center
    index_for_y += 1


def preobr(item_list):
    return_list = []
    for intem in item_list:
        if intem == 1:
            return_list.append("*")
        else:
            return_list.append(" ")
    return return_list


list_final = []

for item in list:
    list_final.append(preobr(item))

index_for_y = 0
index_for_x = 0
temp_string = ""
while index_for_y < value:
    while index_for_x < value:
        temp_string += str(list_final[index_for_y][index_for_x])
        index_for_x += 1
    print(temp_string)
    temp_string = ""
    index_for_x = 0
    index_for_y += 1
