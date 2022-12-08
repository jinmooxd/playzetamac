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

#GETTING REMAINING TIME
""" time = driver.find_elements(By.XPATH, '//*[@id="game"]/span[1]')
remaining_time = re.findall(r'\d+', time)
remaining_time = "".join(remaining_time) """


# GETTING THE EQUATION
""" equation = driver.find_elements(By.XPATH, '//*[@id="game"]/div/div[1]/span') """

#CALCULATING THE ANSWER TO THE EQUATION
""" if "+" in equation:
    answer = eval(equation)
elif "-" in equation:
    answer = eval(equation)
elif "×" in equation:
    x = equation.split()
    answer = x[0] * x[2]
elif "÷" in equation:
    x = equation.split()
    answer = x[0] / x[2] """

#RUNNING THE SCRIPT
text_box = driver.find_element(By.XPATH, '//*[@id="game"]/div/div[1]/input')
action = ActionChains(driver)

""" while int(remaining_time) > 0: """
answer = 0
equation = driver.find_elements(By.XPATH, '//*[@id="game"]/div/div[1]/span')
if "+" in equation:
    answer = eval(equation)
elif "-" in equation:
    answer = eval(equation)
elif "×" in equation:
    x = equation.split()
    answer = x[0] * x[2]
elif "÷" in equation:
    x = equation.split()
    answer = x[0] / x[2]
for i in range(9000):
    action.send_keys_to_element(text_box, answer)








