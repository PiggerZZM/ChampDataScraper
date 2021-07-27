import pandas as pd
import sys
sys.path.append("../../..")
from scraper.team_data_scraper.jty.get_url import get_url
from scraper.team_data_scraper.jty.get_match_id import get_match_id
from scraper.team_data_scraper.jty.get_data import get_match_data


if __name__ == '__main__':
    for t in ['zc', 'zj']:
        url_list = get_url(t)
        id_list = get_match_id(url_list, t)
        data = get_match_data(id_list, t)
        file = open('gotten_data/data_' + t + '.txt', 'w')
        file.write(str(data))
        file.close()
        pd.DataFrame(data).to_csv('gotten_data/data_' + t + '.csv', encoding='utf-8-sig')
        print(t+'已经存入gotten_data')















