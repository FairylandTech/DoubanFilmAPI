# coding: utf8
""" 
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/23 22:26
"""

from source.services.api import Api
from flask import jsonify
from source.services.core import CoreServer


@Api.route('/t')
def test():
    CoreServer.db.reflect()
    all_table = {table_obj.name: table_obj for table_obj in CoreServer.db.get_tables_for_bind()}
    # 获取demo表的所有数据
    all_data = CoreServer.db.session.query(all_table['tb_movies_used_info'])
    data_1 = ''
    for data in all_data:
        print(data)  # 查看数据
        data_1 = data
        break
    # 将字典转换成json数据
    return str(data_1)
