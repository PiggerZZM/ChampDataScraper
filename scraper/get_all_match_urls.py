from typing import List

import requests
import logging
from bs4 import BeautifulSoup

# 日志设置
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")


def get_schedule_detail_url(base_url: str, match: str, year: str, round: str) -> str:
    return base_url + "/match/" + "scheduleDetail-" + match + "-" + year + "-" + round + ".html"


def get_match_url(base_url: str, other: str) -> str:
    return base_url + other


def get_all_match_urls() -> List[str]:
    base_url = "http://data.champdas.com"
    years = ["2018", "2019"]
    rounds = [str(i) for i in range(1, 31)]
    matches = ["1", "2"]
    match_urls = []

    for year in years:
        for round in rounds:
            for match in matches:
                # 请求
                schedule_detail_url = get_schedule_detail_url(base_url, match, year, round)
                response = requests.get(schedule_detail_url)
                if response.status_code == 200:
                    # 解析
                    html = response.text
                    soup = BeautifulSoup(html, "lxml")
                    match_note_list = soup.find_all(name="span", class_="matchNote")
                    for match_note in match_note_list:
                        other = match_note.a["href"]
                        match_url = get_match_url(base_url, other)
                        match_urls.append(match_url)
                else:
                    logging.warning(response.status_code)
                    logging.warning(schedule_detail_url)
    return match_urls


if __name__ == '__main__':
    match_urls = get_all_match_urls()
