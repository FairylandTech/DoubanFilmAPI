# coding: utf8
""" 
@File: GetAnalyseDataScore.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/2/2 1:33
"""

from source.tools.ToolsMySQL import ConnectMySQL


class GetAnalyseDataScore:

    def __init__(self):
        self.connect = ConnectMySQL()

    def get_movies_types(self, limit):
        m_type_sql = """
        select tb_douban_movies.tb_movies_used_info.movie_type
        from tb_douban_movies.tb_movies_used_info
        where tb_douban_movies.tb_movies_used_info.is_delete is false
        limit {} ;
        """.format(limit)
        return self.connect.query(sql=m_type_sql)
    
    def get_movies_types_score(self, limit, m_type):
        m_type_score_sql = """
        select temp.score
        from (select tb_douban_movies.tb_movies_used_info.movie_type,
            tb_douban_movies.tb_movies_used_info.score
            from tb_douban_movies.tb_movies_used_info
            where tb_douban_movies.tb_movies_used_info.is_delete is false
            limit {}) as temp
        where temp.movie_type like '%{}%' ;
        """.format(limit, m_type)
        return self.connect.query(sql=m_type_score_sql)
