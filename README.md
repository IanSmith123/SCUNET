# SCUNET
命令行登录SCUNET

# How to use

## 安装
本程序依赖于python，且只在python3 on win10 测试通过，未测试其他环境。
```bash
$ pip3 install scunet
```

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
# Hint
- 账户信息保存在`~/.scunet.json`
- win10将会使用toast提示命令执行情况，如果不需要该提示框，执行 `pip3 uninstall win10toast` 即可 

# Todo
- [x] win10使用toast提醒消息
- [ ] 使用python原生http
- [ ] 使用pypi进行分发



# More

不接受任何形式的提需求，只接受PR :)





Les1ie

2018-9-19 20:50:22