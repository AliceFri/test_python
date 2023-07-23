# import requests
# import execjs
#
# asw = execjs.compile(open('b.js', 'r', encoding='utf-8').read()).call('main123')
# print(asw)
# cookies = {
#     'SECKEY_ABVK': 'BnXBT9IjYzcbB8cR5/TEF2m8HJFrkjz+dU0AYQfMa9c%3D',
#     'BMAP_SECKEY': 'fP3Q3XLm7TckJRMTAolX9tL3iuNDHkUJjpO3JYSvkw9ozlamIbC9MDWPC0Xmo0qds9c9RshCGNyYBqjxExa1u4H7gfoSEou4xwlDjDVrepJjLHguP0LPW7ctJdbZW2qRo6Qm2VtshBhPKP_1TFmJB6KMcpNZ3jWe2X7RijsSxvI',
#     'acw_tc': '2760823716775167032583334edef67111b41fa791333ad0f777b686f64622',
#     # 'acw_sc__v2': '63fce554695e617e22e29f9b86289de84407bc1c',
#     'acw_sc__v2': asw,
#     '_WEB_page_type': 'web',
#     '_WEB_city_code': 'sh',
#     '_WEB_token': 'IfmH4VXFLnpfE2-ZL-2H_Jtfxp0VgSOuJT3BLpOz3z7IOxurPvYoH8qXJ0ub1kffLDgAv0vNo98wloyV5o4KKg==',
#     '_WEB_USER_ID': '1677518165708571',
#     '_WEB_city_name': '%E4%B8%8A%E6%B5%B7',
#     '_WEB_cityid': '2',
#     '_WEB_ip_cityCode': 'sz',
#     '_WEB_ip_cityName': '%E6%B7%B1%E5%9C%B3',
#     'Hm_lvt_8d409b931bc5e2ac53a0cea966f06d99': '1677512045,1677516533,1677518166',
#     'Hm_lpvt_8d409b931bc5e2ac53a0cea966f06d99': '1677518166',
#     'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218693dfd9d556-01f618dcd02bd36-12462c6d-2073600-18693dfd9d766b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2218693dfd9d556-01f618dcd02bd36-12462c6d-2073600-18693dfd9d766b%22%7D',
#     'sajssdk_2015_cross_new_user': '1',
#     '_ga': 'GA1.2.1568183015.1677518167',
#     '_gid': 'GA1.2.540133355.1677518167',
#     '_gat_gtag_UA_119236000_1': '1',
# }
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     # 'Cookie': 'SECKEY_ABVK=BnXBT9IjYzcbB8cR5/TEF2m8HJFrkjz+dU0AYQfMa9c%3D; BMAP_SECKEY=fP3Q3XLm7TckJRMTAolX9tL3iuNDHkUJjpO3JYSvkw9ozlamIbC9MDWPC0Xmo0qds9c9RshCGNyYBqjxExa1u4H7gfoSEou4xwlDjDVrepJjLHguP0LPW7ctJdbZW2qRo6Qm2VtshBhPKP_1TFmJB6KMcpNZ3jWe2X7RijsSxvI; acw_tc=2760823716775167032583334edef67111b41fa791333ad0f777b686f64622; acw_sc__v2=63fce554695e617e22e29f9b86289de84407bc1c; _WEB_page_type=web; _WEB_city_code=sh; _WEB_token=IfmH4VXFLnpfE2-ZL-2H_Jtfxp0VgSOuJT3BLpOz3z7IOxurPvYoH8qXJ0ub1kffLDgAv0vNo98wloyV5o4KKg==; _WEB_USER_ID=1677518165708571; _WEB_city_name=%E4%B8%8A%E6%B5%B7; _WEB_cityid=2; _WEB_ip_cityCode=sz; _WEB_ip_cityName=%E6%B7%B1%E5%9C%B3; Hm_lvt_8d409b931bc5e2ac53a0cea966f06d99=1677512045,1677516533,1677518166; Hm_lpvt_8d409b931bc5e2ac53a0cea966f06d99=1677518166; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218693dfd9d556-01f618dcd02bd36-12462c6d-2073600-18693dfd9d766b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%7D%2C%22%24device_id%22%3A%2218693dfd9d556-01f618dcd02bd36-12462c6d-2073600-18693dfd9d766b%22%7D; sajssdk_2015_cross_new_user=1; _ga=GA1.2.1568183015.1677518167; _gid=GA1.2.540133355.1677518167; _gat_gtag_UA_119236000_1=1',
#     'Referer': 'https://sh.esfxiaoqu.zhuge.com/page2/',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
# }
#
# response = requests.get('https://sh.esfxiaoqu.zhuge.com/page2/', cookies=cookies, headers=headers)
# print(response.text)

import requests

if __name__ == '__main__':
    a = requests.get('chrome://gpu')
    # a = requests.get('http://www.baodu.com')
    print(a.text)