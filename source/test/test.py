# coding: utf8
""" 
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 20:32
"""

# from source.tools.DataFormat import DataFormat
from source.services.utils.GetIndexData import GetIndexData
# from source.services.utils.GetSearchData import GetSearchData
from source.services.api.views.DataAnalyse import BaseApi
from settings import Config
import time
from source.services.utils.GetDetailedMsg import GetDetailedMsg
from source.services.utils.GetAnalyseData import GetAnalyseData
import re


if __name__ == '__main__':
    s = time.time()
    limit = 1000
    get_index_data = GetIndexData()
    get_detailed_msg = GetDetailedMsg()
    get_analyse_data = GetAnalyseData()
    # print(get_index_data.get_movies_score_max(limit=limit))
    # print(get_index_data.get_movies_actor_max(limit=limit))
    # print(get_index_data.get_movies_country_max(limit=limit))
    # print(get_index_data.get_movies_type(limit=limit))
    # print(get_index_data.get_movies_languange_max(limit=limit))
    # base_info_types_amount, m_type_echarts_list = get_index_data.get_movies_type(limit=limit)
    # print(base_info_types_amount, m_type_echarts_list)
    # score_max, score_list, score_num_list = get_index_data.get_movies_score_max(num)
    # print(score_max, score_list, score_num_list)
    # print(get_detailed_msg.get_movies_detailed(start=0, num=2))
    # print(get_analyse_data.get_movies_release_year(limit))
    # print(get_analyse_data.get_movies_long(limit))
    m_long_dict = {}
    for row in get_analyse_data.get_movies_long(limit):
        row = row[0]
        print(row)
        row = int(re.findall(r'\d+', row)[0])
        if row < 60:
            if m_long_dict.get('{}'.format('短')):
                m_long_dict['短'] += 1
            else:
                m_long_dict['短'] = 1
        elif 60 < row < 120:
            if m_long_dict.get('{}'.format('中')):
                m_long_dict['中'] += 1
            else:
                m_long_dict['中'] = 1
        elif row > 120:
            if m_long_dict.get('{}'.format('长')):
                m_long_dict['长'] += 1
            else:
                m_long_dict['长'] = 1
    print(type(m_long_dict), m_long_dict)
    print(time.time() - s)
