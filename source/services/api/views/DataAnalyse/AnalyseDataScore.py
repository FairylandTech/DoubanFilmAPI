# coding: utf8
""" 
@File: AnalyseDataScore.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/2 2:26
"""

from source.services.api.PublicApi import PublicApi
from source.services.api import Api
from flask import request, jsonify
from source.services.api.views.DataAnalyse.BaseApi import num
from source.services.utils.GetAnalyseDataScore import GetAnalyseDataScore


public_api = PublicApi()
get_analyse_data_score = GetAnalyseDataScore()

@Api.route('/movies_types_scores_ratio', methods=['GET', 'POST'])
def get_movies_types_scores_ratio():
    if request.method == 'GET':
        m_type_list = []
        for row_index, row in enumerate(get_analyse_data_score.get_movies_types(limit=num)):
            row: str = row[0]
            for m_type in [m_type for m_type in row.split(',')]:
                m_type_list.append(m_type)
        m_type_list = set(m_type_list)
        m_type_list = list(m_type_list)
        try:return jsonify(public_api.get_build_response_json(
            code=200,
            data={'movies_type': m_type_list}
        ))
        except Exception as error:
            return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    if request.method == 'POST':
        req_type = request.form.get('m_type')
        # print(req_type)
        m_type_score_dict = {}
        m_type_score = []
        m_type_num = []
        for row_index, row in enumerate(get_analyse_data_score.get_movies_types_score(limit=num, m_type=req_type)):
            # print(row[0])
            if m_type_score_dict.get('{}'.format(row[0])):
                m_type_score_dict['{}'.format(row[0])] += 1
            else:
                m_type_score_dict['{}'.format(row[0])] = 1
        m_type_score_dict = {data[0]: data[1] for data in sorted(m_type_score_dict.items(), key=lambda x: x[0])}
        for key, value in m_type_score_dict.items():
            m_type_score.append(key)
            m_type_num.append(value)
        try:return jsonify(public_api.get_build_response_json(
            code=200,
            data={
                'score': m_type_score,
                'score_num': m_type_num
            }
        ))
        except Exception as error:
            return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))


