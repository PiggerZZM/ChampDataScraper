import requests
from bs4 import BeautifulSoup

base_url = "http://data.champdas.com"

def catch_url_year(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    spans = soup.find_all(class_='matchNote')
    # size=8

    if spans:
        for span in spans:
            a = span.find(name='a')
            if a:
                href = a.get('href')
                file = open('zc_url.txt', 'a', encoding='utf-8')
                file.write(base_url + href + '\n')
                file.close()


def catch_url_two(num):
    file = open('zc_url.txt', 'a', encoding='utf-8')
    if num == 1:
        file.write("\nzc\n")
    else:
        file.write("\nzj\n")
    file.close()
    for year in range(2016, 2022):
        for round in range(1, 31):
            url = "http://data.champdas.com/match/scheduleDetail-" + str(num) + "-" + str(year) + "-" + str(
                round) + ".html"
            catch_url_year(url)
            print(num, '-', year, '-', round)


if __name__ == '__main__':
    catch_url_two(1)

    catch_url_two(2)


