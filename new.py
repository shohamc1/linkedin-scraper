from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import json

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
driver.get('https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scroll to bottom

#names = driver.find_elements_by_xpath("//div[contains(@id, 'ember')]") #finding elements starting with ember

#for name in names:
    #namevar = name.find_element_by_class_name('name')
#    namevar = name.find_element_by_xpath("//span[contains(@class, 'actor-name')]")
#    print (namevar.text)

soup = bs(driver.page_source, features = "html.parser")


data = soup.select("code[id*=bpr-guid]")
#print (data)

for datas in data:
    if datas.get_text().find("searchId") != -1:
        #put search stuff here
        print ("Hello")
        
        #with open('data.json', 'w') as datafile:
        #    datafile.writelines(datas.get_text())
