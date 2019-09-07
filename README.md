# SCUNET
命令行登录SCUNET

[![PyPI version](https://img.shields.io/pypi/v/scunet.svg)](https://github.com/IanSmith123/SCUNET) [![GitHub stars](https://img.shields.io/github/stars/IanSmith123/SCUNET.svg)](https://github.com/IanSmith123/SCUNET/stargazers) [![GitHub license](https://img.shields.io/github/license/IanSmith123/SCUNET.svg)](https://github.com/IanSmith123/SCUNET/blob/master/License)




# How to use

## 安装
本程序依赖于python，且只在python3 on win10 测试通过，未测试其他环境。
```bash
$ pip3 install scunet
```


## 使用前提
已经正常连接SCUNET并且获取到了正确的IP，比如地址范围为`10.0.0.0/8`的IP。

## 打开终端

- 登入

```bash
$ scunet 
```

- 注销

```bash
$ scunet logout
```
- 重置账户密码

```bash
$ scunet reset
```

- 查看帮助信息

```bash
$ scunet help
```

- 升级本脚本
```
$ pip3 install -U scunet -i https://pypi.org/simple
```

# Hint
- 账户信息保存在`~/.scunet.json`
- win10将会使用toast提示命令执行情况，如果不需要该提示框, 重设用户信息的时候选择`n`即可

# Todo
- [x] win10使用toast提醒消息
- [x] 使用pypi进行分发
- [ ] 使用python原生http


# Changelog
- 2018-10-12 02:07:57 1.0.0 正式版释出, 只在win10下完整测试兼容性，mac和linux未完整测试
- 2018-12-3 12:42:10 1.1.0 Captive Portal 修改了登录网址的url跳转规则,目前的已知的两个登陆注销接口均可用, 程序只适配了新的跳转规则，未修改验证接口

# Bug
- 如果获取的IP是`169.254.0.0/16`时无法使用本程序，此时通过WEB也无法正常登陆
- 未能正常连接wifi时，本程序也会报告连接正常，目前暂不打算修复。此问题请参考前文的`使用前提`。欢迎PR。

# More

不接受任何形式的提需求，只接受PR :)


Les1ie

2018-9-19 20:50:22
