# pyscunet
命令行登录SCUNET

# How to use
1. 环境配置

请使用python3 :)
```bash
pip3 install requests
```

win10可使用toaster发送通知消息,可以额外安装
```
$ pip3 install win10toast
```


2. 打开终端

- 登入

```bash
$ scunet 
```

- 注销

```bash
$ scunet logout
```
- 重置账户密码

```
$ scunet reset
```

3. 首次使用会提示修改输入学号和账号密码, 按要求输入即可，账户信息保存在`~/.pyscunet.json`

# todo
- [x] win10使用toast提醒消息
- [ ] 使用python原生http
- [ ] 使用pypi进行分发