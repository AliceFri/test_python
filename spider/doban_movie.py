import requests
from bs4 import BeautifulSoup

baseurl = 'https://movie.douban.com/top250?start='


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"网页请求失败，状态码：{res.status_code}")
    return res.text


def parse_result(html):
    soup = BeautifulSoup(html, 'lxml')
    lst = soup.find(class_='grid_view').find_all('li')

    for item in lst:
        try:
            item_name = item.find(class_='title').string
            item_img = item.find('a').find('img').get('src')
            item_index = item.find(class_='').string
            item_score = item.find(class_='rating_num').string
            item_author = item.find('p').text
            item_intr = item.find(class_='inq').string

            # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
            print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)
            yield "%-10s|%-50s|%-5s|%-20s" % (item_index, item_name, item_score, item_intr)
        except Exception as e:
            print(e)


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('record/movie', 'a', encoding='UTF-8') as f:
        f.write(item + '\n')


def request_doban():
    for i in range(0, 250, 25):
        url = baseurl + str(i)
        html = get_page(url)
        for item in parse_result(html):
            write_item_to_file(item)


if __name__ == '__main__':
    request_doban()
