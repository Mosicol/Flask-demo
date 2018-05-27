
from flask_script import Manager

from flask_scripts_demo import app
from flask_scripts_demo import BackendUser,db

manager = Manager(app)

# @manager.command      #这个装饰器把函数变成在终端可以运行的命令
# def greet():
#     print('你好')

#如果函数需要传递参数就用option装饰器
# @manager.option("-u","--username",dest="username")    #第一个参数是简称
# @manager.option("-a","--age",dest="age")
# def add_user(username,age):
#     print("添加的用户名是：%s,年龄是：%s"%(username,age))

@manager.option("-u","--username",dest="username")    #第一个参数是简称
@manager.option("-e","--email",dest="email")
def add_user(username,email):
    user = BackendUser(username=username,email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()