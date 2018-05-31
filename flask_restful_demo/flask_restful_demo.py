from flask import Flask
from flask_restful import Api,Resource,reqparse,inputs

app = Flask(__name__)
api = Api(app)

class LoginView(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username',type=str,help='用户名验证错误',default='xxx',trim=True)
        parser.add_argument('password',type=str,help='密码验证错误',required=True)
        parser.add_argument('gender',type=str,choices=['male','famale'])
        parser.add_argument('home_page',type=inputs.url,help=('个人中心链接错误'))
        parser.add_argument('birthday',type=inputs.date)
        args = parser.parse_args()
        print(args)
        return {'username':'derek'}

api.add_resource(LoginView,'/login/',endpoint="login")

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
