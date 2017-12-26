import pymysql

db = pymysql.connect('localhost', 'root', 'huhuhu917531', 'test_db')
cur = db.cursor()
#db.set_charset('utf8')

#创建trigger
#  1.删除esport_info条目后，删除game_info和league_info中与删除的esport_info有关的信息
#  2.删除league_info条目后，删除league_info包含的所有game_info信息，和league_result中有关信息
#  3.删除team_info 条目后， 删除player_info属于team_info的选手信息
cur.execute("drop trigger if exists delete_all_esport")
sql = """
           create trigger delete_all_esport
           before delete on esport_info 
           for each row 
           begin 
           delete from game_info 
              where game_info.league_id = ALL 
                 ( 
                     select id 
                     from league_info 
                     where league_info.id = ALL 
                     ( 
                        select league_id 
                        from league_result 
                        where league_result.esport_id = old.id 
                        ) 
                  ); 
           delete from league_info 
              where league_info.id = ALL 
              (
                  select league_id 
                  from league_result 
                  where league_result.esport_id = old.id 
            ); 
           delete from league_result 
           where league_result.esport_id = old.id ;
           end"""

cur.execute(sql)

    #cursor.execute("drop trigger delete_all_game on league_info if exists delete_all_game")
cur.execute("drop trigger if exists delete_all_game")
sql = "    create trigger delete_all_game\
           before delete on league_info \
           for each row \
           begin \
           delete from league_result \
           where league_result.league_id = old.id ;\
           delete from game_info \
           where game_info.league_id = old.id;\
           end"        

cur.execute(sql)

    #cursor.execute("drop trigger delete_player on team_info if exists delete_player")
cur.execute("drop trigger if exists delete_player")
sql = "create trigger delete_player\
        before delete on team_info \
        for each row \
           delete from player_info \
           where player_info.team_id = old.id"

cur.execute(sql)




