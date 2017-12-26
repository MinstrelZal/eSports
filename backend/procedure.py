# procedures declaration in mysql
# create by MinstrelZal
# 2017-12-25

from backend import dbinterface

def Register_Login():
    sql = 'DROP PROCEDURE IF EXISTS `register_login`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE register_login
             (IN inusername NVARCHAR(30),
              IN inpassword NVARCHAR(30),
              IN inis_loggedin TINYINT,
              IN inis_staff TINYINT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  DECLARE pswd VARCHAR(30) DEFAULT NULL;
                  SELECT COUNT(*) INTO result FROM user_info WHERE username=inusername;
                  IF result > 0 THEN
                      SELECT password INTO pswd FROM user_info WHERE username=inusername;
                      IF inpassword <> pswd THEN
                          ROLLBACK;
                      ELSE
                          UPDATE user_info SET is_loggedin=1 WHERE username=inusername;
                      END IF;
                  ELSE
                      INSERT INTO user_info (username, password, is_loggedin, is_staff) VALUES (inusername, inpassword, inis_loggedin, inis_staff);
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

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

def Add_League_Result():
    sql = 'DROP PROCEDURE IF EXISTS `add_league_result`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_league_result
             (IN inleague_id INT,
              IN inesport_id INT,
              IN inresult NVARCHAR(30))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM league_info WHERE id=inleague_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM esport_info WHERE id=inesport_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          SELECT COUNT(*) INTO result FROM league_result WHERE league_id=inleague_id;
                          IF result > 0 THEN
                              ROLLBACK;
                          ELSE
                              INSERT INTO league_result (league_id, esport_id, result) VALUES (inleague_id, inesport_id, inresult);
                          END IF;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_League_Result():
    sql = 'DROP PROCEDURE IF EXISTS `alter_league_result`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_league_result
             (IN inleague_id INT,
              IN inesport_id INT,
              IN inresult NVARCHAR(30))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM league_result WHERE league_id=inleague_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      UPDATE league_result SET esport_id=inesport_id,result=inresult WHERE league_id=inleague_id;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_Game():
    sql = 'DROP PROCEDURE IF EXISTS `add_game`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_game
             (IN inname NVARCHAR(30),
              IN intime DATE,
              IN inlocation NVARCHAR(30),
              IN inleague_id INT,
              IN inresult NVARCHAR(20))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM league_info WHERE id=inleague_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM game_info WHERE name=inname;
                      IF result > 0 THEN
                          ROLLBACK;
                      ELSE
                          INSERT INTO game_info (name, time, location, league_id, result) VALUES (inname, intime, inlocation, inleague_id, inresult);
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_Game():
    sql = 'DROP PROCEDURE IF EXISTS `alter_game`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_game
             (IN ingame_id INT,
              IN inname NVARCHAR(30),
              IN intime DATE,
              IN inlocation NVARCHAR(30),
              IN inleague_id INT,
              IN inresult NVARCHAR(20))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM league_info WHERE id=inleague_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM game_info WHERE id=ingame_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          UPDATE game_info SET name=inname,time=intime,location=inlocation,league_id=inleague_id,result=inresult WHERE id=ingame_id;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_Club():
    sql = 'DROP PROCEDURE IF EXISTS `add_club`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_club
             (IN inname NVARCHAR(30),
              IN insponsor NVARCHAR(30),
              IN inachievement NVARCHAR(255),
              IN insetup_time DATE,
              IN infounder NVARCHAR(20))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM club_info WHERE name=inname;
                  IF result > 0 THEN
                      ROLLBACK;
                  ELSE
                      INSERT INTO club_info (name, sponsor, achievement, setup_time, founder) VALUES (inname, insponsor, inachievement, insetup_time, infounder);
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_Club():
    sql = 'DROP PROCEDURE IF EXISTS `alter_club`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_club
             (IN inclub_id INT,
              IN inname NVARCHAR(30),
              IN insponsor NVARCHAR(30),
              IN inachievement NVARCHAR(255),
              IN insetup_time DATE,
              IN infounder NVARCHAR(20))
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM club_info WHERE id=inclub_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      UPDATE club_info SET name=inname,sponsor=insponsor,achievement=inachievement,setup_time=insetup_time,founder=infounder WHERE id=inclub_id;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_Team():
    sql = 'DROP PROCEDURE IF EXISTS `add_team`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_team
             (IN inname NVARCHAR(30),
              IN incoach NVARCHAR(30),
              IN inachievement NVARCHAR(255),
              IN inclub_id INT,
              IN inesport_id INT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM club_info WHERE id=inclub_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM esport_info WHERE id=inesport_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          SELECT COUNT(*) INTO result FROM team_info WHERE name=inname;
                          IF result > 0 THEN
                              ROLLBACK;
                          ELSE
                              INSERT INTO team_info (name, coach, achievement, club_id, esport_id) VALUES (inname, incoach, inachievement, inclub_id, inesport_id);
                          END IF;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_Team():
    sql = 'DROP PROCEDURE IF EXISTS `alter_team`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_team
             (IN inteam_id INT,
              IN inname NVARCHAR(30),
              IN incoach NVARCHAR(30),
              IN inachievement NVARCHAR(255),
              IN inclub_id INT,
              IN inesport_id INT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM club_info WHERE id=inclub_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM esport_info WHERE id=inesport_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          SELECT COUNT(*) INTO result FROM team_info WHERE id=inteam_id;
                          IF result < 1 THEN
                              ROLLBACK;
                          ELSE
                              UPDATE team_info SET name=inname,coach=incoach,achievement=inachievement,club_id=inclub_id,esport_id=inesport_id WHERE id=inteam_id;
                          END IF;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_Player():
    sql = 'DROP PROCEDURE IF EXISTS `add_player`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_player
             (IN ingame_id NVARCHAR(30),
              IN inname NVARCHAR(30),
              IN ingender TINYINT,
              IN inachievement NVARCHAR(255),
              IN inteam_id INT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM team_info WHERE id=inteam_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM player_info WHERE game_id=ingame_id AND name=inname AND gender=ingender;
                      IF result > 0 THEN
                          ROLLBACK;
                      ELSE
                          INSERT INTO player_info (game_id, name, gender, achievement, team_id) VALUES (ingame_id, inname, ingender, inachievement, inteam_id);
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_Player():
    sql = 'DROP PROCEDURE IF EXISTS `alter_player`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_player
             (IN inplayer_id INT,
              IN ingame_id NVARCHAR(30),
              IN inname NVARCHAR(30),
              IN ingender TINYINT,
              IN inachievement NVARCHAR(255),
              IN inteam_id INT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM team_info WHERE id=inteam_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM player_info WHERE id=inplayer_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          UPDATE player_info SET game_id=ingame_id,name=inname,gender=ingender,achievement=inachievement,team_id=inteam_id WHERE id=inplayer_id;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_Game_Competitor():
    sql = 'DROP PROCEDURE IF EXISTS `add_game_competitor`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_game_competitor
             (IN ingame_id INT,
              IN inteam_id INT,
              IN inplayer_id INT,
              IN inself TINYINT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM game_info WHERE id=ingame_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM team_info WHERE id=inteam_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          SELECT COUNT(*) INTO result FROM player_info WHERE id=inplayer_id;
                          IF result < 1 THEN
                              ROLLBACK;
                          ELSE
                              SELECT COUNT(*) INTO result FROM game_competitor WHERE game_id=ingame_id AND team_id=inteam_id AND player_id=inplayer_id;
                              IF result > 0 THEN
                                  ROLLBACK;
                              ELSE
                                  INSERT INTO game_competitor (game_id, team_id, player_id, self) VALUES (ingame_id, inteam_id, inplayer_id, inself);
                              END IF;
                          END IF;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Alter_Game_Competitor():
    sql = 'DROP PROCEDURE IF EXISTS `alter_game_competitor`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE alter_game_competitor
             (IN ingame_id INT,
              IN inteam_id INT,
              IN inplayer_id INT,
              IN inself TINYINT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM game_info WHERE id=ingame_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM team_info WHERE id=inteam_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          SELECT COUNT(*) INTO result FROM player_info WHERE id=inplayer_id;
                          IF result < 1 THEN
                              ROLLBACK;
                          ELSE
                              SELECT COUNT(*) INTO result FROM game_competitor WHERE game_id=ingame_id AND team_id=inteam_id AND player_id=inplayer_id;
                              IF result < 1 THEN
                                  ROLLBACK;
                              ELSE
                                  UPDATE game_competitor SET self=inself WHERE game_id=ingame_id AND team_id=inteam_id AND player_id=inplayer_id;
                              END IF;
                          END IF;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def Add_Club_ESport():
    sql = 'DROP PROCEDURE IF EXISTS `add_club_esport`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_club_esport
             (IN inclub_id INT,
              IN inesport_id INT)
              BEGIN
                  DECLARE result INT DEFAULT 0;
                  SELECT COUNT(*) INTO result FROM club_info WHERE id=inclub_id;
                  IF result < 1 THEN
                      ROLLBACK;
                  ELSE
                      SELECT COUNT(*) INTO result FROM esport_info WHERE id=inesport_id;
                      IF result < 1 THEN
                          ROLLBACK;
                      ELSE
                          SELECT COUNT(*) INTO result FROM club_esport WHERE club_id=inclub_id AND esport_id=inesport_id;
                          IF result > 0 THEN
                              ROLLBACK;
                          ELSE
                              INSERT INTO club_esport (club_id, esport_id) VALUES (inclub_id, inesport_id);
                          END IF;
                      END IF;
                  END IF;
              END"""
    dbinterface.cursor.execute(sql)

def init_procedures():
    Register_Login()
    Logout()
    Add_User()
    Alter_User()
    Add_ESport()
    Alter_ESport()
    Add_League()
    Alter_League()
    Add_League_Result()
    Alter_League_Result()
    Add_Game()
    Alter_Game()
    Add_Club()
    Alter_Club()
    Add_Team()
    Alter_Team()
    Add_Player()
    Alter_Player()
    Add_Game_Competitor()
    Alter_Game_Competitor()
    Add_Club_ESport()
