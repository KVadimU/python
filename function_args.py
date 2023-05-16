##def f(h1 =1, h=2, *args, key):
##    print(h1, h, key)
##    print(args)
##f(4,5,6,7,8, key=10)
#Поиск эксклюзивных элементов списков#
def exclusive_item(*args, key=False):
    new_list = []
    for i in args:
        for j in i:
            if j not in new_list:
                new_list.append(j)
    if key == True:
        new_list.sort()
    return new_list

list_1 = [1, 2, 3, 4, 5, 5, 5]
list_2 = [1, 2, 3, 4, 5, 6 , 7, 1, 2]
list_3 = [1, 2, 3, 4, 5, 6 , 7, 11, 12]

result = exclusive_item(list_1, list_2, list_3, key=True)
print(result)
