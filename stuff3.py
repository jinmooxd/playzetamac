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

def solve(lst):
    if "+" in lst:
        return int(lst[0]) + int(lst[4])
    elif "-" in lst:
        return int(lst[0]) - int(lst[4])ther goin
    elif "×" in lst:
        return int(lst[0]) * int(lst[4])
    elif "÷" in lst:
        return int(lst[0]) / int(lst[4])


while(True):
    equation = driver.find_elements(By.XPATH, '//*[@id="game"]/div/div[1]/span')
    answer = solve(equation)
    text_box = driver.find_element(By.XPATH, '//*[@id="game"]/div/div[1]/input')
    text_box.send_keys(answer)