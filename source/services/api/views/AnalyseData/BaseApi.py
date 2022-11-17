# coding: utf8
""" 
@File: BaseApi.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 2:37
"""

from source.services.api import Api
from flask import jsonify
from source.services.utils.GetIndexData import GetIndexDataMysql
from source.services.api.PublicApi import PublicApi

public_api = PublicApi()
index_data = GetIndexDataMysql(limit=1000)


@Api.route('/base_info_amount', methods=['GET'])
def base_info_amount():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'moviesAmount': index_data.get_movies_amount()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())


@Api.route('/base_info_score_max', methods=['GET'])
def base_info_score_max():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'scoreMax': index_data.get_movies_score_max()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())


@Api.route('/base_info_actor_max', methods=['GET'])
def base_info_actor_max():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'actorMax': index_data.get_movies_actor_max()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())


@Api.route('/base_info_country_max', methods=['GET'])
def base_info_country_max():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'countryMax': index_data.get_movies_country_max()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())


@Api.route('/base_info_type_amount', methods=['GET'])
def base_info_type_amount():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'typeAmount': index_data.get_movies_type_amount()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())


@Api.route('/base_info_languages_max')
def base_info_languages_max():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'languagesMax': index_data.get_movies_languages_max()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())


@Api.route('/echarts_info_movies_type', methods=['GET'])
def echarts_info_movies_type():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[{'moviesType': index_data.get_movies_type_echarts()}]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())
    
    
@Api.route('/echarts_info_movies_score', methods=['GET'])
def echarts_info_movies_score():
    try:
        return jsonify(
            public_api.get_build_response_json(
                code=200,
                data=[
                    {'moviesScore': index_data.get_movies_score_echarts()[0]},
                    {'moviesAmount': index_data.get_movies_score_echarts()[1]}
                ]
            )
        )
    except Exception as error:
        print(error)
        return jsonify(public_api.get_build_response_json())

