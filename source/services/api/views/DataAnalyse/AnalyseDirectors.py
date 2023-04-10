# coding: utf8
""" 
@ File: AnalyseDirectors.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-09
"""

import sys

sys.dont_write_bytecode = True

from flask import jsonify
from source.services.api.PublicApi import PublicApi
from source.services.api import Api

public_api = PublicApi()

@Api.route(rule='/directors', methods=['GET'])
def directors():
    pass
