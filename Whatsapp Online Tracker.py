#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import os
driver = webdriver.Chrome(r'chromedriver.exe')

# Load Whatsapp Web page
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 60)

name="Contact"

while True:

    try:
        chat=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div")
        chat.click()
        time.sleep(2)
        search=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]')
        search.click()
        print("client")
        time.sleep(2)
        search.send_keys(name)
        print("found")
        time.sleep(2)
        open=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div")
        open.click()
        time.sleep(2)


        while True:
            try:
                status = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]/span').text
                print("status \n")
                print("{0}".format(status))
                now = datetime.now()

                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)
                time.sleep(10)
            except:
                pass


    except:
            pass
