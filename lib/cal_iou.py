#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:03:00 2020
box is (w h x y)
@author: wangyizheng"""
def cal_iou(labelbox, resultbox):
    A = [0]*4
    B = [0]*4
    A[0] = labelbox[2]
    A[1] = labelbox[3] - labelbox[1]
    A[2] = labelbox[2] + labelbox[0]
    A[3] = labelbox[3]
    B[0] = resultbox[2]
    B[1] = resultbox[3] - resultbox[1]
    B[2] = resultbox[2] + resultbox[0]
    B[3] = resultbox[3]    
    left_max = max(A[0], B[0])
    top_max = max(A[1], B[1])
    right_min = min(A[2], B[2])
    bottom_min = min(A[3], B[3])
    
    # calculate inter area
    inter = max(0, (right_min-left_max))*max(0, (bottom_min-top_max))
    sa = (A[2] - A[0]) * (A[3] - A[1]) 
    sb = (B[2] - B[0]) * (B[3] - B[1]) 
    union = sa + sb - inter
    iou = inter / union
    return iou