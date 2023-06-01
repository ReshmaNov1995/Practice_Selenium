from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

a = webdriver.ChromeOptions()
a.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=a)


driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()

search = driver.find_element(By.XPATH, "//input[@id='srchword']")
attribute = search.get_attribute("type")
print(attribute)
