# coding: utf8
""" 
@ File: AnalyseDirectors.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-09
"""

import sys

sys.dont_write_bytecode = True

from flask import jsonify
from source.services.api.PublicApi import PublicApi
from source.services.api import Api
from source.services.utils.GetAnalyseDirectors import GetAnalyseDirectors
from source.services.api.views.DataAnalyse.BaseApi import num
from flask import request

public_api = PublicApi()
get_analyse_directors = GetAnalyseDirectors()


@Api.route('/directors', methods=['GET'])
def directors():
    try:
        result = get_analyse_directors.get_analyse_directors(limit_num=num)
        return jsonify(public_api.get_build_response_json(
            code=200,
            data=result
        ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(
            code=500,
            msg='{}'.format(error)
        ))


@Api.route('/directors_movies', methods=['GET'])
def get_directors_movies_details():
    try:
        name = request.args.get('name')
        num = request.args.get('num')
        if name is None or num is None:
            return jsonify(public_api.get_build_response_json(
                code=500,
                msg='参数错误'
            ))
        details = get_analyse_directors.get_analyse_directors_movies(director_name=name, amount_num=int(num))
        return jsonify(public_api.get_build_response_json(
            code=200,
            data={'details': details}
        ))
    except Exception as error:
        jsonify(public_api.get_build_response_json(
            code=500,
            msg='{}'.format(error)
        ))
