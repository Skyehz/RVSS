from flask import Flask, render_template, Response, jsonify
from flask import redirect
from flask import url_for
from flask_cors import CORS
from register.email_demo import *
from sqltest import *

# 登录功能
# create Flask instance
#
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
"""
导入配置文件
DEBUG=True
JSON_AS_ASCII=False
"""

@app.route('/')
def index():
    return redirect(url_for('user_login'))


# 登录页面 登陆按钮 json接口，接收用户名和密码
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        my_json = request.get_json()
        print(my_json)

        global gl_email
        gl_email = my_json.get("email")
        global gl_password
        gl_password = my_json.get("password")
        global gl_type
        gl_type = my_json.get("type")

        # postman接口测试，返回login_message
        if isusers(gl_type):  # 用户
            if is_existed_users(gl_email, gl_password):
                login_message = "user exist"
                print(login_message)
                t = {
                    "email": gl_email,
                    "token": "wsad",
                    "status": 200
                }

                return jsonify(t)
            else:
                login_message = "user not exist"
                print(login_message)
                t = {
                    "email": gl_email,
                    "token": "wsad",
                    "status": 400
                }
                return jsonify(t)
        elif isadmin(gl_type):  # 管理员
            if is_existed_admin(gl_email, gl_password):
                login_message = "admin exist"
                print(login_message)
                t = {
                    "email": gl_email,
                    "token": "wsad",
                    "status": 200
                }
                return jsonify(t)
            else:
                login_message = "admin not exist"
                print(login_message)
                t = {
                    "email": gl_email,
                    "token": "wsad",
                    "status": 400
                }
                return jsonify(t)
        else:
            login_message = "no member Login Failed"
            print(login_message)
            return jsonify(login_message)

    except Exception as e:
        print(e)
        return jsonify("wrong")


# 注册页面 注册按钮 json接口，接收用户名、密码、邮件、类型，返回“注册成功”
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        my_json = request.get_json()
        print(my_json)
        username = my_json.get("username")
        password = my_json.get("password")
        email = my_json.get("email")
        type = my_json.get("type")
        get_key = my_json.get("key")
        print(key)
        print("get key " + get_key)

        if key == get_key:
            if type == "user":
                add_user(username, password, email)
                print("add user successfully")
                t = {
                    "status": 200
                }
                return jsonify(t)
            else:
                add_admin(username, password, email)
                t = {
                    "status": 200
                }
                return jsonify(t)
        else:
            t = {
                "status": 400
            }
            return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")


# 注册页面，发送验证码按钮，接收邮件地址，返回验证码
@app.route('/reg_verify', methods=['POST'])
def reg_verify():
    try:
        my_json = request.get_json()
        print(my_json)
        email = my_json.get("email")
        global key
        key = send_email(email)
        t = {
            "key": key
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")


# 修改个人信息，修改用户名，接收邮件地址、类型、新用户名，返回修改成功信息
@app.route('/change_name', methods=['POST'])
def change_name():
    try:
        my_json = request.get_json()
        print(my_json)

        email = my_json.get("email")
        newname = my_json.get("username")
        update_name(gl_type, email, newname)

        t = {
            "status": 200
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")


# 修改个人密码，接收邮件地址、类型、新密码，返回修改成功信息
@app.route('/change_password', methods=['POST'])
def change_password():
    try:
        my_json = request.get_json()
        print(my_json)
        email = my_json.get("email")
        get_key = my_json.get("key")
        password = my_json.get("password")
        if key == get_key:
            update_password(gl_type, email, password)
            t = {
                "status": 200
            }
            return jsonify(t)
        else:
            t = {
                "status": 400
            }
            return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")


# 删除用户
@app.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        my_json = request.get_json()
        print(my_json)
        email = my_json.get("email")
        username = my_json.get("username")
        print("email ", email)
        delete_user(email)
        t = {
            "msg": "success"
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("delete wrong")
'''
{
    "username":"admin",
    "password":"123456",
    "email":"czh15296700133@163.com",
    "type":"admin"
}
'''

@app.route('/message', methods=['POST'])
def message():
    try:
        my_json = request.get_json()
        print(my_json)
        msg = my_json.get("msg")
        print("msg--- ", msg)
        if msg == "get_information":
            if gl_type == "user":
                result = usersfind(gl_email)
            else:
                result = adminfind(gl_email)
            print("find ", result)
            print(result[0])
            t = {
                "username": result[0],
                "password": result[1],
                "email": result[2]
            }
            return jsonify(t)
        else:
            return jsonify("else")

    except Exception as e:
        print(e)
        return jsonify("delete wrong")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
