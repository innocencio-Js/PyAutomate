from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

accounts = [
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'},
    {'username': 'account name', 'password': 'abc123abc'}
            ]

dice_credits = 'Dice Credits Remaining for each account\n'

driver = webdriver.Chrome()

for account in accounts:
    time.sleep(3)
    
    driver.get("https://www.dice.com/employer/login/")

    email_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys(account['username'])
    password_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
    password_input.send_keys(account['password'])
    login_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/main/div[2]/form/button')))
    login_button.click()

    number_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/dhi-root/div[2]/div[1]/div[2]/dhi-profile-views/div/span[1]')))
    number = number_element.text

    dice_credits += account['username'] + " :" + number + "\n"

    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "user-name")))
    element.click()
    element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-cy="logoutButton"]')))
    element.click()

today_date = datetime.date.today().strftime('%d%b')
path = r"C:\Users\USER\OneDrive\Desktop\PyAutomate\DiceCredits{}.txt".format(today_date)

with open(path, "w") as f:
    f.write(dice_credits)
#print(dice_credits)

driver.quit()

