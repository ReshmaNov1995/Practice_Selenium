"""
list1 = [20,30,50,70,90]
list2 = [100,70,80,10,40]

get the common numbers from the 2 list
"""

def common_items(list1, list2):
    lista = set(list1)
    listb = set(list2)

    common_listitems = lista & listb
    print(common_listitems)

list1 = [20,30,50,70,90]
list2 = [100,70,80,10,40]

common_items(list1, list2)