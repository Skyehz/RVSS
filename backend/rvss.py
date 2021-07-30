import base64
from locale import atoi

import cv2
import numpy as np
from flask import Response, send_from_directory
from flask import redirect
from flask import url_for
from flask_cors import CORS

from login.cam import VideoCamera, gen, add_face, generate_random
from login.playback import playbackCamera, gen_playback
from register.email_demo import *
from sqltest import *

# 登录功能
# create Flask instance

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
"""
导入配置文件
DEBUG=True
JSON_AS_ASCII=False
"""
video_file = " "
video_url = " "
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


def reg(type, username, password, email, imgcode):
    flag = True
    if len(imgcode) == 0:
        tag = ''
    else:
        tag = add_face(imgcode)
    if type == "user":
        flag = add_user(username, password, email, tag)
    else:
        flag = add_admin(username, password, email, tag)

    return flag


# 注册页面 注册按钮 json接口，接收用户名、密码、邮件、类型，返回“注册成功”
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        my_json = request.get_json()
        username = my_json.get("username")
        password = my_json.get("password")
        email = my_json.get("email")
        type = my_json.get("type")
        get_key = my_json.get("key")
        imgcode = my_json.get("imgcode")
        print(imgcode)
        if key == get_key:
            reg(type, username, password, email, imgcode)
        t = {
            "status": 200
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")


@app.route('/change_password_verify', methods=['POST'])
def change_password_verify():
    try:
        my_json = request.get_json()
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


# 注册页面，发送验证码按钮，接收邮件地址，返回验证码
@app.route('/reg_verify', methods=['POST'])
def reg_verify():
    flag = False
    try:
        my_json = request.get_json()
        print(my_json)
        email = my_json.get("email")
        type = my_json.get("type")
        if type == "user":
            if usersfind(email) == None:
                flag = True
        else:
            if adminfind(email) == None:
                flag = True

        global key
        key = ''
        if flag:
            key = send_email(email)
        t = {
            "key": key
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")

@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        my_json = request.get_json()
        username = my_json.get("username")
        password = my_json.get("password")
        email = my_json.get("email")
        status = 400
        if usersfind(email) == None:
            reg("user", username, password, email, '')
            status = 200

        t = {
            "status": status
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


@app.route('/edit_remark', methods=['POST'])
def edit_remark():
    try:
        my_json = request.get_json()
        print(my_json)
        remark = my_json.get("mess")
        time = my_json.get("time")
        update_remark(time, remark)
        t = {
            "status": 200
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("wrong")


@app.route('/edit_user', methods=['POST'])
def edit_user():
    try:
        my_json = request.get_json()
        print(my_json)
        email = my_json.get("email")
        password = my_json.get("password")
        username = my_json.get("username")

        update_name("user", email, username)
        update_password("user", email, password)
        t = {
            "status": 200
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
        # email = my_json.get("email")
        # print("email ", email)
        delete_user_info(my_json[2])
        print(my_json[2])
        t = {
            "status": 200
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("delete wrong")


# 删除入侵记录
@app.route('/delete_message', methods=['POST'])
def delete_message():
    try:
        my_json = request.get_json()
        print(my_json)
        delete_invade_message(my_json[0])
        print(my_json[2])
        t = {
            "status": 200
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("delete wrong")


# 查找信息
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


@app.route('/users_info', methods=['GET', 'POST'])
def users_info():
    try:
        my_json = request.get_json()
        print(my_json)

        pagenum = my_json.get("pagenum")
        pagesize = my_json.get("pagesize")

        result = get_users_info()
        matrix = [' ' for i in range(pagesize)]

        nn = 0
        n = (pagenum - 1) * pagesize

        while pagesize != nn:
            matrix[nn] = result[n]
            n += 1
            nn += 1
            if n >= len(result):
                break

        t = {
            "length": len(result),
            "information": matrix
        }
        return jsonify(t)

    except Exception as e:
        print(e)
        return jsonify("info_wrong")


@app.route('/invade_info', methods=['GET', 'POST'])
def invade_info():
    try:
        my_json = request.get_json()
        pagenum = my_json.get("pagenum")
        pagesize = my_json.get("pagesize")

        result = get_invade_info()
        matrix = [' ' for i in range(pagesize)]

        nn = 0
        n = (pagenum-1)*pagesize

        while pagesize != nn:
            matrix[nn] = result[n]
            n += 1
            nn += 1
            if n >= len(result):
                break
        t = {
            "length": len(result),
            "information": matrix
        }
        return jsonify(t)

    except Exception as e:
        return jsonify("info wrong")


@app.route('/video_feed', methods=['POST', 'GET'])
def video_feed():
    return Response(gen(VideoCamera()), content_type="multipart/x-mixed-replace; boundary=frame")


@app.route('/play_back', methods=['POST', 'GET'])
def play_back():
    global video_file
    print("playback start-------------", video_file)
    return Response(gen_playback(playbackCamera(video_file)), content_type="multipart/x-mixed-replace; boundary=frame")


@app.route('/get_invade_time', methods=['POST', 'GET'])
def get_invade_time():

    my_json = request.get_json()
    print(my_json)
    invade_time = my_json[0]
    print(invade_time)

    global video_file
    video_file = filename_find(invade_time)[3]
    print(video_file)

    global video_url
    video_url = generate_random()+"video_playback"

    return video_file
    # return jsonify(video_file)


@app.route('/draw', methods=['POST', 'GET'])
def draw():
    my_json = request.get_json()
    print(my_json)

    x = my_json.get("x")
    y = my_json.get("y")
    index = my_json.get("index")

    update_invade_area(x, y, index)
    t = {
        "status": 200
    }
    return jsonify(t)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
