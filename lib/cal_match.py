#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:34:23 2020

@author: wangyizheng
"""

def cal_match(labeldict, resultdict):
    num_match = {}
    for i in range(len(labeldict['match'])): # for A  series in labeldict
        if [s for s in labeldict['match'][i].values()][-1].strip() is not '':
            try:
                num_match[[s for s in labeldict['match'][i].values()][0]] += 1

            except:
                num_match[[s for s in labeldict['match'][i].values()][0]] = 1

            try:
                
                num_match[[s for s in labeldict['match'][i].values()][-1]] += 1
            except:
                
                num_match[[s for s in labeldict['match'][i].values()][-1]] = 1            
    for i,m  in  num_match.items():
        for k in range(len(labeldict['signs'])):
            if i == labeldict['signs'][k]['sign_id']:
                labeldict['signs'][k]['matchnum'] = m
 
    num_match = {}
    for i in range(len(resultdict['match'])): # for A  series
        flag = False
        for m in range(len(resultdict['signs'])):
            try:
                if resultdict['signs'][m]['sign_id'] == [s for s in resultdict['match'][i].values()][0] and resultdict['signs'][m]['obtp'] == 'fire':
                    flag = True
                    break
            except:
                hhh=1
        if flag != True:
            continue            
        if [s for s in resultdict['match'][i].values()][-1].strip() is not '':
            for m in range(len(resultdict['signs'])):
                try:
                    if resultdict['signs'][m]['sign_id'] == [s for s in resultdict['match'][i].values()][-1] and resultdict['signs'][m]['obtp']== 'fire':                    
                        try:
                            num_match[[s for s in resultdict['match'][i].values()][0]] += 1
                        
                        except:
                            num_match[[s for s in resultdict['match'][i].values()][0]] = 1
                except:
                    hhh =1
    for i in range(len(resultdict['match'])): # for A  series
        if [s for s in resultdict['match'][i].values()][-1].strip() is not '':
            flag = False
            for m in range(len(resultdict['signs'])):
                try:
                    if resultdict['signs'][m]['sign_id'] == [s for s in resultdict['match'][i].values()][-1] and resultdict['signs'][m]['obtp'] == 'fire':
                        flag = True
                        break
                except:
                    hhh =1
            if flag != True:
                continue             
            for m in range(len(resultdict['signs'])):
                try:
                    if resultdict['signs'][m]['sign_id'] == [s for s in resultdict['match'][i].values()][0] and resultdict['signs'][m]['obtp']== 'fire':                    
                        try:
                            num_match[[s for s in resultdict['match'][i].values()][-1]] += 1
                        
                        except:
                            num_match[[s for s in resultdict['match'][i].values()][-1]] = 1
                except:
                    hhh = 1
    for i,m  in  num_match.items():
        for k in range(len(resultdict['signs'])):
            if i == resultdict['signs'][k]['sign_id']:
                resultdict['signs'][k]['matchnum'] = m   
                
   
    for i in range(len(labeldict['signs'])):
        try:
            if labeldict['signs'][i]['matchnum'] != 0 :
                hhh = 1 
        except:
            labeldict['signs'][i]['matchnum'] = 0
    
    for i in range(len(resultdict['signs'])):
        try:
            if resultdict['signs'][i]['matchnum'] != 0 :
                hhh = 1 
        except:
            resultdict['signs'][i]['matchnum'] = 0    
            
    for i in range(len(labeldict['signs'])):
        try:
            if labeldict['signs'][i]['global'] != 0 :
                hhh = 1 
        except:
            labeldict['signs'][i]['global'] = 0
    
    for i in range(len(resultdict['signs'])):
        try:
            if resultdict['signs'][i]['global'] != 0 :
                hhh = 1 
        except:
            resultdict['signs'][i]['global'] = 0    
    return labeldict, resultdict
        