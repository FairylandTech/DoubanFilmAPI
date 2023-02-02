# coding: utf8
""" 
@File: GetAnalyseDataTime.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/1 2:25
"""

from source.tools.ToolsMySQL import ConnectMySQL


class GetAnalyseData(object):
    
    def __init__(self):
        self.connect_mysql = ConnectMySQL()
        
    def get_movies_release_year(self, limit):
        sql = """
        select tb_movies_used_info.release_year from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ; 
        """.format(limit)
        return self.connect_mysql.query(sql=sql)
        
    def get_movies_long(self, limit):
        sql = """
        select tb_movies_used_info.movie_long from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {} ;
        """.format(limit)
        return self.connect_mysql.query(sql=sql)


