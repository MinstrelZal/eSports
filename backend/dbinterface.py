import pymysql

db = pymysql.connect('localhost', 'root', '20121513zal', 'esports')
cursor = db.cursor()

def init(db, cursor):
    # create esports_info table
    cursor.execute("DROP TABLE IF EXISTS esport_info")
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

def Delete_User(username):
    sql = 'DELETE FROM user_info WHERE username="%s";' % username
    try:
        cursor.execute(sql)
        db.commit()
        print("删除用户成功")
    except:
        print("Error: Unable to delete from user_info")
        return 1
    return 0

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
        print("Error: Unable to update user_info")
        return 1
    return 0

#init(db, cursor)

