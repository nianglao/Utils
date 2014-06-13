#!/usr/bin/python
# -*- coding: utf-8 -*- 
#coding=utf-8

'''
To my beloved girl friend TongXin.
'''

import  random
menu=['手抓饼', '煎饼', '教工米线', '土豆粉', '清真食堂', '烤肉饭', '教工凉皮', '南门米线', '教工点菜',
      '桂林米粉', '南门抄手', '南门成都美食', '北门砂锅', '新食堂二层', '鸭腿饭']
N = len(menu)
choice = random.randint(0,N-1)
print "今天吃%s, 好开心^_^~~"%(menu[choice])
