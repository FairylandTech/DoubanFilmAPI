# coding: utf8
""" 
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/23 22:26
"""

from source.services.api import Api
from flask import jsonify, request
from source.services.core import CoreServer
from source.services.utils.GetIndexData import GetIndexData
from source.services.api.PublicApi import PublicApi

get_index_data = GetIndexData()
public_api = PublicApi()

@Api.route('/test', methods=['GET'])
def test():
    try:
        num = request.args.get('num')
        # print(num)
        if num is None:
            num = 500
        print(type(num))
        return jsonify(public_api.get_build_response_json(
        code=200,
        data=[num, get_index_data.test()],
        msg='测试通过'
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(
            msg='{}'.format(error)
        ))
    pass
