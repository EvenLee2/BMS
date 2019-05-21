from flask import Flask
from flask import request

import sqlite3

def check(username, password):
    conn = sqlite3.connect('D:\\1.db')
    cursor = conn.cursor()
    cursor.execute('select* from student')
    values1 = cursor.fetchall()
    cursor.execute('select* from teacher')
    values2 = cursor.fetchall()
    conn.commit()
    conn.close()
    if(username,password) in values1:
        return 1
    elif(username,password) in values2:
        return 2
    else:
        return -1

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])   
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p>Username:<input name="username"></p>
              <p>Password:<input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容
    if check(request.form['username'], request.form['password']):
        r = request.args.get(request.form['username'], 'admin')
        return 'Hello,'+ r + '!'#输出变量问题未解决
    return '<h3>Bad username or password.</h3>'

@app.route('/login', methods=['GET'])
def login_form():
    return '''<form action="/login" method="post">
              <p>学号:<input name="sno"></p>
              <p>姓名:<input name="sname"></p>
              <p>性别:<input name="ssex"></p>
              <p>年龄:<input name="sage"></p>
              <p>专业:<input name="sdept"></p>
              <p><button type="submit">Log in</button></p>
              </form>'''

@app.route('/login', methods=['POST'])
def login():
    login_ins(request.form['sno'], request.form['sname'], request.form['ssex'], request.form['sage'], request.form['sdept'])
    return '<h3>Log in successfully</h3>'

if __name__ == '__main__':
    app.run()
