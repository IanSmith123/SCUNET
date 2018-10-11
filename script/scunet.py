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

config_path = os.path.join(os.path.expanduser('~'), '.scunet.json')


# config_path = "./scunet.json"


def login(stuid, password):
    src = requests.get("http://192.168.2.135", allow_redirects=False)
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
    global toast

    # 根据配置文件确定使用的提醒方式
    if toast:
        if os.path.isfile(config_path) and os.path.getsize(config_path):
            j = json.load(open(config_path))
            toast = False if j['toast'] == 'n' else True

    # 设定提示方式

    if toast:
        toaster.show_toast("SCUNET", message, duration=3)
    else:
        print(message)


def get_user_info():
    if not os.path.isfile(config_path):
        print("未检测到账户信息，请输入账户信息")
        with open(config_path, 'w', encoding='utf8') as f:
            _toast = input("是否需要使用弹出式提示框提示信息(仅win10有效) y/n?")
            _stuid = input("请输入用户名: ")
            _password = getpass.getpass("输入密码，输入时密码不可见: ")
            dic = {
                "stuid": _stuid,
                "password": _password,
                "toast": _toast
            }
            f.write(json.dumps(dic, indent=2))
        print("已经保存账户信息，路径为{}".format(config_path))

    if os.path.getsize(config_path):
        j = json.load(open(config_path))
    else:
        prompt("请重置登录信息再继续操作")
        exit(1)
    _stuid = j['stuid']
    _password = j['password']

    _toast = True if j['toast'] == 'y' else False

    global toast
    if toast:
        toast = _toast

    return _stuid, _password


def detectportal():
    url = "http://detectportal.firefox.com/success.txt"
    try:
        if requests.get(url, timeout=2).text.strip() == 'success':
            return True
        else:
            return False
    except:
        return True


def main():
    """
    判断将要执行的操作
    :return:
    """
    if len(sys.argv) == 1:
        stuid, password = get_user_info()
        # 检测联网状况，判定是否需要登录
        if detectportal():
            prompt("正常联网，无需登录")
            exit(0)

        # 避免检测超时导致的误判
        logout()
        login(stuid, password)

    else:
        args = sys.argv[1]
        if args == "logout":
            logout()
            prompt("已注销")

        elif args == 'reset':
            # config_path = os.path.join(os.path.expanduser('~'), '.scunet.json')
            if os.path.isfile(config_path):
                os.remove(config_path)
                prompt("账户信息已清除")
            else:
                prompt("未检测到账户信息")

        elif args == 'help':
            output = """
            {}
            
            scunet          : login
            scunet logout   : log out
            scunet reset    : clear user info
            scunet help     : print this message
            
            
            Bug report URL: https://github.com/iansmith123/scunet
            
            powered by Les1ie.
            
            {}
            """.format('*' * 52, '*' * 52)
            print(output)
        else:
            prompt("无法识别的指令 {}, 请运行 scunet help 查看帮助".format(args))


if __name__ == '__main__':
    main()
