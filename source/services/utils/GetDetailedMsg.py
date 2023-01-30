# coding: utf8
""" 
@File: GetDetailedMsg.py
@Editor: PyCharm
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2023/1/29 14:22
"""

from source.tools.ToolsMySQL import ConnectMySQL


class GetDetailedMsg(object):
    
    def __init__(self):
        self.connect = ConnectMySQL()
        
    def get_movies_detailed(self, start, num):
        ret_list = []
        sql = """
        select tb_movies_used_info.* from tb_movies_used_info where tb_movies_used_info.is_delete is false limit {}, {} ;
        """.format(start, num)
        # result = self.connect.query(sql=sql)
        for row in self.connect.query(sql=sql):
            movie_detail_dict = {
                'id' : row[0],
                'directors' : row[1],
                'score' : row[2],
                'title' : row[3],
                'actor' : row[4],
                'playbill_url' : row[5],
                'movie_detail_url' : row[6],
                'release_year' : row[7],
                'movie_type' : row[8],
                'movie_country' : row[9],
                'language' : row[10],
                'release_time' : row[11],
                'long' : row[12],
                'short_review_num' : row[13],
                'summary' : row[15],
                'image' : row[17],
                'video' : row[18],
            }
            ret_list.append(movie_detail_dict)
        movie_amount = [row for row in self.connect.query(sql="""
        select count(*) from tb_movies_used_info where tb_movies_used_info.is_delete is false ;
        """)][0][0]
        return ret_list, movie_amount
            # m_id = row[0]
            # directors = row[1]
            # score = row[2]
            # title = row[3]
            # actor = row[4]
            # playbill_url = row[5]
            # movie_detail_url = row[6]
            # release_year = row[7]
            # movie_type = row[8]
            # movie_country = row[9]
            # language = row[10]
            # release_time = row[11]
            # long = row[12]
            # short_review_num = row[13]
            # summary = row[15]
            # image = row[17]
            # video = row[18]
            
