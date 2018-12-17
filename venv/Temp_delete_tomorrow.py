
def all_sum(item):
    return item*2


def my_map(function,list_in):
    result=[]
    for item in list_in:
        result.append(function(item))
    return result

def delenie(item):
    return item/2


print(my_map(all_sum,[1,2,3,4,5]))
print(my_map(delenie,[1,2,3,4,5,6]))

print(my_map(lambda x:x/2,[2,4,6]))

my_map(lambda x:x**x,[1,2,3,4])