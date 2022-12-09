from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

driver.maximize_window()

# CSS Selector
# 1) tag & id tagname#valueofid input#email
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")

# Can also use value as #email by ignoring tagname
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

# 2) tag & class tagname.valueofclass
# driver.find_element(By.CSS_SELECTOR, "input.inputtext _55r1 _6luy").send_keys("xyz") #In value, after space the characters will be ignored. So, Refer below
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("xyz")

# Can also use value as .inputtext by ignoring tagname
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("xyz")

# 3) tag & attribute tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("ijk")

# Can also use value as [data-testid=royal_email] by ignoring tagname
# driver.find_element(By.CSS_SELECTOR, "[data-testid=royal_email]").send_keys("ijk")

# 4) tag, class & attribute tagname.valueofclass[attribute=value]
# driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("pqr")

# Can also use value as .inputtext[data-testid=royal_pass] by ignoring tagname
driver.find_element(By.CSS_SELECTOR, ".inputtext[data-testid=royal_pass]").send_keys("pqr")