import logging
from typing import List

from scraper.get_all_match_urls import get_all_match_urls
from scraper.get_json_data import get_match_id, get_json_data

# 日志设置
from scraper.get_team_names import get_team_names
from scraper.json_to_csv import json_to_csv

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


def run(years: List[str]):
    # 获取所有中超中甲比赛详情页url
    match_urls = get_all_match_urls(years)

    ajax_url = "http://data.champdas.com/getMatchStaticListAjax.html"

    for match_url in match_urls:
        # 获取比赛球队名称
        l_team, r_team = get_team_names(match_url)
        # 获取比赛id
        match_id = get_match_id(match_url)
        json_data_list = []
        for half in [0, 1, 2]:
            # 请求"球队数据"
            json_data_list.append(get_json_data(ajax_url, match_id, half, l_team, r_team))
        # 存储
        json_to_csv(json_data_list, file_name=r"match_data.csv")


if __name__ == '__main__':
    years = ["2018", "2019"]
    run(years)
