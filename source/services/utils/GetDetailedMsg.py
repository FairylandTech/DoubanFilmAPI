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
        select tb_movies_used_info.directors,
            tb_movies_used_info.score,
            tb_movies_used_info.title,
            tb_movies_used_info.actors,
            tb_movies_used_info.playbill_link,
            tb_movies_used_info.detail_link,
            tb_movies_used_info.release_year,
            tb_movies_used_info.movie_type,
            tb_movies_used_info.movie_country,
            tb_movies_used_info.movie_lang,
            tb_movies_used_info.release_time,
            tb_movies_used_info.movie_long,
            tb_movies_used_info.short_review_num,
            tb_movies_used_info.summary,
            tb_movies_used_info.movie_url
        from tb_movies_used_info
        where tb_movies_used_info.is_delete is false
        limit {}, {} ;
        """.format(start, num)
        for row_index, row in enumerate(self.connect.query(sql=sql)):
            movie_detail_dict = {
                # Id
                'id' : row_index + 1,
                # 导演
                'directors' : row[0],
                # 评分
                'score' : row[1],
                # 电影名称
                'title' : row[2],
                # 参与演员
                'actor' : row[3],
                # 海报
                'playbill_url' : row[4],
                # 电影详情url
                'movie_detail_url' : row[5],
                # 发行年份
                'release_year' : row[6],
                # 电影类型
                'movie_type' : row[7],
                # 拍摄国家
                'movie_country' : row[8],
                # 语言
                'language' : row[9],
                # 上映时间
                'release_time' : row[10],
                # 电影时长
                'long' : row[11],
                # 短评数量
                'short_review_num' : row[12],
                # 电影简介
                'summary' : row[13],
                # 预告片
                'video' : row[14],
            }
            if movie_detail_dict.get('video') == '':
                movie_detail_dict['video'] = movie_detail_dict.get('playbill_url')
            ret_list.append(movie_detail_dict)
        movie_amount = [row for row in self.connect.query(sql="""
        select count(*) from tb_movies_used_info where tb_movies_used_info.is_delete is false ;
        """)][0][0]
        return ret_list, movie_amount



