#!/usr/bin/env python3
import re
import sys
import json
from urllib.parse import urlparse

import requests

try:
    from win10toast import ToastNotifier

    toaster = ToastNotifier()
    toast = True

except ImportError:
    toast = False


def login(stuid, password):
    src = requests.get("http://1.2.3.1", allow_redirects=False)
    pattern = r"href=\'(.*?)\'"
    raw_url = re.findall(pattern, src.text)[0]

    payload = {
        "userId": stuid,
        "password": password,
        "service": "internet",
        "queryString": urlparse(raw_url).query,
        "operatorPwd": '',
        "operatorUserId": '',
        "validcode": '',
        "passwordEncrypt": False,
    }

    # 登录url
    login_url = "http://192.168.2.135/eportal/InterFace.do?method=login"
    r = requests.post(login_url, data=payload)
    r.encoding = 'utf8'
    res = r.json()

    # 判断登录状态
    if res['result'] == 'fail':
        # print(res['message'])
        prompt(res['message'])
    elif res['result'] == 'success':
        # print("login success")
        prompt(res['message'])

    else:
        # print("error")
        prompt(res['message'])


def logout():
    url = "http://192.168.2.135/eportal/InterFace.do?method=logout"
    requests.post(url, data='')
    print("logout success")


def prompt(message):
    if toast:
        toaster.show_toast("pyscunet", message, duration=3)
    else:
        print(message)


def get_user_info():
    j = json.load(open('password.json'))
    _stuid = j['stuid']
    _password = j['password']

    return _stuid, _password


def action(stuid, password):
    """
    判断将要执行的操作
    :return:
    """
    if len(sys.argv) == 1:
        prompt("login")
        exit(1)
        logout()
        login(stuid, password)

    else:
        args = sys.argv[1]
        if args == "logout":
            prompt("logout")
            exit(1)
            logout()
        else:
            prompt("无法识别的指令 {}".format(args))


stuid, password = get_user_info()

if __name__ == '__main__':
    action(stuid, password)
