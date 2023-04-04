import psycopg2 # Postgres
from Excel_operations import Excel_Utility01

connection=psycopg2.connect(host="62.171.183.83",database="Motherson-23-03-2023",user="postgres",password="pg@123",port="5433")
print(connection)

connection.autocommit=True # To perform in Actual DB
cursor=connection.cursor()
cursor.execute("select * from users;")
users=cursor.fetchall() # To fetch all the data
row_entry_point=2
excel_path="E:\\Automation\\Data\\DB_Excel.xlsx"

for i in users:
    column_entry_point=1
    for j in i:
        Excel_Utility01.write_excel(excel_path, row_entry_point, column_entry_point, j)
        column_entry_point = column_entry_point + 1
    row_entry_point = row_entry_point + 1


    # pytest - 39,40,41 & Log
