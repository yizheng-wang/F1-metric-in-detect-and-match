#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 07:46:05 2020

@author: wangyizheng
"""
def cal_tp(labeldict, resultdict, tp):
   
    for i in range(len(labeldict['signs'])):
        for m in range(len(resultdict['signs'])):
            if labeldict['signs'][i]['matchnum'] == resultdict['signs'][m]['matchnum'] and resultdict['signs'][m]['global'] == labeldict['signs'][i]['sign_id']:
                try:
                    tp[labeldict['signs'][i]['type']] += 1
                except:
                    tp[labeldict['signs'][i]['type']] = 1
    return tp