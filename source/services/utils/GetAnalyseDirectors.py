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

class GetAnalyseDirectors:
    
    def __init__(self):
        self.conn = ConnectMySQL()

    def get_analyse_directors(self, limit_num: int):
        sql = """select directors
from tb_movies_used_info
where is_delete is FALSE
limit {} ;""".format(limit_num)
        query_result = self.conn.query(sql=sql)
        # print(query_result)
        return query_result

