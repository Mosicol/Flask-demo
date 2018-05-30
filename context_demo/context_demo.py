from flask import Flask,current_app,url_for,render_template

app = Flask(__name__)

#应用上下文
#如果在视图函数外部访问，则必须手动推入一个app上下文到app上下文栈中
with app.app_context():
    print(current_app.name)     #context_demo

@app.route('/')
def index():
    # 在视图函数内部可以直接访问current_app.name
    print(current_app.name)    #context_demo
    return 'Hello World!'

@app.route('/list/')
def my_list():
    return 'my_list'

# 请求上下文
with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for('my_list'))


# ===================钩子函数=============================================

@app.before_first_request
def first_request():
    print('只有在处理第一次请求之前执行')

@app.before_request
def before_request():
    print('在视图函数执行之前执行')

@app.context_processor
def context_rocessor():
    return {{'current_user':'xxx'}}

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'),500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run(debug=True)
