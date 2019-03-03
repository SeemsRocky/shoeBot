import time
from selenium import webdriver

#driver = webdriver.Chrome(executable_path=r'C:\Users\baymax\Downloads\chromedriver.exe')
#driver = webdriver.Firefox(executable_path=r'C:\Users\baymax\Downloads\geckodriver.exe')

def chooseBrowser(browser):
    if(browser=="firefox"):
        return webdriver.Firefox(executable_path=r'C:\Users\baymax\Downloads\geckodriver.exe')
    if(browser=="chrome"):
        return webdriver.Chrome(executable_path=r'C:\Users\baymax\Downloads\chromedriver.exe')


def login(driver):
    login = driver.find_element_by_class_name("join-log-in")
    login.click()

    username = 'damitzmehxd@gmail.com'
    password = 'Nikepls123'

    emailInput = driver.find_element_by_name("emailAddress")
    emailInput.clear()
    emailInput.send_keys(username)


    passwordInput = driver.find_element_by_name("password")
    passwordInput.clear()
    passwordInput.send_keys(password)
    time.sleep(3)

    loginBtn = driver.find_element_by_xpath('//*[@value="LOG IN"]')
    loginBtn.click()
    time.sleep(10)

#------------------------------------------------------------
# program calls for bot
driver = chooseBrowser('chrome')
driver.get('https://nike.com/launch/')

driver.maximize_window()
login(driver)
driver.quit()