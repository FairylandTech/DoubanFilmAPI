# coding: utf8
""" 
@File: main.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 1:43
"""

from source.services.core.CoreServer import run

if __name__ == '__main__':
    run(debug=False, host='0.0.0.0')
