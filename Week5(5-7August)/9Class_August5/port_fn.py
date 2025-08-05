# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 07:21:13 2018

@author: sougs002
"""


def value(DP,DS):
    value=0
    for var in DS:
        value = value + DS[var]*DP[var] 
    return value