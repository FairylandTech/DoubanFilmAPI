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


if __name__ == '__main__':
    s = time.time()
    limit = 300
    get_index_data = GetIndexData()
    print(get_index_data.get_movies_score_max(limit=limit))
    print(get_index_data.get_movies_actors_max(limit=limit))
    print(get_index_data.get_movies_country_max(limit=limit))
    print(get_index_data.get_movies_type(limit=limit))
    print(time.time() - s)
