# coding: utf8
""" 
@File: DataFormat.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 20:07
"""

import pandas
from source.tools.ToolsMySQL import CreateEngine


class DataFormat(object):
    
    def __init__(self):
        self.conn_engine = CreateEngine().conn_engine()
        
    def data_matrix(self):
        sql_query = "select tb_douban_movies.tb_movies_used_info_bak_all.id, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.directors, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.score, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.title, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.actors, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.playbill_link, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.detail_link, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.release_year, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.movie_type, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.movie_country, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.movie_lang, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.release_time, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.movie_long, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.short_review_num, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.star_compare, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.summary, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.movie_review, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.about_img_url, " \
                    "tb_douban_movies.tb_movies_used_info_bak_all.movie_url " \
                    "from tb_douban_movies.tb_movies_used_info_bak_all " \
                    "where tb_douban_movies.tb_movies_used_info_bak_all.is_delete = false " \
                    "limit 50 ;"
        return pandas.read_sql(sql=sql_query, con=self.conn_engine)

    def data_format_to_list(self, field):
        if field == 'score':
            data = self.data_matrix()[f'{field}'].map(lambda x:float(x)).values
            data.sort()
            return data
        else:
            data = self.data_matrix()[f'{field}'].values
            data = list(map(lambda x: x.split(','), data))
            data_list = []
            for row in data:
                for element in row:
                    data_list.append(element)
            return data_list
        
