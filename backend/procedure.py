from backend import dbinterface

def Add_User():
    #sql = 'delimiter $$'
    #dbinterface.cursor.execute(sql)
    #dbinterface.db.commit()
    sql = 'DROP PROCEDURE IF EXISTS `add_user`;'
    dbinterface.cursor.execute(sql)
    sql = """CREATE PROCEDURE add_user
             (IN username VARCHAR(30),
              IN password VARCHAR(30),
              IN is_loggedin TINYINT,
              IN is_staff TINYINT)
              BEGIN
                  DECLARE result VARCHAR(30) DEFAULT NULL;
                  START TRANSACTION;
                  SELECT password INTO result FROM user_info WHERE username=username;
                  IF result IS NOT NULL THEN
                      ROLLBACK;
                  ELSE
                      INSERT INTO user_info (username, password, is_loggedin, is_staff) VALUES (username, password, is_loggedin, is_staff);
                  END IF;
                  COMMIT;
              END"""
    dbinterface.cursor.execute(sql)
    dbinterface.db.commit()
    #sql = 'DELIMITER ;'
    #dbinterface.cursor.execute(sql)
    #dbinterface.db.commit()

