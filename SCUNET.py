import re
import json
from urllib.parse import urlparse, parse_qs, quote, unquote
import requests


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
        print(res['message'])
    elif res['result'] == 'success':
        print("login success")

    else:
        print("error")


def logout():
    url = "http://192.168.2.135/eportal/InterFace.do?method=logout"
    requests.post(url, data='')
    print("logout success")





stuid = ''
password = ''

if __name__ == '__main__':
    logout()
    login(stuid, password)
    # logout()

