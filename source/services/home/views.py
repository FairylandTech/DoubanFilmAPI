# coding: utf8
""" 
@File: views.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 1:29
"""

from source.services.home import Home
from flask import render_template, request
from source.services.utils.GetIndexData import GetIndexDataMysql
from source.services.utils.GetSearchData import GetSearchData

@Home.route('/index/<int:num>', methods=['GET'])
def index(num):
    movies_amount = num
    
    get_index_data_mysql = GetIndexDataMysql(limit=300)
    movie_amount = get_index_data_mysql.get_movies_amount()
    movie_score_max = get_index_data_mysql.get_movies_score_max()
    movies_actor_max = get_index_data_mysql.get_movies_actor_max()
    movies_movie_country_max = get_index_data_mysql.get_movies_movie_country_max()
    movies_movie_type_amount = get_index_data_mysql.get_movies_movie_type_amount()
    movies_movie_lang_max = get_index_data_mysql.get_movies_movie_lang_max()
    movies_movie_type_echarts_data = get_index_data_mysql.get_movies_movie_type_echarts()
    # movies_score_echarts_data = get_index_data_mysql.get_movies_score_echarts()
    result_score, result_amount = get_index_data_mysql.get_movies_score_echarts()
    movies_data = get_index_data_mysql.get_movies_data()
    return render_template('home/index.html', **locals())


@Home.route('/search/<int:movies_id>', methods=['GET', 'POST'])
def search(movies_id):
    if request.method == 'GET':
        get_search_data = GetSearchData(movie_id=movies_id)
        movie_details_data = get_search_data.get_movies_details_data()
        print(movie_details_data)
        return render_template('home/search.html')
    elif request.method == 'POST':
        pass


