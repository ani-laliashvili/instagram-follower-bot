from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = 'C:\\PATH\\chromedriver.exe'
SIMILAR_ACCOUNT = 'balenciaga'
USERNAME = 'MYUSERNAME'
PASSWORD = 'MYPASSWORD'

## Login
driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
driver.get('https://www.instagram.com/')
time.sleep(6)
driver.maximize_window()
username = driver.find_element(By.NAME, 'username')
username.send_keys(USERNAME)

password = driver.find_element(By.NAME, 'password')
password.send_keys(PASSWORD)

driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
time.sleep(5)

try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/main/div/div/div/div/button').click()
    time.sleep(5)
except:
    print('')


try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
    time.sleep(5)
except:
    print('')

## Find Followers
driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}')
time.sleep(5)

driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a/div').click()
time.sleep(5)

to_follow = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[1]/div/div[2]/button')
to_follow = driver.find_elements(By.CSS_SELECTOR, 'div._aano ul div li div div._aaes button')

scr1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')

for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
    time.sleep(2)

## Follow users discovered    
for user in to_follow:
    try:
        user.click()
    except():
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()

    time.sleep(2)


driver.quit()
