#!/usr/bin/env python3
import re
import os
import sys
import json
import getpass
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
        prompt(res['message'])
    elif res['result'] == 'success':
        prompt("登录成功")

    else:
        prompt(res['message'])


def logout():
    url = "http://192.168.2.135/eportal/InterFace.do?method=logout"
    requests.post(url, data='')


def prompt(message):
    if toast:
        toaster.show_toast("pyscunet", message, duration=3)
    else:
        print(message)


def get_user_info():
    home = os.path.expanduser('~')
    filepath = os.path.join(home, '.scunet.json')

    if not os.path.isfile(filepath):
        print("未检测到账户信息，请输入账户信息")
        with open(filepath, 'w', encoding='utf8') as f:
            _stuid = input("请输入用户名: ")
            _password = getpass.getpass("输入密码，输入时密码不可见: ")
            dic = {
                "stuid": _stuid,
                "password": _password
            }
            f.write(json.dumps(dic, indent=2))
        print("已经保存账户信息，路径为{}".format(filepath))

    j = json.load(open(filepath))
    _stuid = j['stuid']
    _password = j['password']
    return _stuid, _password


def detectportal():
    url = "http://detectportal.firefox.com/success.txt"
    if requests.get(url, timeout=5).text.strip() == 'success':
        return True
    else:
        return False


def main():
    """
    判断将要执行的操作
    :return:
    """
    if len(sys.argv) == 1:
        # 检测联网状况，判定是否需要登录
        if detectportal():
            prompt("正常联网，无需登录")
            exit(0)

        stuid, password = get_user_info()
        # 避免检测超时导致的误判
        logout()
        login(stuid, password)

    else:
        args = sys.argv[1]
        if args == "logout":
            logout()
            prompt("已注销")

        elif args == 'reset':
            filepath = os.path.join(os.path.expanduser('~'), '.scunet.json')
            if os.path.isfile(filepath):
                os.remove(filepath)
                prompt("账户信息已清除")
            else:
                prompt("未检测到账户信息")
        else:
            prompt("无法识别的指令 {}".format(args))


if __name__ == '__main__':
    main()
