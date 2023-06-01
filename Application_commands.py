from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_Options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

pagetitle = driver.title
print(pagetitle)

pageurl = driver.current_url
print(pageurl)

pagesource = driver.page_source
print(pagesource)