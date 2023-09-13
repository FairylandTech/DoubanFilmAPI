# coding: utf8
""" 
@File: AnalyseDataScore.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/2 2:26
"""

import json
from source.services.api.PublicApi import PublicApi
from source.services.api import Api
from flask import request, jsonify
from source.services.api.views.DataAnalyse.BaseApi import num
from source.services.utils.GetAnalyseDataScore import GetAnalyseDataScore


public_api = PublicApi()
get_analyse_data_score = GetAnalyseDataScore()

@Api.route('/movies_types_scores_ratio', methods=['GET', 'POST'])
def get_movies_types_scores_ratio():
    """
    电影类型评分
    :return: 
    """
    if request.method == 'GET':
        m_type_list = []
        # 每条数据
        for row_index, row in enumerate(get_analyse_data_score.get_movies_types(limit=num)):
            row: str = row[0]
            # 类型分割
            for m_type in [m_type for m_type in row.split(',')]:
                m_type_list.append(m_type)
        # set去重
        m_type_list = set(m_type_list)
        m_type_list = list(m_type_list)
        # 构建返回的json数据
        try:return jsonify(public_api.get_build_response_json(
            code=200,
            data={'movies_type': m_type_list}
        ))
        except Exception as error:
            return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    if request.method == 'POST':
        # 取前端传来的值
        req_data: dict = json.loads(bytes.decode(request.data, encoding='utf-8'))
        req_type = req_data.get('m_type')
        m_type_score_dict = {}
        m_type_score = []
        m_type_num = []
        # 查询某一个类型的数据
        for row_index, row in enumerate(get_analyse_data_score.get_movies_types_score(limit=num, m_type=req_type)):
            # 统计类型出现的个数
            if m_type_score_dict.get('{}'.format(row[0])):
                m_type_score_dict['{}'.format(row[0])] += 1
            else:
                m_type_score_dict['{}'.format(row[0])] = 1
        # 类型个数排序
        m_type_score_dict = {data[0]: data[1] for data in sorted(m_type_score_dict.items(), key=lambda x: x[0])}
        for key, value in m_type_score_dict.items():
            m_type_score.append(key)
            m_type_num.append(value)
            # 构建返回json数据
        try:return jsonify(public_api.get_build_response_json(
            code=200,
            data={
                'score': m_type_score,
                'score_num': m_type_num
            }
        ))
        except Exception as error:
            return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))


