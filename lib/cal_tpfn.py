#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 18:43:05 2020

@author: wangyizheng
"""

def cal_tpfn(labeldict, tpfn):
    dict_tpfn = {}
    for i in range(len(labeldict['signs'])):
        if labeldict['signs'][i]['type'] not in tpfn:
            tpfn[labeldict['signs'][i]['type']] = 1
        else:
            tpfn[labeldict['signs'][i]['type']] += 1
    return tpfn