from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)

driver.get("https://text-compare.com/")

driver.maximize_window()

# CTRL+A
# CTRL+C
# TAB
# CTRL+V

field1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']").send_keys("Hello Reshma")
field2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

act = ActionChains(driver)

# CTRL+A
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# CTRL+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# TAB
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
# element = driver.find_element(By.XPATH, "")
# act.send_keys_to_element(element,"Hi")

# CTRL+V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


# act.key_down(Keys.CONTROL)
# act.send_keys(Keys.END)
# act.key_up(Keys.CONTROL)
# act.perform()
