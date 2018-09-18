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

2. 保存用户名到
password.json
```json
{
  "stuid": "",
  "password": ""
}
```

3. windows修改bat文件，设定环境变量, *nix 用户请自行解决

4. 打开终端

登入
```bash
$ scunet 
```

注销
```bash
$ scunet logout
```

# todo
- [x] win10使用toast提醒消息
- [ ] 使用python原生http
- [ ] 使用pypi进行分发