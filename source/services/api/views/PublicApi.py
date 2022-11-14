# coding: utf8
""" 
@File: PublicApi.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 2:37
"""

class BuildResponseJson(object):
    result_dict = {
        'code': 500,
        'msg': 'Fault',
        'data': None,
        'remark': None,
    }


class PublicApi(object):
    
    def __init__(self):
        self.build_response_json = BuildResponseJson() 
        pass
    
    def get_build_response_json(self):
        return self.build_response_json.result_dict
        


