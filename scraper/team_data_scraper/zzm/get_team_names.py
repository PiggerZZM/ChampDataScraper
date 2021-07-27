from logging import Logger
from typing import Tuple, Union, Any

import requests
from bs4 import BeautifulSoup


def get_team_names(match_url: str, logger: Logger) -> Tuple[Union[str, Any], Union[str, Any]]:
    """
    获取比赛双方的球队名称
    :param logger: 日志
    :param match_url: 比赛详情页的URL
    :return: 比赛双方的球队名称
    """
    l_team, r_team = "", ""
    try:
        logger.info("get team names: " + match_url)
        response = requests.get(match_url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        l_team = soup.find(class_="l_team").p.text
        r_team = soup.find(class_="r_team").p.text

    except requests.RequestException as e:
        logger.warning("get team names failed: " + match_url)
        logger.warning(e)

    return l_team, r_team
