import psycopg2 # Posgres
import openpyxl
from Excel_operations import Excel_Utility01

connection=psycopg2.connect(host="62.171.183.83",database="ETICA_01-08-2023",user="postgres",password="pg@123",port="5433")
print(connection)

# connection.autocommit=True # To perform in Actual DB
cursor=connection.cursor()
cursor.execute("select * from users;")
users=cursor.fetchall() # To fetch all the data
row=2
excel_path="E:\\Automation\\Data\\DB_Excel.xlsx"
workbook = openpyxl.load_workbook(excel_path)
worksheet = workbook["Sheet1"]

for i in users:
    column=1
    for j in i:
        worksheet.cell(row, column).value = j
        workbook.save(excel_path)
        column_entry_point = column + 1
    row_entry_point = row + 1


    # pytest - 39,40,41 & Log
