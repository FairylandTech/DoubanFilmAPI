# coding: utf8
""" 
@File: AnalyseDataTime.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/1 2:23
"""

from source.services.api import Api
from flask import jsonify, request
from source.services.api.PublicApi import PublicApi
from source.services.utils.GetAnalyseDataTime import GetAnalyseData
from source.services.api.views.DataAnalyse.BaseApi import num
import re

public_api = PublicApi()
get_analyse_data = GetAnalyseData()

@Api.route('/movies_year_ratio', methods=['GET'])
def get_movies_year_ratio():
    m_year_dict = {}
    ret_year_list = []
    ret_year_num_list = []
    for row in get_analyse_data.get_movies_release_year(limit=num):
        row: int = row[0]
        if m_year_dict.get('{}'.format(row)):
            m_year_dict['{}'.format(row)] += 1
        else:
            m_year_dict['{}'.format(row)] = 1
    m_year_dict = {data[0]: data[1] for data in sorted(m_year_dict.items(), key=lambda x:x[0])}
    for key, value in m_year_dict.items():
        ret_year_list.append(key)
        ret_year_num_list.append(value)
    try:
        return jsonify(public_api.get_build_response_json(
            code=200,
            data={'year': ret_year_list, 'year_number': ret_year_num_list}
        ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/movies_long_ratio', methods=['GET'])
def get_movies_long_ratio():
    m_long_dict = {
        '长': 0,
        '中': 0,
        '短': 0
    }
    for row_index, row in enumerate(get_analyse_data.get_movies_long(limit=num)):
        m_long = int(re.findall(r'\d+', row[0])[0])
        if m_long <= 60:
            m_long_dict['短'] += 1
        elif 60 < m_long < 120:
            m_long_dict['中'] += 1
        elif m_long >= 120:
            m_long_dict['长'] += 1
    ret_list = []
    for key, value in m_long_dict.items():
        ret_list.append({'name': key, 'value': value})
    try:return jsonify(public_api.get_build_response_json(
        code=200,
        data={'long_ratio': ret_list}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))



