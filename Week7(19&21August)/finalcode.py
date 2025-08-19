# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 07:21:13 2018

@author: sougs002
"""


def avg_value(sqft,bath,year,num):
    import numpy as np      
        
    ts= np.sum(sqft)   
    tb=np.sum(bath)
    ty = 2000*num - np.sum(year)
    av = (ts*100+tb*15000 -ty*1000)/num
    
    
    return av



    