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
from source.services.utils.GetAnalyseDataTime import GetAnalyseData
import re
from source.services.utils.GetAnalyseDataScore import GetAnalyseDataScore


if __name__ == '__main__':
    s = time.time()
    limit = 300
    get_index_data = GetIndexData()
    get_detailed_msg = GetDetailedMsg()
    get_analyse_data = GetAnalyseData()
    get_analyse_data_score = GetAnalyseDataScore()
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
    # 时间分析法
    # m_long_dict = {
    #     '长': 0,
    #     '中': 0,
    #     '短': 0
    # }
    # for row_index, row in enumerate(get_analyse_data.get_movies_long(limit)):
    #     m_long = int(re.findall(r'\d+', row[0])[0])
    #     if m_long <= 60:
    #         m_long_dict['短'] += 1
    #     elif 60 < m_long < 120:
    #         m_long_dict['中'] += 1
    #     elif m_long >= 120:
    #         m_long_dict['长'] += 1
    # ret_list = []
    # for key, value in m_long_dict.items():
    #     ret_list.append({'name': key, 'value': value})
    # print(ret_list)
    # print(type(m_long_dict))
    # 评分分析法
    m_type_list = []
    for row_index, row in enumerate(get_analyse_data_score.get_movies_types(limit=limit)):
        row: str = row[0]
        for m_type in [m_type for m_type in row.split(',')]:
            m_type_list.append(m_type)
    m_type_list = set(m_type_list)
    m_type_list = list(m_type_list)
    m_type_score_dict = {}
    m_type_score = []
    m_type_num = []
    for row_index, row in enumerate(get_analyse_data_score.get_movies_types_score(limit=limit, m_type='喜剧')):
        # print(row[0])
        if m_type_score_dict.get('{}'.format(row[0])):
            m_type_score_dict['{}'.format(row[0])] += 1
        else:
            m_type_score_dict['{}'.format(row[0])] = 1
    m_type_score_dict = {data[0]: data[1] for data in sorted(m_type_score_dict.items(), key=lambda x: x[0])}
    for key, value in m_type_score_dict.items():
        m_type_score.append(key)
        m_type_num.append(value)
    print(m_type_score, m_type_num)
    print(len(m_type_score), len(m_type_num))
    print(time.time() - s)
