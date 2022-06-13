from selenium import webdriver
from selenium.webdriver.common.by import By

executable_path = "/usr/local/share/chromedriver"


def run_selenium_test():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    print(driver.title)

    input = driver.find_element(By.CSS_SELECTOR, '#kw')
    input.send_keys('星期五')
    button = driver.find_element(By.CSS_SELECTOR, '#su')
    button.click()

    # driver.close()


if __name__ == '__main__':
    run_selenium_test()
