import json
import re
from typing import Dict

import requests
import logging


def get_match_id(match_url: str) -> int:
    """
    获取比赛id
    :param match_url: 比赛详情页的URL
    :return: 比赛id
    """

    return int(re.findall(r"\d+", match_url)[0])


def get_json_data(ajax_url: str, match_id: int, half: int, l_team: str, r_team: str) -> Dict:
    """
    使用POST请求比赛详情页下的"球队数据"
    :param ajax_url: "http://data.champdas.com/getMatchStaticListAjax.html"
    :param match_id: 比赛id
    :param half: 0-全场 1-上半场 2-下半场
    :param l_team: 主场球队名称
    :param r_team: 客场球队名称
    :return: 字典形式存储的json数据
    """

    post_params = {
        "matchId": match_id,
        "half": half,
    }

    json_dict = {}
    try:
        logging.info("get json data: match_id = {}, half = {}".format(match_id, half))
        response = requests.post(ajax_url, post_params)
        response.raise_for_status()
        json_data = response.text
        json_dict = json.loads(json_data)
        json_dict['l_team'] = l_team
        json_dict["r_team"] = r_team
    except requests.RequestException as e:
        logging.warning("get json data failed: match_id = {}, half = {}".format(match_id, half))
        logging.warning(e)

    return json_dict


if __name__ == '__main__':
    json_data = get_json_data("http://data.champdas.com/getMatchStaticListAjax.html", 16333, 2, "大连一方", "北京人和")
    print(json_data)
