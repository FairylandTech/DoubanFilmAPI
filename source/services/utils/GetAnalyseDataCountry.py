# coding: utf8
""" 
@File: GetAnalyseDataCountry.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/12 22:24
"""

from source.tools.ToolsMySQL import ConnectMySQL


class GetAnalyseDataCountry(object):
    
    def __init__(self):
        self.connect = ConnectMySQL()
    
    def get_movies_country(self, limit):
        sql = """
        select tb_douban_movies.tb_movies_used_info.movie_country
        from tb_douban_movies.tb_movies_used_info
        limit {} ;
        """.format(limit)
        return self.connect.query(sql=sql)

