import logging
from typing import Tuple, Union, Any

import requests
from bs4 import BeautifulSoup


def get_team_names(match_url: str) -> Tuple[Union[str, Any], Union[str, Any]]:
    """
    获取比赛双方的球队名称
    :param match_url: 比赛详情页的URL
    :return: 比赛双方的球队名称
    """
    l_team, r_team = "", ""
    try:
        logging.info("get team names: " + match_url)
        response = requests.get(match_url)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        l_team = soup.find_all(class_="l_team")[0].p.text
        r_team = soup.find_all(class_="r_team")[0].p.text

    except requests.RequestException as e:
        logging.warning("get team names failed: " + match_url)
        logging.warning(e)

    return l_team, r_team
