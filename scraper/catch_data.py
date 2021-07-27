import fileinput
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def catch_detail_data(button, con_one, writer):
    button.click()
    time.sleep(1)
    data = con_one.find_elements_by_class_name('bg_blue')
    action = con_one.find_elements_by_class_name('bg_black')
    for i in range(len(data) // 2):
        writer.writerow([action[i].text, data[i * 2].text, data[i * 2 + 1].text])


def catch_rough_data(tab, browser, name, writer, l_team, r_team):
    tab.click()
    time.sleep(1)
    temp = browser.find_element_by_id('tab2')  # 因为点击了，保险起见重新抓取 球队数据
    con_one = temp.find_element_by_id(name)
    button = con_one.find_elements_by_tag_name('button')  # 全场、上半场、下半场

    writer.writerow([button[0].text, l_team, r_team])
    catch_detail_data(button[0], con_one, writer)
    writer.writerow([button[1].text, l_team, r_team])
    catch_detail_data(button[1], con_one, writer)
    writer.writerow([button[2].text, l_team, r_team])
    catch_detail_data(button[2], con_one, writer)


if __name__ == '__main__':
    browser = webdriver.Edge()

    try:
        csvfile = open('data.csv', 'a', encoding='utf-8')
        writer = csv.writer(csvfile)
        browser.get('http://data.champdas.com/match/data-18010.html')
        # 获取两个队名
        l_team = browser.find_element_by_class_name('l_team').find_element_by_tag_name('p').text
        r_team = browser.find_element_by_class_name('r_team').find_element_by_tag_name('p').text
        # 获取上列表：首发阵容，球队数据，球员数据。。。。
        title = browser.find_elements_by_name('titletab')
        # 取球队数据
        bon = title[1]
        bon.click()
        tab2 = []
        temp = browser.find_element_by_id('tab2')  # 球队数据
        tab2.append(temp.find_element_by_id('one1'))  # 总览
        tab2.append(temp.find_element_by_id('one2'))  # 进攻
        tab2.append(temp.find_element_by_id('one3'))  # 防守

        writer.writerow(['总览'])
        catch_rough_data(tab2[0], browser, 'con_one_1', writer, l_team, r_team)
        writer.writerow(['进攻数据'])
        catch_rough_data(tab2[1], browser, 'con_one_2', writer, l_team, r_team)
        writer.writerow(['防守数据'])
        catch_rough_data(tab2[2], browser, 'con_one_3', writer, l_team, r_team)

    finally:
        browser.close()
        csvfile.close()
