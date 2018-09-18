import re
from urllib.parse import urlparse, parse_qs, quote, unquote
import requests


def login(stuid, password):
    s = requests.Session()
    # src = s.get("http://1.2.3.1", allow_redirects=False)
    src = requests.get("http://1.2.3.1", allow_redirects=False)
    pattern = r"href=\'(.*?)\'"
    raw_url = re.findall(pattern, src.text)[0]

    # 获取请求的参数
    parse = urlparse(raw_url)
    query = parse.query
    qs = parse_qs(query)

    queryString = query

    payload = {
        "userId": stuid,
        "password": password,
        "service": "internet",
        "queryString": queryString,
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
    requests.get(url)
    print("logout success")

stuid = ''
password = ''

if __name__ == '__main__':
    logout()
    login(stuid, password)
    # logout()

