"""
str1 = "abcdABCDabcd";
occurrence of each character
"""


def occ_Char(str1):
    size = len(str1)
    dict = {}
    for i in range(size):
        if str1[i] not in dict:
            dict[str1[i]] = 1

        else:
            dict[str1[i]] = dict[str1[i]] + 1

    print(dict)




str1 = "abcdABCDabcd"
occ_Char(str1)