import requests
from bs4 import BeautifulSoup
import lxml
import logging

# 日志设置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

if __name__ == '__main__':
    # 请求
    url = "http://data.champdas.com/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.status_code)
        logging.debug("请求成功")

    # 解析
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    if soup is not None:
        logging.debug("解析成功")

    # 保存
    with open(r'../data/result.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
        logging.debug("保存成功")
