from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/learn_sqlalchemy?charset=utf8"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return "<username:%s>"%self.username

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer,db.ForeignKey("user.id"))
    author = db.relationship("User",backref='article')

# db.drop_all()         #删除表
# db.create_all()       #创建表

# 1.添加数据
# user = User(username='derek')
# article = Article(title='今天5/27号')
# article.author = user
#
# db.session.add(article)
# db.session.commit()

# 2.查询数据
# users=User.query.all()
# print(users)

# 3.修改数据,先查找出来再修改
# user = User.query.filter(User.username=='derek').first()
# user.username = 'jack'
# db.session.commit()

# 4.删除数据
user = User.query.filter(User.username=='jack').first()
db.session.delete(user)
db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
