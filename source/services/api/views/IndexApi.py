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


@Api.route('/get/index/data', methods=['GET'])
def get_index_data():
    result_dict = {
        'Amount': None,
        'ScoreMax': None,
        'ActorMax': None,
        'MovieCountryMax': None,
        'MovieTypeAmount': None,
        'MovieLangMax': None
    }
    index_data = GetIndexDataMysql(limit=1000)
    get_movies_amount = index_data.get_movies_amount()
    get_movies_score_max = index_data.get_movies_score_max()
    get_movies_actor_max = index_data.get_movies_actor_max()
    get_movies_movie_country_max = index_data.get_movies_movie_country_max()
    get_movies_movie_type_amount = index_data.get_movies_movie_type_amount()
    get_movies_movie_lang_max = index_data.get_movies_movie_lang_max()
    result_dict.update(
        Amount=get_movies_amount,
        ScoreMax=get_movies_score_max,
        ActorMax=get_movies_actor_max,
        MovieCountryMax=get_movies_movie_country_max,
        MovieTypeAmount=get_movies_movie_type_amount,
        MovieLangMax=get_movies_movie_lang_max
    )
    return jsonify(result_dict)
    
    
    
    

