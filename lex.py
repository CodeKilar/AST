# -*- coding: utf-8 -*-
# @Time : 2022/7/3 16:52
# @Author : 野比向日葵
# @File : lex.py

from ply import lex

tokens = (
	'NUMBER', 'PLUS'
)

t_PLUS = r'\+'


def t_NUMBER(t):
	r"""[0-9]+"""
	t.value = int(t.value)
	return t


def t_error(t):
	raise Exception('Lex error')


MyLex = lex.lex()

