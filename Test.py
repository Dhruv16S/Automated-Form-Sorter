from selenium import webdriver
from selenium.webdriver.common.keys import Keys #can be used to replicate keyword functions like enter, tab

import tkinter
window = tkinter.Tk()
window.minsize(height = 500, width = 700)
def Begin():
    chrome_driver_path= "C:/Chrome Driver/chromedriver"
    driver = webdriver.Chrome(executable_path = chrome_driver_path)
    driver.get("https://accounts.google.com/signin/v2/identifier?service=writely&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    login = driver.find_element_by_id("identifierId")
    emailid = "dscuderiaferrari@gmail.com"
    login.send_keys(emailid)
    next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
    next_button.click()

button = tkinter.Button(text = "Click", command = Begin).pack()
window.mainloop()

# login2 = driver.find_elements_by_css_selector("whsOnd zHQkBf")
# print(login2)
# name, attribute
# driver.close() 
# driver.quit() #Entire program is closed
# driver.find_element_by_id
#if everything fails use xpath
# login2 = driver.find_element_by_xpath('//*[@id="identifierId"]')
# print(login2)