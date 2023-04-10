# coding: utf8
""" 
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 20:32
"""

from source.services.utils.GetIndexData import GetIndexData
from source.services.api.views.DataAnalyse import BaseApi
from settings import Config
import time
from source.services.utils.GetDetailedMsg import GetDetailedMsg
from source.services.utils.GetAnalyseDataTime import GetAnalyseData
import re
from source.services.utils.GetAnalyseDataScore import GetAnalyseDataScore
from source.services.utils.GetAnalyseDataCountry import GetAnalyseDataCountry


def get_analyse_directors(limit_num: int):
    from source.services.utils.GetAnalyseDirectors import GetAnalyseDirectors
    get_analyse_directors = GetAnalyseDirectors()
    result = get_analyse_directors.get_analyse_directors(limit_num)
    directors = []
    for row in result:
        row: str = row[0]
        if ',' in row:
            director_list = row.split(',')
            directors += director_list
        else:
            directors.append(row)
    print(directors)
    return 


if __name__ == '__main__':
    s = time.time()
    limit = 400

    print(get_analyse_directors(limit_num=limit))
    
    # get_analyse_data_country = GetAnalyseDataCountry()
    # country_info_dict = {}
    # movies_country_list = []
    # movies_country_number_list = []
    # for row in get_analyse_data_country.get_movies_country(limit=limit):
    #     row[0]: str
    #     if country_info_dict.get('{}'.format(row[0].split(',')[0])):
    #         country_info_dict['{}'.format(row[0].split(',')[0])] += 1
    #     else:
    #         country_info_dict['{}'.format(row[0].split(',')[0])] = 1
    # for key, value in {data[0]: data[1] for data in sorted(country_info_dict.items(), key=lambda x: x[1])}.items():
    #     movies_country_list.append(key)
    #     movies_country_number_list.append(value)
    print(time.time() - s)
