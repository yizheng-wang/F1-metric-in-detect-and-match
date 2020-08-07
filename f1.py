#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 08:01:43 2020

@author: wangyizheng
"""

import json 
import glob
import numpy as np
import _init_paths

from cal_iou import * 
from cal_tpfn import *
from cal_tpfp import *
from cal_match import *
from cal_tp import *

# for detect json
orderjson = 0
inputlist = glob.glob('./val/*.json')
totaljson = []
for i in inputlist: # get the file dir in a list
    totaljson.append(i.split('/')[-1])
# tpfn and tpfp init
tpfn = {}
tpfp = {}
tp = {}
f1 = {}
for i in totaljson:
    with open('./val/'+ i) as flabel:
        labelcontent = flabel.read()
        labeldict = json.loads(labelcontent)
    with open('./result/'+i) as fresult:
        resultcontent = fresult.read()
        resultdict = json.loads(resultcontent)
    tpfn = cal_tpfn(labeldict, tpfn)
    tpfp = cal_tpfp(resultdict, tpfp)
# the above is all data we need in a json file, then we analysis them in each iter for tp
    for i in range(len(labeldict['signs'])) :
        for j in range(len(resultdict['signs'])):
            if labeldict['signs'][i]['type'] == resultdict['signs'][j]['type']:
                labelbox = [labeldict['signs'][i]['w'], labeldict['signs'][i]['h'], labeldict['signs'][i]['x'], labeldict['signs'][i]['y']]
                resultbox = [resultdict['signs'][j]['w'], resultdict['signs'][j]['h'], resultdict['signs'][j]['x'], resultdict['signs'][j]['y']]
                iou = cal_iou(labelbox, resultbox)
                if iou >= 0.5:
                    resultdict['signs'][j]['obtp'] = 'fire' 
                    resultdict['signs'][j]['global'] = labeldict['signs'][i]['sign_id'] # create a mark who activate it   
                    break
    labeldict, resultdict = cal_match(labeldict, resultdict)
    # statistic tp
    
    tp = cal_tp(labeldict, resultdict, tp)
for i in tpfn:
    try:
        f1[i] = 2*(tp[i]/tpfn[i])*(tp[i]/tpfp[i])/((tp[i]/tpfn[i])+(tp[i]/tpfp[i]))
    except:
        f1[i] = 0
    
    
mf1 = np.array( [i for i  in f1.values()]).mean()
for i,j in f1.items():
    print(f'every type {i} is {j}')
print(f'mean f1 value is : {mf1}')
    
    