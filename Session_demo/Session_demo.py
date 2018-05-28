from flask import Flask,session
import os
from datetime import timedelta
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
#自定义设置session的有效期
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
CSRFProtect(app)

@app.route('/')
def index():
    # 设置session
    session['username'] = 'derek'
    # permanent:过期时间，默认为false,如果设置为True,则默认为31天之后过期
    # 可以通过app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)
    # 来自定义过期时间，这样设置后，session.permanent = True的session有效期则为两个小时
    session.permanent = True
    return 'Hello World!'

@app.route('/get_session/')
def get_session():
    #获取session
    username = session.get('username')    # derek
    return username

@app.route('/delete_session/')
def delete_session():
    #删除session
    session.pop('username')    #删除指定的session
    # session.clear()          #删除所有session
    return '删除成功'

if __name__ == '__main__':
    app.run(debug=True)
