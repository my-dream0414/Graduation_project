# -*- codeing = utf-8 -*-
# @Time : 2024/4/16 9:14
# @Author : Luo_CW
# @File : titledata.py
# @Software : PyCharm


import json
def titleData():
    with open('./dataset/alltangs3.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data