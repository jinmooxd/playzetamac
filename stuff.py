# IMPORTING LIBRARIES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import re

#LOADING UP THE WEBSITE
s = Service("/Users/yoojinmoo/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://arithmetic.zetamac.com/")

#CLICKING ON THE START BUTTON
link = driver.find_element(By.XPATH, '//*[@id="welcome"]/form/input') 
link.click()
driver.implicitly_wait(5)

#RUNNING THE SCRIPT
""" text_box = driver.find_element(By.XPATH, '//*[@id="game"]/div/div[1]/input') """
""" action = ActionChains(driver) """

while(True):
    equation = driver.find_elements(By.XPATH, '//*[@id="game"]/div/div[1]/span')
    while equation:
        if "+" in equation:
            lst = equation.split()
            answer = int(lst[0]) + int(lst[2]) 
        elif "-" in equation:
            lst = equation.split()
            answer = int(lst[0]) - int(lst[2]) 
        elif "×" in equation:
            lst = equation.split()
            answer = int(lst[0]) * int(lst[2]) 
        elif "÷" in equation:
            lst = equation.split()
            answer = int(lst[0]) / int(lst[2]) 
    text_box = driver.find_element(By.XPATH, '//*[@id="game"]/div/div[1]/input')
    text_box.send_keys(answer)
    

