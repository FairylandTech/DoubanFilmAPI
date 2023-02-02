# coding: utf8
""" 
@File: BaseApi.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 2:37
"""

from source.services.api import Api
from flask import jsonify, request
from source.services.utils.GetIndexData import GetIndexData
from source.services.api.PublicApi import PublicApi
from source.services.utils.GetDetailedMsg import GetDetailedMsg

public_api = PublicApi()
get_index_data = GetIndexData()
get_detailed_msg = GetDetailedMsg()
num = 300
m_type_echarts_list = None
score_list = None
score_num_list = None

# index_data = GetIndexDataMysql()


# @Api.before_app_first_request
# def before_app_first_request():
#     global index_data
#     index_data = GetIndexDataMysql()


# @Api.route('/data_range', methods=['POST'])
# def data_range():
#     global index_data
#     try:
#         start = int(request.form.get('start'))
#         end = int(request.form.get('end'))
#     except Exception as error:
#         return jsonify(public_api.get_build_response_json(
#             msg='{}'.format(error)
#         ))
#     index_data = GetIndexDataMysql(limit_s=start, limit_e=end)
#     return jsonify(public_api.get_build_response_json(code=200))
# 
# 
# @Api.route('/base_info_amount', methods=['GET'])
# def base_info_amount():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'moviesAmount': index_data.get_movies_amount()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/base_info_score_max', methods=['GET'])
# def base_info_score_max():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'scoreMax': index_data.get_movies_score_max()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/base_info_actor_max', methods=['GET'])
# def base_info_actor_max():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'actorMax': index_data.get_movies_actor_max()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/base_info_country_max', methods=['GET'])
# def base_info_country_max():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'countryMax': index_data.get_movies_country_max()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/base_info_type_amount', methods=['GET'])
# def base_info_type_amount():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'typeAmount': index_data.get_movies_type_amount()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/base_info_languages_max')
# def base_info_languages_max():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'languagesMax': index_data.get_movies_languages_max()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/echarts_info_movies_type', methods=['GET'])
# def echarts_info_movies_type():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[{'moviesType': index_data.get_movies_type_echarts()}]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/echarts_info_movies_score', methods=['GET'])
# def echarts_info_movies_score():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[
#                 {'moviesScore': index_data.get_movies_score_echarts()[0]},
#                 {'moviesAmount': index_data.get_movies_score_echarts()[1]}
#             ]
#         ))
#     except Exception as error:
#         print(error)
#         return jsonify(public_api.get_build_response_json())
# 
# 
# @Api.route('/base_info_data', methods=['GET'])
# def base_info_data():
#     try:
#         return jsonify(public_api.get_build_response_json(
#             code=200,
#             data=[
#                 {'moviesAmount': index_data.get_movies_amount()},
#                 {'scoreMax': index_data.get_movies_score_max()},
#                 {'actorMax': index_data.get_movies_actor_max()},
#                 {'countryMax': index_data.get_movies_country_max()},
#                 {'typeAmount': index_data.get_movies_type_amount()},
#                 {'languagesMax': index_data.get_movies_languages_max()},
#                 {'moviesType': index_data.get_movies_type_echarts()},
#                 {'moviesScore': [
#                     {'moviesScore': index_data.get_movies_score_echarts()[0]},
#                     {'moviesAmount': index_data.get_movies_score_echarts()[1]}
#                 ]}
#             ]
#         ))
#     except Exception as error:
#         return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))

@Api.route('/base_info_amount', methods=['GET'])
def base_info_amount():
    global num
    try:
        if request.args.get('num') is None:
            num = 300
        else:
            num = request.args.get('num')
        return jsonify(public_api.get_build_response_json(
            code=200,
            data={'movies_amount': num}
        ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))

@Api.route('/base_info_score_max', methods=['GET'])
def base_info_score_max():
    global score_list, score_num_list
    try:
        score_max, score_list, score_num_list = get_index_data.get_movies_score_max(num)
        return jsonify(public_api.get_build_response_json(
        code=200,
        data={'movies_score_max': score_max}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/base_info_actor_max', methods=['GET'])
def base_info_actor_max():
    try:return jsonify(public_api.get_build_response_json(
        code=200,
        data={'movies_actors_max': get_index_data.get_movies_actor_max(num)}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/base_info_countrys_max', methods=['GET'])
def base_info_countrys_max():
    try:return jsonify(public_api.get_build_response_json(
        code=200,
        data={'movies_countrys_max': get_index_data.get_movies_country_max(num)}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/base_info_types_amount', methods=['GET'])
def base_info_types_amount():
    global m_type_echarts_list
    try:
        base_info_types_amount, m_type_echarts_list = get_index_data.get_movies_type(limit=num)
        return jsonify(public_api.get_build_response_json(
        code=200,
        data={'movies_types_amount': base_info_types_amount}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/base_info_languages_max')
def base_info_languages_max():
    try:return jsonify(public_api.get_build_response_json(
        code=200,
        data={'movies_languages_max': get_index_data.get_movies_languange_max(num)}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/echarts_info_movies_type')
def echarts_info_movies_type():
    try:return jsonify(public_api.get_build_response_json(
        code=200,
        data={'m_type_echarts': m_type_echarts_list}
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('echarts_info_movies_score')
def echarts_info_movies_score():
    try:return jsonify(public_api.get_build_response_json(
        code=200,
        data={
            'score': score_list,
            'score_num': score_num_list
        }
    ))
    except Exception as error:
        return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    
@Api.route('/movies_details_msg', methods=['GET', 'POST'])
def movies_details_msg():
    if request.method == 'GET':
        page_num = request.args.get('page')
        amount = request.args.get('num')
        if page_num is None or amount is None:
            return jsonify(public_api.get_build_response_json(msg='{}'.format('接口参数异常')))
        try:
            start_num = (int(page_num) - 1) * int(amount)
            movies_details_list, movies_amount = get_detailed_msg.get_movies_detailed(start=start_num, num=amount)
            return jsonify(public_api.get_build_response_json(
                code=200,
                data=[{'details_list': movies_details_list},{'movies_amount': movies_amount}]
            ))
        except Exception as error:
            return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))
    if request.method == 'POST':
        try:
            pass
        except Exception as error:
            return jsonify(public_api.get_build_response_json(msg='{}'.format(error)))


