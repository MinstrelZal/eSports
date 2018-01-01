# -*- coding: utf-8 -*-
import pymysql

db = pymysql.connect('localhost', 'root', 'huhuhu917531', 'esport')
cursor = db.cursor()
db.set_charset('utf8')

# ------------------------------ Create Tables ----------------------------------
# by MinstrelZal
# 2017-12-22

def init(db, cursor):
    # create esports_info table
    cursor.execute("DROP TABLE IF EXISTS esport_info")
    sql = """CREATE TABLE `esport_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(20) NOT NULL UNIQUE,
                    `type` VARCHAR(20) DEFAULT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)
    
    cursor.execute("DROP TABLE IF EXISTS league_info")
    sql = """CREATE TABLE `league_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL UNIQUE,
                    `begin_time` DATE DEFAULT NULL,
                    `end_time` DATE DEFAULT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS game_info")
    sql = """CREATE TABLE `game_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL UNIQUE,
                    `time` DATE DEFAULT NULL,
                    `location` VARCHAR(20) DEFAULT NULL,
                    `league_id` INT(11) NOT NULL,
                    `result` VARCHAR(40) NOT NULL,
                    PRIMARY KEY (`id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS club_info")
    sql = """CREATE TABLE `club_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `name` VARCHAR(30) NOT NULL UNIQUE,
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
                    `name` VARCHAR(30) NOT NULL UNIQUE,
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
                    PRIMARY KEY (`id`),
                    UNIQUE KEY (`game_id`, `name`, `gender`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)
   
    cursor.execute("DROP TABLE IF EXISTS user_info")
    sql = """CREATE TABLE `user_info` (
                    `id` INT(11) NOT NULL AUTO_INCREMENT,
                    `username` VARCHAR(30) NOT NULL UNIQUE,
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
                    PRIMARY KEY (`league_id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS game_competitor")
    sql = """CREATE TABLE `game_competitor` (
                    `game_id` INT(11) NOT NULL,
                    `team_id` INT(11) NOT NULL,
                    `player_id` INT(11) NOT NULL,
                    `self` TINYINT NOT NULL,
                    PRIMARY KEY (`game_id`, `team_id`, `player_id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)

    cursor.execute("DROP TABLE IF EXISTS club_esport")
    sql = """CREATE TABLE `club_esport` (
                    `club_id` INT(11) NOT NULL,
                    `esport_id` INT(11) NOT NULL,
                    PRIMARY KEY (`club_id`, `esport_id`)
                    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""
    cursor.execute(sql)


init(db,cursor)
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
    '''
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
    '''
    sql = 'call register_login("%s", "%s", %d, %d);' % (username, password, is_loggedin, is_staff)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('密码错误')
            return 1
        print("(注册)登录成功")
    except:
        db.rollback()
        print("Error: Unable to Register or Login")
        return 1
    return 0

def Logout(username):
    '''
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
    '''
    sql = 'call logout("%s");' % username
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount != 1):
            print('用户名错误')
            return 1
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
    '''
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
    '''
    sql = 'call add_user("%s", "%s", %d, %d);' % (username, password, is_loggedin, is_staff)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('用户已存在')
            return 1
        print("用户添加成功")
    except:
        db.rollback()
        print("Error: Unable to Add User")
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
    sql = 'SELECT id,username,is_staff,is_loggedin FROM user_info WHERE username REGEXP "%s";' % username
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
    fields = ('id', 'username', 'is_staff', 'is_loggedin')
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
    '''
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
    '''
    sql = 'call alter_user(%d, "%s", "%s", %d);' % (user_id, username, password, is_staff)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该用户不存在')
            return 1
        print("编辑用户信息成功")
    except:
        db.rollback()
        print("Error: Unable to Alter User")
        return 1
    return 0

def User_List():
    sql = "SELECT id,username,is_staff,is_loggedin FROM user_info;"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    except:
        print("Error: Unable to select from user_info")
        return 1
    print("获取用户列表成功")
    fields = ('id', 'username', 'is_staff', 'is_loggedin')
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

    sql = 'call add_esport("%s","%s")' % (name, etype)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该项目已存在')
            return 1
        print("项目添加成功")
    except:
        db.rollback()
        print("Error: Unable to insert Add ESport")
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

def Alter_ESport(esport_id, name, etype):
    '''
    sql = 'UPDATE esport_info SET name="%s",type="%s" WHERE id=%d;' % (name, etype, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print("编辑竞技项目信息成功")
    except:
        db.rollback()
        print('Error: Unable to update esport_info')
        return 1
    return 0
    '''
    sql = 'call alter_esport(%d, "%s", "%s");' % (esport_id, name, etype)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1): 
            print("该竞技项目不存在")
            return 1
        print("编辑竞技项目信息成功")
    except:
        db.rollback()
        print('Error: Unable to Alter ESport')
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
    '''
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
    '''
    sql = 'call add_league("%s", "%s", "%s");' % (name, begin_time, end_time)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print("该联赛记录已存在")
            return 1
        print('联赛记录添加成功')
    except:
        db.rollback()
        print('Error: Unable to Add League')
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
    '''
    sql = 'UPDATE league_info SET name="%s",begin_time="%s",end_time="%s" WHERE id=%d;' % (name, begin_time, end_time, league_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑联赛记录信息成功')
    except:
        db.rollback()
        print('Error: Unable to update league_info')
        return 1
    return 0
    '''
    sql = 'call alter_league(%d, "%s", "%s", "%s");' % (league_id, name, begin_time, end_time)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print("该联赛记录不存在")
            return 1
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
    '''
    sql = 'SELECT name FROM league_info WHERE id=%d;' % league_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该联赛信息已删除')
            return 1
    except:
        print('Error: Unable to select from league_info')
        return 1
    sql = 'SELECT name FROM esport_info WHERE id=%d;' % esport_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该竞技项目已删除')
            return 1
    except:
        print('Error: Unable to select from esport_info')
        return 1
    sql = 'SELECT result FROM league_result WHERE league_id=%d;' % league_id
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
    '''
    sql = 'call add_league_result(%d, %d, "%s");' % (league_id, esport_id, result)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print("该联赛信息已删除 or 该竞技项目已删除 or 该联赛结果已登记")
            return 1
        print('联赛结果记录添加成功')
    except:
        db.rollback()
        print('Error: Unable to Add League Result')
        return 1
    return 0

def Delete_League_Result(league_id):
    sql = 'DELETE FROM league_result WHERE league_id=%d;' % league_id
    try:
        cursor.execute(sql)
        db.commit()
        print('删除联赛结果记录成功')
    except:
        db.rollback()
        print('Error: Unable to delete from league_result')
        return 1
    return 0

def Search_League_Result(league_id):
    sql = 'SELECT * FROM league_result WHERE league_id=%d;' % league_id
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
    except:
        print('查询联赛记录结果失败')
        return 1
    if(result == None):
        return {}
    fields = ('league_id', 'esport_id', 'result')
    sql = 'SELECT name FROM league_info WHERE id=%d;' % result[0]
    sql2 = 'SELECT name FROM esport_info WHERE id=%d;' % result[1]
    result = dict(zip(fields, result))    
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该联赛已删除')
            result['league_name'] = 'UNKNOWN'
        else:
            print('查找联赛名称成功')
            result['league_name'] = cursor.fetchone()[0]
    except:
        print('Error: Unable to select from league_info')
        return 1
    try:
        cursor.execute(sql2)
        if(cursor.rowcount < 1):
            print('该竞技项目已删除')
            result['esport_name'] = 'UNKNOWN'
        else:
            print('查找竞技项目成功')
            result['esport_name'] = cursor.fetchone()[0]
    except:
        print('Error: Unable to select from esport_info')
    return result

def Alter_League_Result(league_id, esport_id, result):
    '''
    sql = 'UPDATE league_result SET esport_id=%d,result="%s" WHERE league_id=%d;' % (esport_id, result, league_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('联赛结果记录修改成功')
    except:
        db.rollback()
        print('Error: Unable to update league_result')
        return 1
    return 0
    '''
    sql = 'call alter_league_result(%d, %d, "%s");' % (league_id, esport_id, result)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该联赛结果不存在')
            return 1
        print('联赛结果记录修改成功')
    except:
        db.rollback()
        print('Error: Unable to Alter League Result')
        return 1
    return 0

def League_Result_List():
    sql = 'SELECT * FROM league_result;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from league_info')
        return 1
    print('获取联赛记录列表成功')
    fields = ('league_id', 'esport_id', 'result')
    leaguelist = []
    for row in result:
        sql = 'SELECT name FROM league_info WHERE id=%d;' % row[0]
        sql2 = 'SELECT name FROM esport_info WHERE id=%d;' % row[1]
        row = dict(zip(fields, row))
        try:
            cursor.execute(sql)
            if(cursor.rowcount < 1):
                print('该联赛已删除')
                row['league_name'] = 'UNKNOWN'
            else:
                print('查找联赛名称成功')
                row['league_name'] = cursor.fetchone()[0]
        except:
            print('Error: Unable to select from league_info')
            return 1
        try:
            cursor.execute(sql2)
            if(cursor.rowcount < 1):
                print('该竞技项目已删除')
                row['esport_name'] = 'UNKNOWN'
            else:
                print('查找竞技项目成功')
                row['esport_name'] = cursor.fetchone()[0]
        except:
            print('Error: Unable to select from esport_info')
        leaguelist.append(row)
    print(leaguelist)
    return leaguelist

# ---------------------------- game_info ---------------------------------
# by MinstrelZal
# 2017-12-22

def Add_Game(name, time, location, league_id, result):
    '''
    sql = 'SELECT name FROM league_info WHERE id=%d;' % league_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该联赛信息已删除')
            return 1
    except:
        print('Error: Unable to select from league_info')
        return 1
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
    '''
    sql = 'call add_game("%s", "%s", "%s", %d, "%s");' % (name, time, location, league_id, result)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该联赛信息已删除 or 该比赛记录已登记')
            return 1
        print("添加比赛记录成功")
    except:
        db.rollback()
        print('Error: Unable to Add Game')
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

def Alter_Game(game_id, name, time, location, league_id, result):
    '''
    sql = 'SELECT name FROM league_info WHERE id=%d;' % league_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该联赛信息已删除')
            return 1
    except:
        print('Error: Unable to select from league_info')
        return 1
    sql = 'UPDATE game_info SET name="%s",time="%s",location="%s",league_id=%d,result="%s" WHERE id=%d;' % (name, time, location, league_id, result, game_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑比赛记录成功')
    except:
        db.rollback()
        print('Error: Unable to update game_info')
        return 1
    return 0
    '''
    sql = 'call alter_game(%d, "%s", "%s", "%s", %d, "%s");' % (game_id, name, time, location, league_id, result)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1): 
            print('该联赛信息已删除 or 比赛记录不存在')
            return 1
        print('编辑比赛记录成功')
    except:
        db.rollback()
        print('Error: Unable to Alter Game')
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
    fields = ('id', 'name', 'time', 'location', 'league_id', 'result')
    for row in result:
        sql = 'SELECT name FROM league_info WHERE id=%d;' % row[4]
        row = dict(zip(fields, row))
        try:
            cursor.execute(sql)
            if(cursor.rowcount < 1):
                print('该联赛已被删除')
                row['league_name'] = 'UNKNOWN'
            else:
                print('查找联赛名成功')
                league_name = cursor.fetchone()[0]
                row['league_name'] = league_name
        except:
            print('Error: Unable to select from league_info')
            return 1
        gamelist.append(row)
    print(gamelist)
    return gamelist


#init(db, cursor)

# ---------------------------- club_info & club_esport---------------------------------
# by HUHU
# 2017-12-23
def Add_Club(name, sponsor, achievement, setup_time, founder):
    '''
    sql = 'SELECT id FROM club_info WHERE name="%s";' % name
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该俱乐部信息已登记')
            return 1
    except:
        print('Error: Unable to select from club_info')
        return 1
    sql = 'INSERT INTO club_info (name, sponsor, achievement, setup_time, founder) VALUES ("%s", "%s", "%s", "%s", "%s");' % (name, sponsor, achievement, setup_time, founder)
    try:
        cursor.execute(sql)
        db.commit()
        print("添加俱乐部信息成功")
    except:
        db.rollback()
        print('Error: Unable to insert into club_info')
        return 1
    return 0
    '''
    sql = 'call add_club("%s", "%s", "%s", "%s", "%s");' % (name, sponsor, achievement, setup_time, founder)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print("该俱乐部信息已存在")
            return 1
        print("添加俱乐部信息成功")
    except:
        db.rollback()
        print('Error: Unable to Add Club')
        return 1
    return 0

def Add_Club_ESport(club_id,esport_id):
    '''
    sql = 'SELECT name FROM club_info WHERE id=%d;' % club_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该俱乐部信息已删除')
            return 1
    except:
        print('Error: Unable to select from club_info')
        return 1
    sql = 'SELECT name FROM esport_info WHERE id=%d;' % esport_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该竞技项目已删除')
            return 1
    except:
        print('Error: Unable to select from esport_info')
        return 1
    sql = 'SELECT * FROM club_esport WHERE club_id=%d AND esport_id=%d;' % (club_id, esport_id)
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该俱乐部竞技项目记录已登记')
            return 1
    except:
        print('Error: Unable to select from club_esport')
        return 1
    sql = 'INSERT INTO club_esport (club_id,esport_id) VALUES (%d, %d);' % (club_id,esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print("添加俱乐部涉及项目记录成功")
    except:
        db.rollback()
        print('Error: Unable to insert into club_esport')
        return 1
    return 0
    '''
    sql = 'call add_club_esport(%d, %d);' % (club_id, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该俱乐部信息已删除 or 该竞技项目已删除')
            return 1
        print("添加俱乐部涉及项目记录成功")
    except:
        db.rollback()
        print('Error: Unable to insert into club_esport')
        return 1
    return 0

def Delete_Club(club_id, esport_id):
    sql = 'DELETE FROM club_info WHERE id=%d;' % club_id
    try:
        cursor.execute(sql)
        db.commit()
        print('删除俱乐部信息成功')
    except:
        db.rollback()
        print('Error: Unable to delete from club_info')
        return 1
    return 0

def Delete_Club_ESport(club_id,esport_id):
    sql = 'DELETE FROM club_esport WHERE club_id=%d AND esport_id= %d;' % (club_id,esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('删除俱乐部涉及项目信息成功')
    except:
        db.rollback()
        print('Error: Unable to delete from club_esport')
        return 1
    return 0

def Search_Club(name):
    sql = 'SELECT * FROM club_info WHERE name REGEXP "%s";' % name
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from club_info')
        return 1
    print('查询俱乐部信息成功')
    clublist = []
    fields = ('id', 'name', 'sponsor', 'achievement', 'setup_time', 'founder')
    for row in result:
        row = dict(zip(fields, row))
        clublist.append(row)
    print(clublist)
    return clublist

def Search_Club_ESport(club_id):
    sql = 'SELECT * FROM club_esport WHERE club_id= %d;' % club_id
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from club_esport')
        return 1
    print('查询俱乐部涉及项目成功')
    club_esportlist = []
    fields = ('club_id', 'esport_id')
    for row in result:
        sql = 'SELECT name FROM club_info WHERE id=%d;' % row[0]
        sql2 = 'SELECT name FROM esport_info WHERE id=%d;' % row[1]
        row = dict(zip(fields, row))
        try:
            cursor.execute(sql)
            if(cursor.rowcount < 1):
                print('该俱乐部信息已被删除')
                row['club_name'] = 'UNKNOWN'
            else:
                print('查找俱乐部名称成功')
                club_name = cursor.fetchone()[0]
                row['club_name'] = club_name
        except:
            print('Error: Unable to select from club_info')
            return 1
        try:
            cursor.execute(sql2)
            if(cursor.rowcount < 1):
                print('该竞技项目已被删除')
                row['esport_name'] = 'UNKNOWN'
            else:
                print('查找竞技项目成功')
                esport_name = cursor.fetchone()[0]
                row['esport_name'] = esport_name
        except:
            print('Error: Unable to select from esport_info')
            return 1
        club_esportlist.append(row)
    print(club_esportlist)
    return club_esportlist

def Alter_Club(club_id, name, sponsor, achievement, setup_time, founder):
    '''
    sql = 'UPDATE club_info SET name="%s",sponsor="%s",achievement="%s",setup_time="%s",founder = "%s" WHERE id=%d;' % (name, sponsor, achievement, setup_time, founder,club_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑俱乐部信息成功')
    except:
        db.rollback()
        print('Error: Unable to update club_info')
        return 1
    return 0
    '''
    sql = 'call alter_club(%d, "%s", "%s", "%s", "%s", "%s");' % (club_id, name, sponsor, achievement, setup_time, founder)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print("该俱乐部不存在")
            return 1
        print('编辑俱乐部信息成功')
    except:
        db.rollback()
        print('Error: Unable to Alter Club')
        return 1
    return 0

def Club_List():
    sql = 'SELECT * FROM club_info;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from club_info')
        return 1
    print('获取俱乐部信息列表成功')
    clublist = []
    fields = ('id', 'name', 'sponsor', 'achievement', 'setup_time','founder')
    for row in result:
        row = dict(zip(fields, row))
        clublist.append(row)
    print(clublist)
    return clublist

def Club_ESport_List():
    sql = 'SELECT * FROM club_esport;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from club_esport')
        return 1
    print('获取俱乐部涉及项目列表成功')
    club_esportlist = []
    fields = ('club_id', 'esport_id')
    for row in result:
        sql = 'SELECT name FROM club_info WHERE id=%d;' % row[0]
        sql2 = 'SELECT name FROM esport_info WHERE id=%d;' % row[1]
        row = dict(zip(fields, row))
        try:
            cursor.execute(sql)
            if(cursor.rowcount < 1):
                print('该俱乐部信息已被删除')
                row['club_name'] = 'UNKNOWN'
            else:
                print('查找俱乐部名称成功')
                club_name = cursor.fetchone()[0]
                row['club_name'] = club_name
        except:
            print('Error: Unable to select from club_info')
            return 1
        try:
            cursor.execute(sql2)
            if(cursor.rowcount < 1):
                print('该竞技项目已被删除')
                row['esport_name'] = 'UNKNOWN'
            else:
                print('查找竞技项目成功')
                esport_name = cursor.fetchone()[0]
                row['esport_name'] = esport_name
        except:
            print('Error: Unable to select from esport_info')
            return 1
        club_esportlist.append(row)
    print(club_esportlist)
    return club_esportlist

# ---------------------------- team_info ---------------------------------
# by HUHU
# 2017-12-23
def Add_Team(name, coach, achievement, club_id, esport_id):
    '''
    sql = 'SELECT name FROM club_info WHERE id=%d;' % club_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该俱乐部信息已删除')
            return 1
    except:
        print('Error: Unable to select from club_info')
        return 1
    sql = 'SELECT name FROM esport_info WHERE id=%d;' % esport_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该竞技项目已删除')
            return 1
    except:
        print('Error: Unable to select from esport_info')
        return 1
    sql = 'SELECT id FROM team_info WHERE name="%s";' % name
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该队伍信息已登记')
            return 1
    except:
        print('Error: Unable to select from team_info')
        return 1
    sql = 'INSERT INTO team_info (name, coach, achievement, club_id, esport_id) VALUES ("%s", "%s", "%s", %d, %d);' % (name, coach, achievement, club_id, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        print("添加队伍信息成功")
    except:
        db.rollback()
        print('Error: Unable to insert into team_info')
        return 1
    return 0
    '''
    sql = 'call add_team("%s", "%s", "%s", %d, %d);' % (name, coach, achievement, club_id, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该俱乐部信息已删除 or 该竞技项目信息已删除 or 该队伍信息已登记')
            return 1
        print("添加队伍信息成功")
    except:
        db.rollback()
        print('Error: Unable to Add Team')
        return 1
    return 0

def Delete_Team(team_id):
    sql = 'DELETE FROM team_info WHERE id=%d;' % team_id
    try:
        cursor.execute(sql)
        db.commit()
        print('删除队伍信息成功')
    except:
        db.rollback()
        print('Error: Unable to delete from team_info')
        return 1
    return 0

def Search_Team(name):
    sql = 'SELECT * FROM team_info WHERE name REGEXP "%s";' % name
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from team_info')
        return 1
    print('查询队伍信息成功')
    teamlist = []
    fields = ('id', 'name', 'coach', 'achievement', 'club_id','esport_id')
    for row in result:
        row = dict(zip(fields, row))
        teamlist.append(row)
    print(teamlist)
    return teamlist

def Alter_Team(team_id, name, coach, achievement, club_id, esport_id):
    '''
    sql = 'SELECT name FROM club_info WHERE id=%d;' % club_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该俱乐部信息已删除')
            return 1
    except:
        print('Error: Unable to select from club_info')
        return 1
    sql = 'SELECT name FROM esport_info WHERE id=%d;' % esport_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该竞技项目已删除')
            return 1
    except:
        print('Error: Unable to select from esport_info')
        return 1
    sql = 'UPDATE team_info SET name="%s",coach ="%s",achievement = "%s", club_id = %d, esport_id = %d WHERE id=%d;' % (name, coach, achievement, club_id, esport_id,team_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑队伍信息成功')
    except:
        db.rollback()
        print('Error: Unable to update team_info')
        return 1
    return 0
    '''
    sql = 'call alter_team(%d, "%s", "%s", "%s", %d, %d)' % (team_id, name, coach, achievement, club_id, esport_id)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该俱乐部信息已删除 or 该竞技项目已删除 or 该队伍不存在')
            return 1
        print('编辑队伍信息成功')
    except:
        db.rollback()
        print('Error: Unable to Alter Team')
        return 1
    return 0

def Team_List():
    sql = 'SELECT * FROM team_info;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from team_info')
        return 1
    print('获取队伍信息列表成功')
    teamlist = []
    fields = ('id', 'name', 'coach', 'achievement', 'club_id','esport_id')
    for row in result:
        row = dict(zip(fields, row))
        teamlist.append(row)
    print(teamlist)
    return teamlist



# ---------------------------- player_info ---------------------------------
# by HUHU
# 2017-12-23
def Add_Player(game_id, name, gender, achievement, team_id):
    '''
    sql = 'SELECT name FROM team_info WHERE id=%d;' % team_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该战队信息已删除')
            return 1
    except:
        print('Error: Unable to select from team_info')
        return 1
    sql = 'SELECT id FROM player_info WHERE name="%s";' % name
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该选手信息已登记')
            return 1
    except:
        print('Error: Unable to select from player_info')
        return 1
    sql = 'INSERT INTO player_info (game_id, name, gender, achievement, team_id) VALUES ("%s", "%s", "%s", "%s",%d);' % (game_id, name, gender, achievement, team_id)
    try:
        cursor.execute(sql)
        db.commit()
        print("添加选手信息成功")
    except:
        db.rollback()
        print('Error: Unable to insert into player_info')
        return 1
    return 0
    '''
    sql = 'call add_player("%s", "%s", %d, "%s", %d);' % (game_id, name, gender, achievement, team_id)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该战队信息已删除 or 该选手信息已登记')
            return 1
        print("添加选手信息成功")
    except:
        db.rollback()
        print('Error: Unable to Add Player')
        return 1
    return 0

def Delete_Player(player_id):
    sql = 'DELETE FROM player_info WHERE id=%d;' % player_id
    try:
        cursor.execute(sql)
        db.commit()
        print('删除选手信息成功')
    except:
        db.rollback()
        print('Error: Unable to delete from player_info')
        return 1
    return 0

def Search_Player(game_id):
    sql = 'SELECT * FROM player_info WHERE game_id REGEXP "%s";' % game_id
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from player_info')
        return 1
    print('查询选手信息成功')
    playerlist = []
    fields = ('id', 'game_id','name', 'gender', 'achievement', 'team_id')
    for row in result:
        row = dict(zip(fields, row))
        playerlist.append(row)
    print(playerlist)
    return playerlist

def Alter_Player(player_id, game_id, name, gender, achievement, team_id):
    '''
    sql = 'SELECT name FROM team_info WHERE id=%d;' % team_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该战队信息已删除')
            return 1
    except:
        print('Error: Unable to select from team_info')
        return 1
    sql = 'UPDATE player_info SET game_id="%s" , name = "%s",gender = "%s" , achievement = "%s" , team_id = %d WHERE id=%d;' % (game_id, name, gender, achievement, team_id, player_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑选手信息成功')
    except:
        db.rollback()
        print('Error: Unable to update player_info')
        return 1
    return 0
    '''
    sql = 'call alter_player(%d, "%s", "%s", %d, "%s", %d);' % (player_id, game_id, name, gender, achievement, team_id)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print("该战队信息已删除 or 该选手不存在")
            return 1
        print('编辑选手信息成功')
    except:
        db.rollback()
        print('Error: Unable to Alter Player')
        return 1
    return 0

def Player_List():
    sql = 'SELECT * FROM player_info;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from player_info')
        return 1
    print('获取选手信息列表成功')
    playerlist = []
    fields = ('id', 'game_id','name', 'gender', 'achievement', 'team_id')
    for row in result:
        row = dict(zip(fields, row))
        playerlist.append(row)
    print(playerlist)
    return playerlist



# ---------------------------- game_competitor ---------------------------------
# by HUHU
# 2017-12-23
def Add_Game_Competitor(game_id, team_id, player_id, self):
    '''
    sql = 'SELECT name FROM game_info where id=%d;' % game_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该比赛信息已删除')
            return 1
    except:
        print('Error: Unable to select from game_info')
        return 1
    sql = 'SELECT name FROM team_info where id=%d;' % team_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该战队信息已删除')
            return 1
    except:
        print('Error: Unable to select from team_info')
        return 1
    sql = 'SELECT name FROM player_info where id=%d;' % player_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该选手信息已删除')
            return 1
    except:
        print('Error: Unable to select from player_info')
        return 1
    sql = 'SELECT self FROM game_competitor WHERE game_id = %d AND team_id=%d AND player_id=%d;' % (game_id, team_id, player_id)
    try:
        cursor.execute(sql)
        if(cursor.rowcount == 1):
            print('该比赛参赛信息记录已登记')
            return 1
    except:
        print('Error: Unable to select from game_competitor')
        return 1
    sql = 'INSERT INTO game_competitor (game_id, team_id, player_id, self) VALUES (%d, %d, %d, %d);' % (game_id, team_id, player_id, self)
    try:
        cursor.execute(sql)
        db.commit()
        print("添加比赛参赛信息记录成功")
    except:
        db.rollback()
        print('Error: Unable to insert into game_competitor')
        return 1
    return 0
    '''
    sql = 'call add_game_competitor(%d, %d, %d, %d);' % (game_id, team_id, player_id, self)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该比赛信息已删除 or 该战队信息已删除 or 该选手信息已删除 or 该比赛参赛信息已登记')
            return 1
        print("添加比赛参赛信息记录成功")
    except:
        db.rollback()
        print('Error: Unable to Add Game Competitor')
        return 1
    return 0

def Delete_Game_Competitor(game_id, team_id, player_id):
    sql = 'DELETE FROM game_competitor WHERE game_id=%d AND team_id=%d AND player_id=%d;' % (game_id, team_id, player_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('删除比赛参赛信息记录成功')
    except:
        db.rollback()
        print('Error: Unable to delete from game_competitor')
        return 1
    return 0

def Search_Game_Competitor(game_id):
    sql = 'SELECT * FROM game_competitor WHERE game_id=%d;' % game_id
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from game_competitor')
        return 1
    print('查询比赛参赛信息成功')
    game_competitorlist = []
    fields = ('game_id', 'team_id','player_id', 'self')
    for row in result:
        row = dict(zip(fields, row))
        game_competitorlist.append(row)
    print(game_competitorlist)
    return game_competitorlist

def Alter_Game_Competitor(game_id, team_id, player_id, self):
    '''
    sql = 'SELECT name FROM game_info where id=%d;' % game_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该比赛信息已删除')
            return 1
    except:
        print('Error: Unable to select from game_info')
        return 1
    sql = 'SELECT name FROM team_info where id=%d;' % team_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该战队信息已删除')
            return 1
    except:
        print('Error: Unable to select from team_info')
        return 1
    sql = 'SELECT name FROM player_info where id=%d;' % player_id
    try:
        cursor.execute(sql)
        if(cursor.rowcount < 1):
            print('该选手信息已删除')
            return 1
    except:
        print('Error: Unable to select from player_info')
        return 1
    sql = 'UPDATE game_competitor SET self=%d WHERE game_id=%d AND team_id=%d AND player_id=%d;' % (self, game_id, team_id, player_id)
    try:
        cursor.execute(sql)
        db.commit()
        print('编辑比赛参赛信息成功')
    except:
        db.rollback()
        print('Error: Unable to update game_competitor')
        return 1
    return 0
    '''
    sql = 'call alter_game_competitor(%d, %d, %d, %d);' % (game_id, team_id, player_id, self)
    try:
        cursor.execute(sql)
        db.commit()
        if(cursor.rowcount < 1):
            print('该比赛信息已删除 or 该战队信息已删除 or 该选手信息已删除 or 该比赛参赛信息不存在')
            return 1
        print('编辑比赛参赛信息成功')
    except:
        db.rollback()
        print('Error: Unable to Alter Game Competitor')
        return 1
    return 0

def Game_Competitor_List():
    sql = 'SELECT * FROM game_competitor;'
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
    except:
        print('Error: Unable to select from game_competitor')
        return 1
    print('获取比赛参赛信息列表成功')
    game_competitorlist = []
    fields = ('game_id','team_id', 'player_id', 'self')
    for row in result:
        row = dict(zip(fields, row))
        game_competitorlist.append(row)
    print(game_competitorlist)
    return game_competitorlist



Add_ESport("英雄联盟","MOBA")
