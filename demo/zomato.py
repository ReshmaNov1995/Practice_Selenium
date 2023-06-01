from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def zomato_rating(client_name,ratings):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("detach", True)
    serv = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=serv, options=chrome_options)
    driver.get("https://demo.wpjobboard.net/wp-admin/admin.php?page=wpjb-application")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//*[@id='wp-submit']").click()
    rows = driver.find_elements(By.XPATH, "//*[@id='the-list']//tr")
    row_len = len(rows)
    print("Rows count is:", row_len)
    column = driver.find_elements(By.XPATH,
                                  "//*[@id='the-list']//tr[@class='alternate   author-self status-publish iedit ']//td")
    column_len = len(column)
    print("Columns count is:", column_len)

    for i in range(1, row_len + 1):
        for j in range(1, column_len + 1):
            values = driver.find_element(By.XPATH, "//*[@id='the-list']//tr[" + str(i) + "]//td[" + str(j) + "]")
            print(values.text, end=" ")
        print()

    for i in range(1, row_len + 1):
        client = driver.find_element(By.XPATH, "//*[@id='the-list']//tr[" + str(i) + "]//td[2]").text
        # print(client)

        if client_name in client:
            print("The "+client_name+" present in " + str(i) + " row ")
            client_row = i
    # print(emily_row)
    for i in range(1, ratings + 1):
        driver.find_element(By.XPATH,
                            "//*[@id='the-list']//tr[" + str(client_row) + "]//*[@data-value='" + str(i) + "']").click()



zomato_rating("Dick", 3)



