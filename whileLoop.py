#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 16:03:06 2022

@author: lijiaheng
"""

# while迴圈設計計算班級成績
# 請使用者輸入名字與成績，如果輸入「-1」則表示成績輸入結束，並顯示平均成績

List = {}
def scoreList():
    totalScore = score = 0
    name = ''
    while (name != 'no'):
        print('\n(要結束請輸入 0 )')
        name = input('學生名字：')
        if (name == '0'):
            break
        score = int(input('成績是：'))
        totalScore += score
        List[name] = score
        print(name, '的成績是', score )
    average = totalScore / len(List)
    print('平均分數為',average)

def findStuScore():
    print('\n(若要離開請輸入0)')
    stuName = input('查詢誰的成績:')
    if (stuName != '0'):
        stuScore = List.get(stuName)
        if stuScore == None:
            print('!!找不到', stuName, '的成績!!')
            findStuScore()
        else:
            print(stuName, '的成績為：', stuScore)
            check = input('繼續請輸入1, 離開請輸入0:')
            if check == '1':
                findStuScore()
    else:
        return

scoreList()
findStuScore()


    