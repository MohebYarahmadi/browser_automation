#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def main():
    service = Service('chromedriver-linux64/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get('https://demoqa.com/login')

    input("Press enter to close the browser")
    driver.quit()


if __name__ == "__main__":
    main()
