# coding: utf8
""" 
@File: AnalyseDataApi.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/1 2:23
"""

from source.services.api import Api
from flask import jsonify, request
from source.services.api.PublicApi import PublicApi
from source.services.utils.GetAnalyseData import GetAnalyseData
from source.services.api.views.DataAnalyse.BaseApi import num

public_api = PublicApi()
get_analyse_data = GetAnalyseData()

@Api.route('/movies_year_ratio', methods=['GET'])
def movies_year_ratio():
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



