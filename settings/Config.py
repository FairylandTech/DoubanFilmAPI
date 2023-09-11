# coding: utf8
""" 
@File: Config.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 3:10
"""

import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR_2 = os.path.dirname(os.path.realpath(__name__))
# RUN_ENV Option: DevelopmentConfig, ProductionConfig; if other RUN_ENV is DefaultConfig
RUN_ENV = 'DevelopmentConfig'
# RUN_ENV = 'ProductionConfig'
# RUN_ENV = 'WorkSpaceConfig'
# RUN_ENV = ''

class DefaultConfig(object):
    __version = '1.0.0_Beta'

    
    
class DevelopmentConfig(DefaultConfig):
    __version = '1.0.0_Dev'
    MYSQL_HOST = '10.0.12.3'
    MYSQL_PORT = 13306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Mysql.pwd_5.8%'
    MYSQL_DATABASE = 'tb_douban_movies'
    MYSQL_CHARSET = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False
    
    
class ProductionConfig(DefaultConfig):
    __version = '1.0.0_Releases'
    MYSQL_HOST = 'connect.sql.alicehome.ltd'
    MYSQL_PORT = 23306
    MYSQL_USER = 'projects'
    MYSQL_PASSWORD = 'Projects@123-'
    MYSQL_DATABASE = 'tb_douban_movies'
    MYSQL_CHARSET = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False


class WorkSpaceConfig(DefaultConfig):
    __version = '1.0.0_WorkSpace'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 61004
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DATABASE = 'tb_douban_movies'
    MYSQL_CHARSET = ''
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        MYSQL_USER,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DATABASE
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JSON_AS_ASCII = False

if RUN_ENV == 'DevelopmentConfig':
    RUN_ENV = DevelopmentConfig()
elif RUN_ENV == 'ProductionConfig':
    RUN_ENV = ProductionConfig()
elif RUN_ENV == 'WorkSpaceConfig':
    RUN_ENV = WorkSpaceConfig()
else:
    RUN_ENV = DefaultConfig()
if RUN_ENV.MYSQL_CHARSET == '':
    RUN_ENV.MYSQL_CHARSET = 'utf8'
