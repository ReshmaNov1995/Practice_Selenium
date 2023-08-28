from selenium import webdriver

def headless_chrome():
    from webdriver_manager.microsoft import EdgeChromiumDriverManager
    from selenium.webdriver.edge.service import Service

    chrome_option = webdriver.EdgeOptions()
    chrome_option.add_experimental_option("detach", True)
    chrome_option.headless=True # headless mode

    driver = webdriver.Chrome(service=Service(EdgeChromiumDriverManager().install()), options=chrome_option)
    return driver

driver = headless_chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
