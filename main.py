#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def main():
    # Define driver options
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    # Define driver and service
    service = Service('chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    # Load the webpage
    driver.get('https://demoqa.com/login')

    # Locate the elements on html
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'userName'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'password'))
    )
    login_button = driver.find_element(By.ID, 'login')
    # login_button = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.ID, 'login'))
    # )

    # Fill in elements and click the btn
    username_field.send_key('user name')
    password_field.send_key('my password')
    driver.execute_script("arguments[0].click();", login_button)
    # login_button.click()

    

    input("Press enter to close the browser")
    driver.quit()


if __name__ == "__main__":
    main()
