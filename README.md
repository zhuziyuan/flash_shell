# flash_shell
用 Flask 实现的在 Web 页面执行 shell 命令的小 Demo

**使用方法如下**

运行在 Python 2.7.x 环境下，依赖 ansible，flask
```
# python -V
Python 2.7.5

```
```
# git clone https://github.com/ackfin/flash_shell.git

# cd flash_shell

# pip install -r requirements.txt

```

下面的IP根据你的情况配置，但要配置好ssh免密认证
```
# cat host.cfg 
192.168.1.254
192.168.1.125
```

测试 ansible 是否能使用 host.cfg 的 ip 正常运行
```
# ansible -i host.cfg all -m ping
192.168.1.254 | success >> {
    "changed": false, 
    "ping": "pong"
}

192.168.1.125 | success >> {
    "changed": false, 
    "ping": "pong"
}
```
启动项目
```
# python main.py 
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
```
比如运行在 192.168.1.254 这台机器上，
就用浏览器打开 http://192.168.1.254:8888
![flask_shell_result.png](https://upload-images.jianshu.io/upload_images/12475671-1da15f8097b8c98b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





