# -*- coding: utf-8 -*-
# @Time : 2022/7/6 22:35
# @Author : 野比向日葵
# @File : yacc.py

from lex import *
from ply import yacc


def p_count(p):
	r"""count : NUMBER PLUS NUMBER"""
	p[0] = p[1] + p[3]


file = "1+1"
parser = yacc.yacc(debug=True)
res = parser.parse(file, MyLex)
print(res)
