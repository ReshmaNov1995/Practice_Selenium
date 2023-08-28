import csv
# csv file starts from row value as '0'

kkk=[]
with open('E:\Myn\ddt2.csv') as cards:
    csv_reader = csv.reader(cards)
    for row, column in enumerate(csv_reader): # enumerate - Split the row & column data. Then it has stored in row,column.
        # print(index)
        kk = []
        if row != 0:
            un = column[0]
            psd = column[1]
            # print(column[0])
            # print(column[1])
            kk.insert(0, un)
            kk.insert(1, psd)
            kkk.append(kk)



print(kkk)

# Refer PyTest Folder->test_parallel_csvfiles.py