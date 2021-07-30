import pymysql

# 连接数据库
config = {"host": "localhost",
          "user": "root",
          "password": "010303",
          "db": "rvss"}

# conn = pymysql.connect(**config)
# cur = conn.cursor()


# 注册新用户
def add_user(username, password, email, tag):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    # sql commands
    sql = "INSERT INTO users(username, password, email, tag)  \
           VALUES ('%s','%s','%s','%s')" % (username, password, email, tag)
    # execute(sql)
    cur.execute(sql)
    login_message = "add user"
    print(login_message)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()


# 注册新管理员
def add_admin(username, password, email, tag):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    # sql commands
    sql = "INSERT INTO admin(username, password, email, tag)  \
           VALUES ('%s','%s','%s','%s')" % (username, password, email, tag)

    # execute(sql)
    cur.execute(sql)
    login_message = "add admin"
    print(login_message)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()


def add_invade_info(time, location, remark, filename):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    # sql commands
    sql = "INSERT INTO invade(time,location,remark, filename)  \
               VALUES ('%s','%s','%s','%s')" % (time, location, remark, filename)

    # execute(sql)
    cur.execute(sql)
    login_message = "add invade"
    print(login_message)
    # commit
    conn.commit()  # 对数据库内容有改变，需要commit()
    conn.close()

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
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE email ='%s'  \
         and password ='%s'" % (email, password)
    cur.execute(sql)
    result = cur.fetchall()
    # print("result_", result)
    # print(len(result))

    conn.close()
    if len(result) == 0:
        return False
    else:
        return True



# 判断管理员是否存在于数据库
def is_existed_admin(email, password):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM admin WHERE email ='%s'  \
           and password ='%s'" % (email, password)
    cur.execute(sql)
    result = cur.fetchall()

    conn.close()
    if len(result) == 0:
        return False
    else:
        return True


# 更改用户名
def update_name(type, email, newname):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    if type == "user":
        sql = "UPDATE users SET username = '%s' WHERE email = '%s'" % (newname, email)
    else:
        sql = "UPDATE admin SET username = '%s' WHERE email = '%s'" % (newname, email)

    cur.execute(sql)
    # 提交sql语句执行操作
    conn.commit()
    conn.close()
    return


# 更改密码
def update_password(type, email, password):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    if type == "user":
        sql = "UPDATE users SET password = '%s' WHERE email = '%s'" % (password, email)
    else:
        sql = "UPDATE admin SET password = '%s' WHERE email = '%s'" % (password, email)

    cur.execute(sql)
    # 提交sql语句执行操作
    conn.commit()
    conn.close()
    return

# 更改入侵区域
def update_invade_area(x, y, tag):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "UPDATE invadeArea SET x = '%d',y = '%d' WHERE tag= '%d'" % (x, y, tag)

    cur.execute(sql)
    # 提交sql语句执行操作
    conn.commit()
    conn.close()
    return


def update_remark(time, remark):

    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "UPDATE invade SET remark='%s' WHERE time='%s'" % (remark,time)

    cur.execute(sql)
    # 提交sql语句执行操作
    conn.commit()
    conn.close()
    return


# 删除用户信息
def delete_user_info(email):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "DELETE FROM users WHERE email = '%s'" % email
    try:
        print('user delete')
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()
    return True
    # if len(usersfind(email)):

    # else:
    #     conn.close()
    #     return False


# 删除入侵记录
def delete_invade_message(time):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "DELETE FROM invade WHERE time = '%s'" % time
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()


    conn.close()
    return True


def usersfind(email):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE email ='%s'" % email
    cur.execute(sql)
    result = cur.fetchone()
    # conn.close()
    # if len(result) == 0:
    #
    #     return False
    # else:
    return result


def adminfind(email):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM admin WHERE email ='%s'" % email
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    # if len(result) == 0:
    #     return False
    # else:
    return result


def admin_find_invade(tag):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM admin WHERE tag ='%s'" % tag
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    if len(result) == 0:
        return False
    else:
        return result


conn = pymysql.connect(**config)
def face_find(tag):
    cur = conn.cursor()
    sql = "SELECT * FROM admin WHERE tag ='%s'" % tag
    # print("MYSQL_", tag)
    cur.execute(sql)
    result = cur.fetchone()
    # print(result)
    if result == None:
        return 'MYSQL unknow'
    else:
        print(result[0])
        return result[0]

# 查找入侵区域
def area_find():
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM invadeArea "
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    if len(result) == 0:
        return False
    else:
        return result

def filename_find(time):
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM invade WHERE time ='%s'" % time
    cur.execute(sql)
    result = cur.fetchone()
    conn.close()
    # if len(result) == 0:
    #     return False
    # else:
    return result

def get_users_info():
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM users"
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    if len(result) == 0:
        return False
    else:
        return result


def get_invade_info():
    conn = pymysql.connect(**config)
    cur = conn.cursor()
    sql = "SELECT * FROM invade"
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    if len(result) == 0:
        return False
    else:
        return result