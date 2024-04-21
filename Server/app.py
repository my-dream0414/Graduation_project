# -*- codeing = utf-8 -*-
# @Time : 2023/12/30 11:55
# @Author : Luo_CW
# @File : app.py
# @Software : PyCharm
from flask_cors import *
from flask import Flask, render_template, request
from json_flask import JsonFlask
from json_response import JsonResponse
from poemdata import allPoemdata
from titledata import titleData
from translation import translation


# 创建视图应用
app = JsonFlask(__name__)

# 实现跨域请求
CORS(app, supports_credentials=True)

@app.route("/all", methods=["GET"])  # 查询（全部）
def all():
    result = 1
    print("请求了数据")
    return JsonResponse.success(msg='查询成功', data=result)
# 获取诗词数据
@app.route("/poemdata",methods=['GET'])  # 获取（全部诗词数据）
def poemdata():
    result = allPoemdata()
    return JsonResponse.success(msg='查询成功', data=result)
# 获取诗词标题数据
@app.route("/titledata",methods=['GET'])  # 获取（全部诗词数据）
def titledata():
    result = titleData()
    return JsonResponse.success(msg='查询成功', data=result)
@app.route("/poemtranslation",methods=['POST'])  #获取诗词的翻译数据
def poemtranslation():
    poem = request.data.decode('utf-8')
    result = poemtranslation(poem)
    return JsonResponse.success(msg='查询成功', data=result)
# 运行flask：默认是5000端口，此处设置端口为6055
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=6055,debug=True)