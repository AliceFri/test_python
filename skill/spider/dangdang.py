import json
import re

import requests

baseurl = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"网页请求失败，状态码：{res.status_code}")
    return res.text


def parse_result(html):
    pattern = re.compile(
        '<li.*?list_num.*?(\d+)\.</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">(.*?)</span>.*?</li>',
        re.S,
    )
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'range': item[0],
            # 'image': item[1],
            'title': item[2],
            # 'recommend': item[3],
            'author': item[4],
            # 'times': item[5],
            # 'price': item[6],
        }


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('record/book', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def request_dangdang():
    for i in range(1, 26):
        url = baseurl + str(i)
        html = get_page(url)
        for item in parse_result(html):
            write_item_to_file(item)


if __name__ == '__main__':
    request_dangdang()
