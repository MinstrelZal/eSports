from backend import dbinterface

def Logout():
    sql = 'DROP PROCEDURE IF EXISTS `logout`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE logout
             (IN inusername NVARCHAR(30))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM user_info WHERE username=inusername;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      UPDATE user_info SET is_loggedin=0 WHERE username=inusername;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)
    #dbinterface.db.commit()

def Add_User():
    sql = 'DROP PROCEDURE IF EXISTS `add_user`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_user
             (IN inusername NVARCHAR(30),
              IN inpassword NVARCHAR(30),
              IN inis_loggedin TINYINT,
              IN inis_staff TINYINT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM user_info WHERE username=inusername;
                  IF result > 0 THEN
                      ROLLBACK;
                  ELSE
                      INSERT INTO user_info (username, password, is_loggedin, is_staff) VALUES (inusername, inpassword, inis_loggedin, inis_staff);
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)
    #dbinterface.db.commit()

def Alter_User():
    sql = 'DROP PROCEDURE IF EXISTS `alter_user`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_user
             (IN inuser_id INT,
              IN inusername NVARCHAR(30),
              IN inpassword NVARCHAR(30),
              IN inis_staff TINYINT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM user_info WHERE id=inuser_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      UPDATE user_info SET username=inusername,password=inpassword,is_staff=inis_staff WHERE id=inuser_id;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_ESport():
    sql = 'DROP PROCEDURE IF EXISTS `add_esport`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_esport
             (IN inname NVARCHAR(20),
              IN intype NVARCHAR(20))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM esport_info WHERE name=inname;
                  IF result > 0 THEN
                      ROLLBACK;
                  ELSE
                      INSERT INTO esport_info (name, type) VALUES (inname, intype);
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_ESport():
    sql = 'DROP PROCEDURE IF EXISTS `alter_esport`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_esport
             (IN inesport_id INT,
              IN inname NVARCHAR(20),
              IN intype NVARCHAR(20))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM esport_info WHERE id=inesport_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      UPDATE esport_info SET name=inname,type=intype WHERE id=inesport_id;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_League():
    sql = 'DROP PROCEDURE IF EXISTS `add_league`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_league
             (IN inname NVARCHAR(30),
              IN inbegin_time DATE,
              IN inend_time DATE)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM league_info WHERE name=inname;
                  IF result > 0 THEN
                      ROLLBACK;
                  ELSE
                      INSERT INTO league_info (name, begin_time, end_time) VALUES (inname, inbegin_time, inend_time);
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_League():
    sql = 'DROP PROCEDURE IF EXISTS `alter_league`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_league
             (IN inleague_id INT,
              IN inname NVARCHAR(30),
              IN inbegin_time DATE,
              IN inend_time DATE)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM league_info WHERE id=inleague_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      UPDATE league_info SET name=inname,begin_time=inbegin_time,end_time=inend_time WHERE id=inleague_id;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def init_procedures():
    Logout()
    Add_User()
    Alter_User()
    Add_ESport()
    Alter_ESport()
    Add_League()
    Alter_League()
