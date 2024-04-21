# -*- codeing = utf-8 -*-
# @Time : 2024/1/4 10:53
# @Author : Luo_CW
# @File : translation.py
# @Software : PyCharm
import requests
import json


# 翻译接口
def translation(data):
    # 请求的url
    url = "https://fanyi.baidu.com/v2transapi?from=wyw&to=zh"

    # 请求表头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    # 请求cookies
    cookies = "BIDUPSID=90C818E2B49CF49271E4C317158101CA; PSTM=1598866983; BDUSS_BFESS=VrLW80UlY0V2FUaEZET2dOTXNUOFZKclhyUm1NZjc1S2ZxbFdMYy0zVnREMDFqSUFBQUFBJCQAAAAAAAAAAAEAAADXLk0mwO7I1bDXuOcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG2CJWNtgiVjRT; BAIDUID=F1C9693A9BF2AE7705B08DFC64FFFD40:FG=1; MCITY=-240%3A; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1703914290; H_PS_PSSID=39732_39939_39997_40053; BAIDUID_BFESS=F1C9693A9BF2AE7705B08DFC64FFFD40:FG=1; ZFY=rm6sD3arrefqiWxJSJyR4MBHmFNW7kwcqHMpb3y93M4:C; ab_sr=1.0.1_ZWRiOGY3OWZlM2FhZWFhZjJmM2Y4ZDNjM2YyMzBkNTQ4OGM4MjM5N2JiZWUyZmVkZjI0ZGM0YjFkMmZiMjFjZTQ2NDVlN2U3MjA0MDBiZDY0OWQxOGRjOTY4NGEzMzI3ODJlN2RlMjQxNmE4NWZjN2Q4NWVmZGRkNWE2MTUzY2ZmZTQzZDQ4ODlkYTlmYWM4MTdhZWMyYmUxYTNjZTE4OTllMzQzMjYzNzVmOGQyNmZlZDc4MzlhNDI5ZjhiYThm"
    jar = requests.cookies.RequestsCookieJar()
    for cookie in cookies.split(";"):
        key, value = cookie.split("=", 1)
        jar.set(key, value)

    # 请求的表单数据
    post_data = {
        "from": "wyw",
        "to": "zh",
        "query": data,
        "transtype": "translang",
        "simple_means_flag": 3,
        "sign": 180318.402287,
        "token": "7e634827513f1d876329f73eba51435c",
        "domain": "common",
        "ts": "1704339984900"}


    # 向服务器发起请求
    response = requests.post(url, cookies=jar, data=post_data, headers=headers)

    # 获取请求数据
    response_data = json.loads(response.text)
    print(response_data)
    # 返回请求数据
    # return response_data['trans_result']['data'][0]['dst']
