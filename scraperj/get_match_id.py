import re
from time import sleep
import requests


def get_match_id(url_list, match_type='zc'):
    match_id_list = []
    pattern = re.compile(r'match/data-(\d+).html', re.S)
    count = 1
    all = len(url_list)
    for url in url_list:
        print('正在爬取 {} 中的比赛id，完成{}/{}'.format(url, count, all))
        count += 1
        response = requests.get(url)
        match_id = list(set(re.findall(pattern, response.text)))
        match_id_list.extend(match_id)
        sleep(1)
    match_id_list = [int(m_id) for m_id in match_id_list]
    match_id_list.sort()
    match_id_list = [str(m_id) for m_id in match_id_list]
    file = open('gotten_data/id_' + match_type + '.txt', 'w')
    for url in match_id_list:
        file.write(url + '\n')
    file.close()
    print('完成，比赛id已存入 gotten_data/id_' + match_type + '.txt')
    return match_id_list

if __name__ == '__main__':
    url_list = open('gotten_data/url_zc.txt').readlines()
    get_match_id(url_list)
