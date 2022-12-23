# IMPORTING LIBRARIES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import time
from selenium.webdriver.common.action_chains import ActionChains
import re


#CREATING FUNCTIONS
def solve(equation):
    if "+" in equation:
        x = equation.split()
        answer = int(x[0]) + int(x[2])
        return answer
    elif "–" in equation:
        x = equation.split()
        answer = int(x[0]) - int(x[2])
        return answer
    elif "×" in equation:
        x = equation.split()
        answer = int(x[0]) * int(x[2])
        return answer
    elif "÷" in equation:
        x = equation.split()
        answer = int(x[0]) // int(x[2])
        return answer

def PlayZetamac(driver):
    eq = driver.find_elements(By.XPATH, '//*[@id="game"]/div/div[1]/span')
    if not eq:
        return False
    ans = solve(eq[0].text)
    text_box = driver.find_element(By.XPATH, '//*[@id="game"]/div/div[1]/input')
    try:
        text_box.send_keys(ans)
    except ElementNotInteractableException:
        return False
    return True



def main():    
    #LOADING UP THE WEBSITE
    s = Service("/Users/yoojinmoo/Desktop/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://arithmetic.zetamac.com/")

    #CLICKING ON THE START BUTTON
    link = driver.find_element(By.XPATH, '//*[@id="welcome"]/form/input')
    link.click()
    driver.implicitly_wait(5)

    while(PlayZetamac(driver)):
        print("in while loop")
        pass
    
    time.sleep(30)

if __name__ == "__main__":
    main()
