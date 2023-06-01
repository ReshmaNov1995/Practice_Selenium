from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_Options)


driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

driver.maximize_window()

# self
textmessage = driver.find_element(By.XPATH, "//a[contains(text(),'YES Bank Ltd.')]/self::a").text
print(textmessage)

# parent
textmessage = driver.find_element(By.XPATH, "//td[text()='1,949.70']/parent::tr").text
print(textmessage)

# child
textmessage = driver.find_element(By.XPATH, "//div[@class='floatL']/a/child::span").text
print(textmessage)

# ancestor
textmessage = driver.find_element(By.XPATH, "//a[contains(text(),'Jubilant Pharmova')]/ancestor::tr").text
print(textmessage)

# descendant
textmessage = driver.find_element(By.XPATH, "//ul[@class='ul_top_tabs']/descendant::li[2]/a").text
print(textmessage)

# following
following = driver.find_elements(By.XPATH, "//ul[@class='ul_top_tabs']/following::div")
print(len(following))

# following-sibling
fsibling = driver.find_elements(By.XPATH, "//div[@class='toplogobar']/following-sibling::*")
print(len(fsibling))

# preceding
preceding = driver.find_elements(By.XPATH, "//ul[@class='ul_top_tabs floatL']/li[4]/preceding::li")
print(len(preceding))

# preceding-sibling
psibling = driver.find_elements(By.XPATH, "//ul[@class='ul_top_tabs floatL']/li[4]/preceding-sibling::*")
print(len(psibling))