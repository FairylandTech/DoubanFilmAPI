# coding: utf8
""" 
@File: test.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 20:32
"""

from source.services.utils.GetIndexData import GetIndexData
from source.services.api.views.DataAnalyse import BaseApi
from settings import Config
import time
from source.services.utils.GetDetailedMsg import GetDetailedMsg
from source.services.utils.GetAnalyseDataTime import GetAnalyseData
import re
from source.services.utils.GetAnalyseDataScore import GetAnalyseDataScore
from source.services.utils.GetAnalyseDataCountry import GetAnalyseDataCountry

import warnings

# warnings.filterwarnings('ignore')


def get_analyse_directors():
    from source.services.utils.GetAnalyseDirectors import GetAnalyseDirectors
    from collections import Counter

    get_analyse_directors = GetAnalyseDirectors()
    result = get_analyse_directors.get_analyse_directors_movies(director_name='王晶', amount_num=14)
    return result


if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    s = time.time()
    limit = 400

    print(get_analyse_directors())

    print(time.time() - s)
