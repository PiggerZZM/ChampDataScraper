from logging import Logger
from typing import List

import requests
from bs4 import BeautifulSoup


def get_schedule_detail_url(base_url: str, match: str, year: str, round: str) -> str:
    """
    拼接比赛赛程页的URL
    :param base_url: "http://data.champdas.com"
    :param match: 1或2，表示中超或中甲
    :param year: 赛季
    :param round: 轮数
    :return: 比赛赛程页的URL
    """

    return base_url + "/match/" + "scheduleDetail-" + match + "-" + year + "-" + round + ".html"


def get_match_url(base_url: str, other: str) -> str:
    """
    拼接比赛详情页的URL
    :param base_url: "http://data.champdas.com"
    :param other: 包括比赛id号
    :return: 比赛详情页的URL
    """

    return base_url + other


def get_all_match_urls(year: str, match: str, logger: Logger) -> List[str]:
    """
    获取所有比赛详情页的URL
    :param logger: 日志
    :param year: 赛季
    :param match: 中超或中甲
    :return: 所有比赛详情页的URL
    """

    base_url = "http://data.champdas.com"
    rounds = [str(i) for i in range(1, 31)]
    match_urls = []

    for round in rounds:
        # 请求
        schedule_detail_url = get_schedule_detail_url(base_url, match, year, round)
        try:
            logger.info("get schedule detail url: " + schedule_detail_url)
            response = requests.get(schedule_detail_url)
            response.raise_for_status()
            # 解析
            html = response.text
            soup = BeautifulSoup(html, "lxml")
            match_note_list = soup.find_all(name="span", class_="matchNote")
            for match_note in match_note_list:
                other = match_note.a["href"]
                match_url = get_match_url(base_url, other)
                match_urls.append(match_url)
        except requests.RequestException as e:
            logger.warning("get schedule detail url failed: " + schedule_detail_url)
            logger.warning(e)

    return match_urls

