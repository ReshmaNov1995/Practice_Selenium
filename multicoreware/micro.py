"""
Python dictionary merging and sorting.
dict1:
Ram 13
Vijay 2
Ramya 5
Madhu 1

dict2:
Suriya 9
Mahesh 8
Anu 4
"""

# Merging
# def merge(dict1, dict2):
#     (dict1.update(dict2))
#     print(dict1)
#
# dict1 = {"Ram": 13, "Vijay": 2, "Ramya": 5, "Madhu":1}
# dict2 = {"Suriya": 9, "Mahesh":8, "Anu":4}
# merge(dict1, dict2)

# Sorting by value
def sort(dict1):
    sort = dict(sorted(dict1.items(), key=lambda item: item[1]))
    print(sort)

dicta = {'Ram': 13, 'Vijay': 2, 'Ramya': 5, 'Madhu': 1, 'Suriya': 9, 'Mahesh': 8, 'Anu': 4}
sort(dicta)

# Sorting by key
def sort(dict1):
    sort = dict(sorted(dict1.items()))
    print(sort)

dicta = {'Ram': 13, 'Vijay': 2, 'Ramya': 5, 'Madhu': 1, 'Suriya': 9, 'Mahesh': 8, 'Anu': 4}
sort(dicta)
