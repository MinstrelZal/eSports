import pymysql

db = pymysql.connect('localhost', 'root', '20121513zal', 'esports')
cursor = db.cursor()
#db.set_charset('utf8')

#创建trigger
#  1.删除esport_info条目后，删除game_info和league_info中与删除的esport_info有关的信息
#  2.删除league_info条目后，删除league_info包含的所有game_info信息，和league_result中有关信息
#  3.删除team_info 条目后， 删除player_info属于team_info的选手信息
def trigger_init(db,cursor) :
    sql1 = "create trigger \
        if not exists delete_all_esport \
        after delete on esport_info \
        referencing \
           newrow as Newesport \
        for each row \
        begin \
           delete from game_info \
              where game_info.league_id = ALL \
                 ( \
                     select id \
                     from league_info \
                     where league_info.id = ALL \
                     ( \
                        select league_id \
                        from league_result \
                        where league_result.esport_id = Newesport.id \
                        ) \
                  ); \
           delete from league_info \
              where league_info.id = ALL \
              (\
                  select league_id \
                  from league_result \
                  where league_result.esport_id = Newesport.id \
            ); \
           delete from league_result \
           where league_result.esport_id = Newesport.id ;\
         end;"

    cursor.execute(sql1)

    sql1 = "create trigger \
        if not exists delete_all_game \
        after delete on league_info \
        referencing \
           newrow as Newleague \
        for each row \
        begin\
           delete from league_result \
           where league_result.league_id = Newleague.id ;\
           delete from game_info \
           where game_info.league_id = Newleague.id; \
        end;"        

    cursor.execute(sql1)

    sql1 = "create trigger \
        if not exists delete_player \
        after delete on team_info \
        referencing \
           newrow as Newplayer \
        for each row \
        begin \
           delete from player_info \
           where player_info.team_id = Newteam.id \
        end;"

    cursor.execute(sql1)

trigger_init(db, cursor)
