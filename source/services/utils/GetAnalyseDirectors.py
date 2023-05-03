# coding: utf8
""" 
@ File: GetAnalyseDirectors.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-09
"""

import sys

sys.dont_write_bytecode = True

from source.tools.ToolsMySQL import ConnectMySQL
from collections import Counter


class GetAnalyseDirectors:

    def __init__(self):
        self.conn = ConnectMySQL()

    def get_analyse_directors(self, limit_num: int):
        sql = """select directors
from tb_movies_used_info
where is_delete is FALSE
limit {} ;""".format(limit_num)
        query_result = self.conn.query(sql=sql)
        directors = []
        for row in query_result:
            row: str = row[0]
            if ',' in row:
                director_list = row.split(',')
                directors += director_list
            else:
                directors.append(row)
        sort_dict = dict(sorted(Counter(directors).items(), key=lambda x: x[1], reverse=True)[:10])
        return sort_dict
    
    
    def get_analyse_directors_movies(self, director_name: str, amount_num: int):
        sql = """select id, directors,title, playbill_link, detail_link
from tb_movies_used_info
where is_delete is false
and directors like '%{}%'
limit {} ;""".format(director_name, amount_num)
        query_result = self.conn.query(sql=sql)
        result_list = []
        for row in query_result:
            result_list.append({'directors': row[1], 'title': row[2], 'playbill_link': row[3], 'detail_link': row[4]})
        return result_list

