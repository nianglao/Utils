#!/usr/bin/python
# -*- coding: utf-8 -*- 
#coding=utf-8

'''
To my beloved girl friend TongXin.
'''

import  random
import sys

menu_all = ['手抓饼', '煎饼', '教工米线', '土豆粉', '清真食堂', '烤肉饭', '教工凉皮', '南门米线', '教工点菜',
      '桂林米粉', '南门抄手', '南门成都美食', '北门砂锅', '新食堂二层', '鸭腿饭']

menu_big = ['教工米线', '土豆粉', '清真食堂', '烤肉饭', '南门米线', '教工点菜', '桂林米粉',  '北门砂锅', '新食堂二层',
          '鸭腿饭', '南门成都美食']
menu_small = ['手抓饼', '煎饼', '南门抄手', '教工凉皮', '泡面', '零食', '炸鸡腿']


help_info = '''[1] 全部菜单
[2] 量小的菜单
[3] 量大的菜单'''

print help_info
scale = raw_input()

print scale
if scale == '1' :
    menu = menu_all
elif scale == '2' :
    menu = menu_small
elif scale == '3' :
    menu = menu_big
else:
    menu = menu_all
    
N = len(menu)
choice = random.randint(0,N-1)
print "今天吃%s, 好开心^_^~~"%(menu[choice])
