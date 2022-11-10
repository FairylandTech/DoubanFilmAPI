# coding: utf8
""" 
@File: ToolsMySQL.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 18:55
"""

import pymysql
from sqlalchemy import create_engine
from settings import Config


class ConnectMySQL(object):
    
    def __init__(self):
        self.host = Config.RUN_ENV.MYSQL_HOST
        self.port = Config.RUN_ENV.MYSQL_PORT
        self.user = Config.RUN_ENV.MYSQL_USER
        self.password = Config.RUN_ENV.MYSQL_PASSWORD
        self.database = Config.RUN_ENV.MYSQL_DATABASE
        self.charset = Config.RUN_ENV.MYSQL_CHARSET
        
    def connect(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset,
            )
            return conn
        except Exception as error:
            print(error)
            exit(1)


class Query(ConnectMySQL):

    def execute(self, query):
        conn = self.connect()
        cur = conn.cursor()
        try:
            cur.execute(query=query)
            result = cur.fetchall()
            cur.close()
            conn.close()
            return result
        except Exception as error:
            return error


class CreateEngine(object):
    
    def __init__(self):
        pass
    
    def conn_engine(self):
        return create_engine(url='mysql+pymysql://{}:{}@{}:{}/{}?charset={}'.format(
            Config.RUN_ENV.MYSQL_USER,
            Config.RUN_ENV.MYSQL_PASSWORD,
            Config.RUN_ENV.MYSQL_HOST,
            Config.RUN_ENV.MYSQL_PORT,
            Config.RUN_ENV.MYSQL_DATABASE,
            Config.RUN_ENV.MYSQL_CHARSET
        ))

