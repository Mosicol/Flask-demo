from flask import Flask,request,Response
from datetime import datetime,timedelta
app = Flask(__name__)

@app.route('/')
def hello_world():
    resp = Response("设置cookie")
    # 1.使用expires参数，就必须使用格林尼治时间
    # 通过expires参数设置有效期的时候，就要相对北京时间少8个小时，所有这里hours是16，
    # 如果直接days=31，就不准确了
    expires = datetime.now() + timedelta(days=30,hours=16)
    resp.set_cookie('username','derek',expires=expires)

    # 2.使用max_age参数设置过期时间（1分钟后后期）
    # resp.set_cookie('username','derek',max_age=60)
    return resp

@app.route('/del/')
def delete_cookie():
    resp = Response("删除cookie")
    #设删除cookie，
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
