import pymysql

# 连接数据库
config = {"host": "localhost",
          "user": "root",
          "password": "010303",
          "db": "rvss"}

conn = pymysql.connect(**config)
cur = conn.cursor()


# 注册新用户
def add_user(username, password, email):
    # sql commands
    sql = "INSERT INTO users(username, password, email)  \
           VALUES ('%s','%s','%s')" % (username, password, email)
    # execute(sql)
    cur.execute(sql)
    login_message = "add user"
    print(login_message)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    # conn.close()


# 注册新管理员
def add_admin(username, password, email):
    # sql commands
    sql = "INSERT INTO admin(username, password, email)  \
           VALUES ('%s','%s','%s')" % (username, password, email)

    # execute(sql)
    cur.execute(sql)
    login_message = "add admin"
    print(login_message)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    # conn.close()


# 选择身份
def isusers(type):
    if type == 'user':
        # 选中用户则为true
        return True
    else:
        return False


def isadmin(type):
    if type == 'admin':
        # 选中管理员则为true
        return True
    else:
        return False


# 判断用户是否存在于数据库
def is_existed_users(email, password):
    sql = "SELECT * FROM users WHERE email ='%s'  \
         and password ='%s'" % (email, password)
    cur.execute(sql)
    result = cur.fetchall()
    # print("result_", result)
    # print(len(result))

    if len(result) == 0:
        return False
    else:
        return True


# 判断管理员是否存在于数据库
def is_existed_admin(email, password):
    sql = "SELECT * FROM admin WHERE email ='%s'  \
           and password ='%s'" % (email, password)
    cur.execute(sql)
    result = cur.fetchall()
    if len(result) == 0:
        return False
    else:
        return True


# 更改用户名
def update_name(type, email, newname):
    if type == "user":
        sql = "UPDATE users SET username = '%s' WHERE email = '%s'" % (newname, email)
    else:
        sql = "UPDATE admin SET username = '%s' WHERE email = '%s'" % (newname, email)

    cur.execute(sql)
    # 提交sql语句执行操作
    conn.commit()
    return


# 更改密码
def update_password(type, email, password):
    if type == "user":
        sql = "UPDATE users SET password = '%s' WHERE email = '%s'" % (password, email)
    else:
        sql = "UPDATE admin SET password = '%s' WHERE email = '%s'" % (password, email)

    cur.execute(sql)
    # 提交sql语句执行操作
    conn.commit()
    return


def users(email):
    if usersfind(email):
        return True


def delete_user(email):
    if (users(email)):
        sql = "DELETE FROM users WHERE email = '%s'" % email
        try:
            cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()
        conn.close()
        return True
    else:
        return False


def usersfind(email):
    sql = "SELECT * FROM users WHERE email ='%s'" % email
    cur.execute(sql)
    result = cur.fetchone()
    if len(result) == 0:
        return False
    else:
        return result


def adminfind(email):
    sql = "SELECT * FROM admin WHERE email ='%s'" % email
    cur.execute(sql)
    result = cur.fetchone()
    if len(result) == 0:
        return False
    else:
        return result
