# -*- coding: utf-8 -*-
import pymysql

db = pymysql.connect('localhost', 'root', '20121513zal', 'esports')
cursor = db.cursor()
#db.set_charset('utf8')

# ------------------------------ Create Tables ----------------------------------
# by MinstrelZal
# 2017-12-22

def init(db, cursor):
    # create esports_info table
    cursor.execute("DROP TABLE IF EXISTS esport_info") # type= 0:MOBA 1:FPS
    sql = """CREATE TABLE `esport_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(20) NOT NULL,
                    `type` INT(11) DEFAULT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)
    
    cursor.execute("DROP TABLE IF EXISTS league_info")
    sql = """CREATE TABLE `league_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    `begin_time` DATE DEFAULT NULL,
                    `end_time` DATE DEFAULT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS game_info")
    sql = """CREATE TABLE `game_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    `time` DATE DEFAULT NULL,
                    `location` VARCHAR(20) DEFAULT NULL,
                    `league_id` INT(11) NOT NULL,
                    `result` VARCHAR(20) NOT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS club_info")
    sql = """CREATE TABLE `club_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    `sponsor` VARCHAR(30) DEFAULT NULL,
                    `achievement` VARCHAR(255) DEFAULT NULL,
                    `setup_time` DATE DEFAULT NULL,
                    `founder` VARCHAR(20) DEFAULT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS team_info")
    sql = """CREATE TABLE `team_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL,
                    `coach` VARCHAR(30) DEFAULT NULL,
                    `achievement` VARCHAR(255) DEFAULT NULL,
                    `club_id` INT(11) NOT NULL,
                    `esport_id` INT(11) NOT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS player_info")
    sql = """CREATE TABLE `player_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `game_id` VARCHAR(30) NOT NULL,
                    `name` VARCHAR(30) NOT NULL,
                    `gender` TINYINT NOT NULL,
                    `achievement` VARCHAR(255) DEFAULT NULL,
                    `team_id` INT(11) NOT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)
   
    cursor.execute("DROP TABLE IF EXISTS user_info")
    sql = """CREATE TABLE `user_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `username` VARCHAR(30) NOT NULL,
                    `password` VARCHAR(30) NOT NULL,
                    `is_loggedin` TINYINT DEFAULT 0,
                    `is_staff` TINYINT DEFAULT 0,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS league_result")
    sql = """CREATE TABLE `league_result` (
                    `league_id` INT(11) NOT NULL,
                    `esport_id` INT(11) NOT NULL,
                    `result` VARCHAR(30) NOT NULL,
                    PRIMARY KEY (`league_id`, `esport_id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS game_competitor")
    sql = """CREATE TABLE `game_competitor` (
                    `game_id` INT(11) NOT NULL,
                    `team_id` INT(11) NOT NULL,
                    `player_game_id` INT(11) NOT NULL,
                    `self` TINYINT NOT NULL,
                    PRIMARY KEY (`game_id`, `team_id`, `player_game_id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS club_esport")
    sql = """CREATE TABLE `club_esport` (
                    `club_id` INT(11) NOT NULL,
                    `esport_id` INT(11) NOT NULL,
                    PRIMARY KEY (`club_id`, `esport_id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

# --------------------------------------- user_info ------------------------------------------
# by MinstrelZal
# 2017-12-22

def Register_Login(username, password, is_loggedin=1, is_staff=1):
    if(len(username) < 1 or len(username) > 30):
        print("用户名长度需在0-30位之间")
        return 1
    if(len(password) < 8 or len(password) > 30):
        print("密码长度需在8-30位之间")
        return 1
    sql = 'SELECT password FROM user_info WHERE username="%s";' % username
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            result = cursor.fetchone()
            print(result)
            if(result[0] == password):
                sql = 'UPDATE user_info SET is_loggedin=1 WHERE username="%s";' % username
                try:
                    cursor.execute(sql)
                    db.commit()
                    print("登录成功")
                except:
                    db.rollback()
                    print("Error: Unable to update user_info")
                    return 1
                return 0
            else:
                print("密码错误")
                return 1
    except:
        print("Error: Unable to select from user_info")
        return 1
    sql = 'INSERT INTO user_info (username, password, is_loggedin, is_staff) values ("%s", "%s", %d, %d);' % (username, password, is_loggedin, is_staff)
    try:
        cursor.execute(sql)
        db.commit()
        print("注册成功")
        print("登录成功")
    except:
        db.rollback()
        print("Error: Unable to insert into user_info")
        return 1
    return 0

def Logout(username):
    sql = 'SELECT id FROM user_info WHERE username="%s";' % username
    try:
        cursor.execute(sql)
        if(cursor.rowcount != 1):
            print("用户名错误")
            return 1
    except:
        print("Error: Unable to select from user_info")
        return 1
    sql = 'UPDATE user_info SET is_loggedin=0 WHERE username="%s";' % username
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print("Error: Unable to update user_info")
        return 1
    print("登出成功")
    return 0
        
def Add_User(username, password, is_loggedin=0, is_staff=0):
    if(len(username) < 1 or len(username) > 30):
        print("用户名长度需在0-30位之间")
        return 1
    if(len(password) < 8 or len(password) > 30):
        print("密码长度需在8-30位之间")
        return 1
    sql = 'SELECT password FROM user_info WHERE username="%s";' % username
    try:
        cursor.execute(sql)
        if(cursor.rowcount > 0):
            print("用户已存在")
            return 1
    except:
        print("Error: Unable to select from user_info")
        return 1
    sql = 'INSERT INTO user_info (username, password, is_loggedin, is_staff) values ("%s", "%s", %d, %d);' % (username, password, is_loggedin, is_staff)
    try:
        cursor.execute(sql)
        db.commit()
        print("用户添加成功")
    except:
        db.rollback()
        print("Error: Unable to insert into user_info")
        return 1
    return 0

def Delete_User(user_id):
    sql = 'DELETE FROM user_info WHERE id="%d";' % user_id
    try:
        cursor.execute(sql)
        db.commit()
        print("删除用户成功")
    except:
        db.rollback()
        print("Error: Unable to delete from user_info")
        return 1
    return 0

def Search_User(username):
    sql = 'SELECT id,username,is_staff FROM user_info WHERE username REGEXP "%s";' % username
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 0):
            return []
        result = cursor.fetchall()
        print(result)
    except:
        print("Error: Unable to select from user_info")
        return 1
    print("查询成功")
    fields = ('id', 'username', 'is_staff')
    userlist = []
    for row in result:
        row = dict(zip(fields, row))
        userlist.append(row)
    print(userlist)
    return userlist

def Alter_User(user_id, username, password, is_staff=0):
    if(len(username) < 1 or len(username) > 30):
        print("用户名长度需在0-30位之间")
        return 1
    if(len(password) < 8 or len(password) > 30):
        print("密码长度需在8-30位之间")
        return 1
    sql = 'UPDATE user_info SET username="%s",password="%s",is_staff=%d WHERE id=%d;' % (username, password, is_staff, user_id)
    try:
        cursor.execute(sql)
        db.commit()
        print("编辑用户信息成功")
    except:
        db.rollback()
        print("Error: Unable to update user_info")
        return 1
    return 0

def User_List():
    sql = "SELECT id,username,is_staff FROM user_info;"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except:
        print("Error: Unable to select from user_info")
        return 1
    print("获取用户列表成功")
    fields = ('id', 'username', 'is_staff')
    userlist = []
    for row in result:
        row = dict(zip(fields, row))
        userlist.append(row)
    print(userlist)
    return userlist

# ---------------------------------- esport_info ----------------------------------
# by MinstrelZal
# 2017-12-22

def Add_ESport(name, etype):
    sql = 'SELECT id FROM esport_info WHERE name="%s";' % name
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print("该项目已存在")
            return 1
    except:
        print("Error: Unable to select from esport_info")
        return 1
    sql = 'INSERT INTO esport_info (name, type) VALUES ("%s", %d);' % (name, etype)
    try:
        cursor.execute(sql)
        db.commit()
        print("项目添加成功")
    except:
        db.rollback()
        print("Error: Unable to insert into esport_info")
        return 1
    return 0

def Delete_ESport(esport_id):
    sql = 'DELETE FROM esport_info WHERE id=%d;' % esport_id
    try:
        cursor.execute(sql)
        db.commit()
        print("删除项目成功")
    except:
        db.rollback()
        print("Error: Unable to delete from esport_info")
        return 1
    return 0

def Search_ESport(name):
    sql = 'SELECT * FROM esport_info WHERE name REGEXP "%s";' % name
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except:
        print('Error: Unable to select from esport_info')
        return 1
    print("查询成功")
    fields = ('id', 'name', 'type')
    esportlist = []
    for row in result:
        row = dict(zip(fields, row))
        esportlist.append(row)
    print(esportlist)
    return esportlist

def Alter_Esport(esport_id, name, etype):
    sql = 'UPDATE esport_info SET name="%s",type=%d WHERE id=%d;' % (name, etype, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print("编辑竞技项目信息成功")
    except:
        db.rollback()
        print('Error: Unable to update esport_info')
        return 1
    return 0

def ESport_List():
    sql = 'SELECT * FROM esport_info;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from esport_info')
        return 1
    print("获取竞技项目列表成功")
    fields = ('id', 'name', 'type')
    esportlist = []
    for row in result:
        row = dict(zip(fields, row))
        esportlist.append(row)
    print(esportlist)
    return esportlist


# --------------------------- league_info & league_result ------------------------------
# by MinstrelZal
# 2017-12-22

def Add_League(name, begin_time, end_time):
    sql = 'SELECT id FROM league_info WHERE name="%s";' % name
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该联赛记录已存在')
            return 1
    except:
        print('Error: Unable to select from league_info;')
        return 1
    sql = 'INSERT INTO league_info (name, begin_time, end_time) VALUES ("%s", "%s", "%s");' % (name, begin_time, end_time)
    try:
        cursor.execute(sql)
        db.commit()
        print('联赛记录添加成功')
    except:
        db.rollback()
        print('Error: Unable to insert into league_info')
        return 1
    return 0

def Delete_League(league_id):
    sql = 'DELETE FROM league_info WHERE id=%d;' % league_id
    try:
        cursor.execute(sql)
        db.commit()
        print("删除联赛记录成功")
    except:
        db.rollback()
        print('Error: Unable to delete from league_info')
        return 1
    return 0

def Search_League(name):
    sql = 'SELECT * FROM league_info WHERE name REGEXP "%s";' % name
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from league_info')
        return 1
    fields = ('id', 'name', 'begin_time', 'end_time')
    leaguelist = []
    for row in result:
        row = dict(zip(fields, row))
        leaguelist.append(row)
    print(leaguelist)
    return leaguelist

def Alter_League(league_id, name, begin_time, end_time):
    sql = 'UPDATE league_info SET name="%s",begin_time="%s",end_time="%s" WHERE id=%d;' % league_id
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑联赛记录信息成功')
    except:
        db.rollback()
        print('Error: Unable to update league_info')
        return 1
    return 0

def League_List():
    sql = 'SELECT * FROM league_info;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from league_info')
        return 1
    print('获取联赛记录列表成功')
    fields = ('id', 'name', 'begin_time', 'end_time')
    leaguelist = []
    for row in result:
        row = dict(zip(fields, row))
        leaguelist.append(row)
    print(leaguelist)
    return leaguelist

def Add_League_Result(league_id, esport_id, result):
    sql = 'SELECT result FROM league_result WHERE league_id=%d AND esport_id=%d;' % (league_id, esport_id)
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print("该联赛结果记录已登记")
            return 1
    except:
        print('Error: Unable to select from league_result')
        return 1
    sql = 'INSERT INTO league_result (league_id, esport_id, result) VALUES (%d, %d, "%s");' % (league_id, esport_id, result)
    try:
        cursor.execute(sql)
        db.commit()
        print('联赛结果记录添加成功')
    except:
        db.rollback()
        print('Error: Unable to insert into league_result')
        return 1
    return 0

def Delete_League_Result(league_id, esport_id):
    sql = 'DELETE FROM league_result WHERE league_id=%d AND esport_id=%d;' % (league_id, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('删除联赛结果记录成功')
    except:
        db.rollback()
        print('Error: Unable to delete from league_result')
        return 1
    return 0

def Search_League_Result(league_id, esport_id):
    sql = 'SELECT result FROM league_result WHERE league_id=%d AND esport_id=%d;' % (league_id, esport_id)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except:
        print('查询联赛记录结果失败')
        return 1
    return result[0]

def Alter_League_Result(league_id, esport_id):
    sql = 'UPDATE league_result SET result="%s" WHERE league_id=%d AND esport_id=%d;' % (result, league_id, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('联赛结果记录修改成功')
    except:
        db.rollback()
        print('Error: Unable to update league_result')
        return 1
    return 0

# ---------------------------- game_info ---------------------------------
# by MinstrelZal
# 2017-12-22

def Add_Game(name, time, location, league_id, result):
    sql = 'SELECT time FROM game_info WHERE name="%s";' % name
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该比赛记录已登记')
            return 1
    except:
        print('Error: Unable to select from game_info')
        return 1
    sql = 'INSERT INTO game_info (name, time, location, league_id, result) VALUES ("%s", "%s", "%s", %d, "%s");' % (name, time, location, league_id, result)
    try:
        cursor.execute(sql)
        db.commit()
        print("添加比赛记录成功")
    except:
        db.rollback()
        print('Error: Unable to insert into game_info')
        return 1
    return 0

def Delete_Game(game_id):
    sql = 'DELETE FROM game_info WHERE id=%d;' % game_id
    try:
        cursor.execute(sql)
        db.commit()
        print('删除比赛记录成功')
    except:
        db.rollback()
        print('Error: Unable to delete from game_info')
        return 1
    return 0

def Search_Game(name):
    sql = 'SELECT * FROM game_info WHERE name REGEXP "%s";' % name
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from game_info')
        return 1
    print('查询比赛记录成功')
    gamelist = []
    fields = ('id', 'name', 'location', 'league_id', 'result')
    for row in result:
        row = dict(zip(fields, row))
        gamelist.append(row)
    print(gamelist)
    return gamelist

def Alter_Game(game_id, name, location, league_id, result):
    sql = 'UPDATE game_info SET name="%s",location="%s",league_id=%d,result="%s" WHERE id=%d;' % game_id
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑比赛记录成功')
    except:
        db.rollback()
        print('Error: Unable to update game_info')
        return 1
    return 0

def Game_List():
    sql = 'SELECT * FROM game_info;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from game_info')
        return 1
    print('获取比赛记录列表成功')
    gamelist = []
    fields = ('id', 'name', 'location', 'league_id', 'result')
    for row in result:
        row = dict(zip(fields, row))
        gamelist.append(row)
    print(gamelist)
    return gamelist


#init(db, cursor)

