# coding: utf8
""" 
@File: test01.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 20:32
"""

from source.tools.DataFormat import DataFormat
from source.services.utils.GetIndexData import GetIndexData, GetIndexDataMysql
from source.services.utils.GetSearchData import GetSearchData
from settings import Config
import time


if __name__ == '__main__':
    s = time.time()
    # get_index_data = GetIndexData()
    # get_index_data_mysql = GetIndexDataMysql(limit=1000)
    # result_score, result_amount = get_index_data.get_movies_score_echarts()
    # print(result_score)
    # print(result_amount)
    # print(get_index_data_mysql.get_movies_amount())
    # print(get_index_data_mysql.get_movies_score_max())
    # print(get_index_data_mysql.get_movies_actor_max())
    # print(get_index_data_mysql.get_movies_director_max())
    # print(get_index_data_mysql.get_movies_movie_country_max())
    # print(get_index_data_mysql.get_movies_movie_type_amount())
    # print(get_index_data_mysql.get_movies_movie_lang_max())
    # print(get_index_data_mysql.get_movies_movie_type_echarts())
    # print(get_index_data_mysql.get_movies_score_echarts())
    # print(get_index_data_mysql.get_movies_data())
    # print(get_index_data.get_movies_data())
    get_search_data = GetSearchData(1)
    print(get_search_data.get_movies_details_data())
    print(time.time() - s)
