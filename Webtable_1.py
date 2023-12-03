# count no.of.rows & columns
# Read specific row & column data
# Read all row & column data
# Read data based on condition(List book name whose author is Amit)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(service = Service(EdgeChromiumDriverManager().install()), options = edge_option)

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

# count no.of.rows & columns

row = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr") # relative xpath
noofrows = len(row)
# print(noofrows)

# Columns will have header
column = driver.find_elements(By.XPATH, "//table[@name='BookTable']//th")
noofcolumns = len(column)
# print(noofcolumns)

# Read specific row & column data

specific_data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]")
print(specific_data.text)

# Read all row & column data

for r in range(2, noofrows+1):
    for c in range(1, noofcolumns+1):
        # Parameterised XPath, which means dynamic xpath. Injecting row & column values.
        data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end = '      ') # this end will represent data in table format
    print()

# Read data based on condition(List book name whose author is Amit)

for rw in range(2, noofrows+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rw)+"]/td[2]").text
    if authorName == "Amit":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rw)+"]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(rw)+"]/td[4]").text
        print(bookName, "      ", authorName, "     ", price)