# coding: utf8
""" 
@File: GetSearchData.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/10 22:18
"""

from source.services.utils.GetIndexData import GetIndexDataMysql

class GetSearchData(object):
    
    def __init__(self, movie_id):
        self.movie_id = movie_id
        self.get_index_data_mysql = None
        
    def instantiation_get_index_data_mysql(self):
        self.get_index_data_mysql = GetIndexDataMysql()
        return self.get_index_data_mysql
    
    def get_movies_details_data(self):
        for row in self.instantiation_get_index_data_mysql().data:
            if self.movie_id == row[0]:
                return row

