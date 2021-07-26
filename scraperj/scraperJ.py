import requests
from time import sleep
import pandas as pd
import sys
sys.path.append("..")
from get_url import get_url
from get_match_id import get_match_id
from bs4 import BeautifulSoup
from deal_data import deal_data

base_url = 'http://data.champdas.com/match/data-{}.html'

def get_team(match_id):
    response = requests.get(base_url.format(match_id))
    assert response.status_code == 200
    html = BeautifulSoup(response.text, "lxml")
    l_team = html.select('#content > section > div:nth-child(1) > div > div.l_team > p')[0].get_text()
    r_team = html.select('#content > section > div:nth-child(1) > div > div.r_team > p')[0].get_text()
    return {'主场': l_team, '客场': r_team}


def get_match_data(match_id_list, match_type='zc'):
    assert match_type in ['zc', 'zj']
    all = len(match_id_list)
    count = 0
    url_DefencesRate = 'http://data.champdas.com/getMatchDefencesRateAjax.html'
    url_Attack = 'http://data.champdas.com/getMatchAttackAjax.html'
    url_Static = 'http://data.champdas.com/getMatchStaticListAjax.html'
    cate_dict = {url_Static: '总览',
                 url_Attack: '进攻数据',
                 url_DefencesRate: '防守数据'}
    stage_dict = {'0': '常规全场',
                  '1': '上半场',
                  '2': '下半场'}
    url_list = [url_Static, url_Attack, url_DefencesRate]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    match_data = dict()
    for match_id in match_id_list:
        print('开始爬取id为 ' + match_id + ' 的比赛数据')
        try:
            if match_data.get(match_id) is None:
                match_data[match_id] = dict()
            if match_data[match_id].get('队伍') is None:
                match_data[match_id]['队伍'] = dict()
                team_dict = get_team(match_id)
                match_data[match_id]['队伍'] = team_dict
            for url in url_list:
                print('正在爬取 {}'.format(cate_dict[url]))
                if match_data[match_id].get(cate_dict[url]) is None:
                    match_data[match_id][cate_dict[url]] = dict()
                for half in ['0', '1', '2']:
                    if match_data[match_id][cate_dict[url]].get(stage_dict[half]) is None:
                        match_data[match_id][cate_dict[url]][stage_dict[half]] = dict()
                    data = {
                        'matchId': match_id,
                        'half': half
                    }
                    response = eval(requests.post(url, headers=headers, data=data).text)
                    file = open('gotten_data/source_'+match_type+'.txt', 'a')
                    file.write(str(response) + '\n')
                    file.close()
                    match_data[match_id][cate_dict[url]][stage_dict[half]] = deal_data(response, team_dict)
                    sleep(0.5)
            print('爬取id为 '+match_id + ' 的比赛数据成功了, 完成情况 ' + '{}/{}'.format(count + 1, all))
            count += 1
            file = open('gotten_data/succeed_'+match_type+'.txt', 'a')
            file.write(match_id + '\n')
            file.close()
        except:
            print('爬取id为 '+match_id + ' 的比赛数据失败了, 完成情况 ' + '{}/{}'.format(count + 1, all))
            count += 1
            file = open('gotten_data/fail_' + match_type + '.txt', 'a')
            file.write(match_id + '\n')
            file.close()
    return match_data



if __name__ == '__main__':
    for t in ['zc', 'zj']:
        if t == 'zc':
            continue
        url_list = get_url(t)
        id_list = get_match_id(url_list, t)
        data = get_match_data(id_list, t)
        file = open('gotten_data/data_' + t + '.txt', 'w')
        file.write(str(data))
        file.close()
        pd.DataFrame(data).to_csv('gotten_data/data_' + t + '.csv', encoding='utf-8-sig')
        print(t+'已经存入gotten_data')














