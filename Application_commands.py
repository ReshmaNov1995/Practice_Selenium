from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

pagetitle = driver.title
print(pagetitle)

pageurl = driver.current_url
print(pageurl)

pagesource = driver.page_source
print(pagesource)