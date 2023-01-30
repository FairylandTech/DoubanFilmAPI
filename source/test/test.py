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


if __name__ == '__main__':
    s = time.time()
    limit = 300
    get_index_data = GetIndexData()
    get_detailed_msg = GetDetailedMsg()
    # print(get_index_data.get_movies_score_max(limit=limit))
    # print(get_index_data.get_movies_actor_max(limit=limit))
    # print(get_index_data.get_movies_country_max(limit=limit))
    # print(get_index_data.get_movies_type(limit=limit))
    # print(get_index_data.get_movies_languange_max(limit=limit))
    # base_info_types_amount, m_type_echarts_list = get_index_data.get_movies_type(limit=limit)
    # print(base_info_types_amount, m_type_echarts_list)
    # score_max, score_list, score_num_list = get_index_data.get_movies_score_max(num)
    # print(score_max, score_list, score_num_list)
    print(get_detailed_msg.get_movies_detailed(start=0, num=2))
    
    print(time.time() - s)
