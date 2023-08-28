import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

chrome_option = webdriver.EdgeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(EdgeChromiumDriverManager().install()), options = chrome_option)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

driver.maximize_window()

min_slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
max_slider = driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")

print("Location of Min Slider before moving ", min_slider.location) # {'x': 59, 'y': 250}
print("Location of max slider before moving", max_slider.location) # {'x': 612, 'y': 250}

act = ActionChains(driver)
# increment
act.drag_and_drop_by_offset(min_slider, 150, 0).perform() # 0 is a default value, Graphwise value Positive
# decrement
act.drag_and_drop_by_offset(max_slider, -40, 0).perform() # Graphwise value Negative

print("Location of Min Slider after moving ", min_slider.location) # {'x': 209, 'y': 250}
print("Location of max slider after moving", max_slider.location) # {'x': 574, 'y': 250} 2 is diff but it has taken the nearby values.

