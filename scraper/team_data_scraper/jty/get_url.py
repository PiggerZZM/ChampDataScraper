from collections.abc import Iterable


def get_url(match_type='zc', years=None):
    if years is None:
        year_ls = ['2017', '2018', '2019', '2021']
    else:
        assert isinstance(years, Iterable)
        year_ls = years
    url_list = []
    if match_type == 'zc':
        match_num = 1
    elif match_type == 'zj':
        match_num = 2
    else:
        print('比赛类型输入错误。')
        return
    for year in year_ls:
        for num in range(30):
            url = 'http://data.champdas.com/match/scheduleDetail-'+str(match_num) + '-' + year + '-' + str(num + 1) + '.html'
            url_list.append(url)
    file = open('gotten_data/url_' + match_type + '.txt', 'w')
    for url in url_list:
        file.write(url + '\n')
    file.close()
    print('链接已存入 gotten_data/url_' + match_type + '.txt 中')
    return url_list

if __name__ == '__main__':
    get_url()