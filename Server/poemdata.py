# -*- codeing = utf-8 -*-
# @Time : 2024/1/18 14:40
# @Author : Luo_CW
# @File : poemdata.py
# @Software : PyCharm


import json
def allPoemdata():
    with open('./dataset/LiBai_2020.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data
