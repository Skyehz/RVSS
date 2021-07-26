from flask import Flask, Response, jsonify
from flask import request
from login.sqltest import *

app = Flask(__name__)
 # 跨域支持
def after_request(response):
    # JS前端跨域支持
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app.after_request(after_request)


@app.route("/register",methods=["GET", 'POST'])
def register():
    try:
        my_json = request.get_json()
        print(my_json)
        username = my_json.get("username")
        password = my_json.get("password")
        email = my_json.get("email")
        type = my_json.get("type")

        if type == "user":
            add_user(username, password, email)
        else:
            add_admin(username, password, email)

        login_message = "add over"
        print(login_message)
        return jsonify(login_message)

    except Exception as e:
        print(e)
        return jsonify("register wrong")

if __name__=="__main__":
    app.run(debug=True)
