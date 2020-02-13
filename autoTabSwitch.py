# -*- coding: utf-8 -*-

"""
Created on Thu Feb 13 18:35:02 2020

@author: Sakshamdeep Singh
"""

import time
from selenium import webdriver

def setOptions():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    #options.add_argument("user-data-dir=C:\\Users\\Saksham\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    return options
    
def setDriver(options):
    path_to_chromedriver = r'C:\Users\Saksham\Desktop\auto tab switch\chromedriver.exe'
    driver = webdriver.Chrome(options = options, executable_path = path_to_chromedriver)
    return driver

def startTab(tab, url):
    driver.execute_script("window.open('{}', '{}');".format(url, tab))
    driver.switch_to.window(tab)
    time.sleep(3)

def startAutoSwitch():
    # Sensor API Service tab
    driver.get('https://stackoverflow.com/questions/')
    time.sleep(10)          # time needed to enter the password
    '''
    username = driver.find_element_by_id("login_id")
    password = driver.find_element_by_id("login_password")
    username.send_keys("my_username")
    password.send_keys("my_password")
    driver.find_element_by_name("submit").click()
    '''
    startTab('tab2', 'https://www.cricbuzz.com/')
    startTab('tab3', 'https://www.geeksforgeeks.org/')
    startTab('tab4', 'https://www.youtube.com/')
    
    #switching starts here
    while True:
        Windows = driver.window_handles
        for window in Windows:
            driver.refresh()
            driver.switch_to.window(window)
            time.sleep(15)
        
if __name__ == '__main__':
    options = setOptions()
    driver = setDriver(options)
    try:
        startAutoSwitch()
    except:
        print('Exception Caught or Browser Closed')

