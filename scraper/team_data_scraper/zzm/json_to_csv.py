import csv
import logging
from typing import Dict, List


def json_to_csv(json_data_list: List[Dict], file_name: str):
    """
    将请求的json数据写入到csv文件
    :param json_data_list: 以字典形式保存的json数据
    :param file_name: 写入的文件名称
    :return:
    """

    file_path = "../../../data/" + file_name
    with open(file_path, "w", newline='') as csv_file:
        fieldnames = json_data_list[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for json_data in json_data_list:
            try:
                writer.writerow(json_data)
            except ValueError as e:
                logging.warning(json_data)
                logging.warning(e)


if __name__ == '__main__':
    json_to_csv([{"field1": 12, "field2": "banana"}, {"field1": 13, "field2": "apple"}], "test.csv")
