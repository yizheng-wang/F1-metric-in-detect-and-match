#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 18:43:05 2020

@author: wangyizheng
"""

def cal_tpfp(resultdict, tpfp):
    dict_tpfn = {}
    for i in range(len(resultdict['signs'])):
        if resultdict['signs'][i]['type'] not in tpfp:
            tpfp[resultdict['signs'][i]['type']] = 1
        else:
            tpfp[resultdict['signs'][i]['type']] += 1
    return tpfp