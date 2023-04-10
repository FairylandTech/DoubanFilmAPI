# coding: utf8
""" 
@File: AnalyseDataCountry.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/12 22:53
"""

from flask import jsonify
from source.services.api import Api
from source.services.api.PublicApi import PublicApi
from source.services.api.views.DataAnalyse.BaseApi import num
from source.services.utils.GetAnalyseDataCountry import GetAnalyseDataCountry

public_api = PublicApi()
get_analyse_data_country = GetAnalyseDataCountry()


@Api.route('/get_country_data', methods=['GET'])
def get_country_data():
    country_info_dict = {}
    movies_country_list = []
    movies_country_number_list = []
    try:
        for row in get_analyse_data_country.get_movies_country(limit=num):
            row[0]: str
            if country_info_dict.get('{}'.format(row[0].split(',')[0])):
                country_info_dict['{}'.format(row[0].split(',')[0])] += 1
            else:
                country_info_dict['{}'.format(row[0].split(',')[0])] = 1
        for key, value in {data[0]: data[1] for data in sorted(country_info_dict.items(), key=lambda x: x[1])}.items():
            movies_country_list.append(key)
            movies_country_number_list.append(value)
        return jsonify(public_api.get_build_response_json(
            code=200,
            data={
                'country_list': movies_country_list,
                'country_number_list': movies_country_number_list
            }
        ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))

