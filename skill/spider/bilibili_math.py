from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

executable_path = "/usr/local/share/chromedriver"
bilibili = "https://www.bilibili.com/"


def parse_bilibili(soup):
    lst = soup.find(class_='video-list row').find_all(class_='video-list-item')
    for item in lst:
        try:
            title = item.find('h3').get('title')
            # author = item.find(class_='bili-video-card__info--author').text
            # date = item.find(class_='bili-video-card__info--date').text
            # data = item.find(class_='bili-video-card__stats').text
            yield {"title": title}
        except Exception as e:
            continue


def request_bilibili():
    driver = webdriver.Chrome(executable_path)
    driver.get(bilibili)
    print(driver.title)

    input = driver.find_element(By.CLASS_NAME, 'nav-search-input')
    input.send_keys('高考语文')
    button = driver.find_element(By.CLASS_NAME, 'nav-search-btn')
    button.click()
    driver.switch_to.window(driver.window_handles[1])

    new_page(driver)


def new_page(driver):
    print('跳转到新的窗口')
    WAIT = WebDriverWait(driver, 10)
    try:
        sleep(3)
        WAIT.until(
            EC.text_to_be_present_in_element(
                (
                    By.XPATH,
                    '//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div/button[10]',
                )
            )
        )
        WAIT.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div/button[10]',
                )
            )
        )
        button = driver.find_element(
            By.XPATH,
            '//*[@id="i_cecream"]/div[1]/div[1]/div[2]/div/div/div[3]/div/div/button[10]',
        )
    except Exception as e:
        print('retry ---------')
        driver.refresh()
        new_page(driver)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    for item in parse_bilibili(soup):
        print(item)

    # 下一页

    if button:
        print('---- new page ----')
        button.click()
        new_page(driver)
    else:
        print('---- end ----')
        driver.close()


if __name__ == '__main__':
    request_bilibili()
