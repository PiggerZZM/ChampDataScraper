from logging import Logger

from scraper.get_all_match_urls import get_all_match_urls
from scraper.get_json_data import get_match_id, get_json_data

# 日志设置
from scraper.get_logger import get_logger
from scraper.get_team_names import get_team_names
from scraper.json_to_csv import json_to_csv


def run(year: str, match: str, logger: Logger):
    # 获取所有比赛详情页url
    match_urls = get_all_match_urls(year, match, logger)

    ajax_url_static = "http://data.champdas.com/getMatchStaticListAjax.html"
    ajax_url_attack = "http://data.champdas.com/getMatchAttackAjax.html"
    ajax_url_defence = "http://data.champdas.com/getMatchDefencesRateAjax.html"

    json_data_list_static = []
    json_data_list_attack = []
    json_data_list_defence = []

    for match_url in match_urls:
        # 获取比赛球队名称
        l_team, r_team = get_team_names(match_url, logger)
        # 获取比赛id
        match_id = get_match_id(match_url)
        for half in [0, 1, 2]:
            # 请求"球队数据"
            json_data_list_static.append(get_json_data(ajax_url_static, match_id, half, l_team, r_team, logger))
            json_data_list_attack.append(get_json_data(ajax_url_attack, match_id, half, l_team, r_team, logger))
            json_data_list_defence.append(get_json_data(ajax_url_defence, match_id, half, l_team, r_team, logger))
    # 存储
    json_to_csv(json_data_list_static, file_name=r"match_data_static_{}_{}.csv".format(match, year))
    json_to_csv(json_data_list_attack, file_name=r"match_data_attack_{}-{}.csv".format(match, year))
    json_to_csv(json_data_list_defence, file_name=r"match_data_defence_{}-{}.csv".format(match, year))


if __name__ == '__main__':
    years = ["2017", "2018", "2019", "2020"]
    matches = ["1", "2"]
    for year in years:
        for match in matches:
            logger = get_logger(year, match)
            run(year, match, logger)
