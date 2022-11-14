# coding: utf8
""" 
@File: IndexApi.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 2:37
"""

from source.services.api import Api
from flask import jsonify
from source.services.utils.GetIndexData import GetIndexDataMysql
from source.services.api.views.PublicApi import PublicApi

public_api = PublicApi()
index_data = GetIndexDataMysql(limit=10)

@Api.route('/get/index/data', methods=['GET'])
def get_index_data():
    try:
        data_dict = {
            'Amount': None,
            'ScoreMax': None,
            'ActorMax': None,
            'MovieCountryMax': None,
            'MovieTypeAmount': None,
            'MovieLangMax': None
        }
        get_movies_amount = index_data.get_movies_amount()
        get_movies_score_max = index_data.get_movies_score_max()
        get_movies_actor_max = index_data.get_movies_actor_max()
        get_movies_movie_country_max = index_data.get_movies_movie_country_max()
        get_movies_movie_type_amount = index_data.get_movies_movie_type_amount()
        get_movies_movie_lang_max = index_data.get_movies_movie_lang_max()
        data_dict.update(
            Amount=get_movies_amount,
            ScoreMax=get_movies_score_max,
            ActorMax=get_movies_actor_max,
            MovieCountryMax=get_movies_movie_country_max,
            MovieTypeAmount=get_movies_movie_type_amount,
            MovieLangMax=get_movies_movie_lang_max
        )
        public_api.get_build_response_json(code=200, msg='Successful', data=data_dict)
        return jsonify(public_api.get_build_response_json())
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())
    
@Api.route('/get/index/echarts/data', methods=['GET'])
def get_index_echarts_data():
    try:
        data_dict = {
            'MovieTypeEcharts': None,
            'MovieScoreEcharts': None
        }
        movie_type_echarts = index_data.get_movies_movie_type_echarts()
        movie_score_echarts = index_data.get_movies_score_echarts()
        data_dict.update(MovieTypeEcharts=movie_type_echarts, MovieScoreEcharts=movie_score_echarts)
        public_api.get_build_response_json(code=200, msg='Successful', data=data_dict)
        return jsonify(public_api.get_build_response_json())
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())



