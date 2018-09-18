# pyscunet
命令行登录SCUNET

# How to use

## 环境配置

本程序请使用python3 :)

```bash
pip3 install requests
```

- windows

将`scunet.bat`所在目录放入环境变量，bat脚本内需要写绝对路径

可选： 

win10用户 可使用toaster发送通知消息,可以额外安装
```
$ pip3 install win10toast
```
- *nix
移动本文件到`/usr/local/bin`
(未测试)

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
- 账户信息保存在`~/.pyscunet.json`

# Todo
- [x] win10使用toast提醒消息
- [ ] 使用python原生http
- [ ] 使用pypi进行分发