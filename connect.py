from selenium import webdriver
import time
#from bs4 import BeautifulSoup as bs
import json
import sys


def add_people (uri):
    with open('accountinfo.json') as f:
        accountinfo = json.load(f)
        email = accountinfo['email']
        psk = accountinfo['password']

    driver = webdriver.Firefox(executable_path=r'C:\Users\Shoham\Downloads\geckodriver-v0.26.0-win64\geckodriver.exe')
    driver.get('https://www.linkedin.com/')
    time.sleep(5)
    username = driver.find_element_by_name('session_key')
    username.send_keys(email)
    password = driver.find_element_by_name('session_password')
    password.send_keys(psk)
    loginbutton = driver.find_element_by_class_name('sign-in-form__submit-btn')
    loginbutton.click()
    driver.get(uri)

    buttons = driver.find_elements_by_xpath('//button[text()="Connect"]')

    for button in buttons:
        button.click()
        try:
            driver.find_element_by_xpath('//span[text()="Send now"]').click() #to handle prompt
        except:
            print ('Send now button not found')

        print ('Clicked button')

    buttons = driver.find_elements_by_xpath('//span[text()="Connect"]')

    for button in buttons:
        button.click()
        try:
            driver.find_element_by_xpath('//span[text()="Send now"]').click() #to handle prompt
        except:
            print ('Send now button not found')

        print ('Clicked button')

if __name__ == "__main__":
    uri = str(sys.argv[1])
    add_people(uri)