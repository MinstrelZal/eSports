import pymysql
import random
from backend import dbinterface

#db = pymysql.connect('localhost', 'root', 'huhuhu917531', 'test_db')
#cur = db.cursor()
    
#esport_info  data
def ADD_ESPORT():
    dbinterface.Add_ESport("英雄联盟","MOBA")
    dbinterface.Add_ESport("地下城与勇士","ACT")
    dbinterface.Add_ESport("穿越火线","FPS")
    dbinterface.Add_ESport("梦三国","MOBA")
    dbinterface.Add_ESport("王者荣耀","MOBA")
    dbinterface.Add_ESport("龙之谷","ACT")
    dbinterface.Add_ESport("CS_Online","FPS")
    dbinterface.Add_ESport("守望先锋","FPS")
    dbinterface.Add_ESport("风暴英雄","MOBA")
    dbinterface.Add_ESport("冒险岛","ACT")
    
    dbinterface.Add_ESport("绝地求生","FPS")
    dbinterface.Add_ESport("H1Z1","FPS")
    dbinterface.Add_ESport("终结者","FPS")
    dbinterface.Add_ESport("炉石传说","CCG")
    dbinterface.Add_ESport("魔兽世界","RPG")
    dbinterface.Add_ESport("极品飞车ol","SPORT")
    dbinterface.Add_ESport("QQ炫舞","SPORT")
    dbinterface.Add_ESport("梦幻西游","RPG")
    dbinterface.Add_ESport("DOTA2","MOBA")
    dbinterface.Add_ESport("剑网3","ACT")

    for i in range(21,200):
        j = random.randint(1,6)
        if j == 1:
            dbinterface.Add_ESport("Test_name%d"%i,"MOBA")
        elif j == 2:
            dbinterface.Add_ESport("Test_name%d"%i,"ACT")
        elif j == 3:
            dbinterface.Add_ESport("Test_name%d"%i,"CCG")
        elif j == 4:
            dbinterface.Add_ESport("Test_name%d"%i,"RPG")
        elif j == 5:
            dbinterface.Add_ESport("Test_name%d"%i,"FPS")
        elif j == 6:
            dbinterface.Add_ESport("Test_name%d"%i,"SPORT")
    
#league_info  data
def ADD_LEAGUE():
    dbinterface.Add_League("2016LPL春季赛","2016-01-14","2016-04-10")
    dbinterface.Add_League("2016LPL夏季赛","2016-05-26","2016-09-01")
    dbinterface.Add_League("2016LPL秋季赛","2016-09-26","2016-11-25")
    dbinterface.Add_League("2016LPL冬季赛","2016-12-11","2017-01-03")
    dbinterface.Add_League("德玛西亚杯","2016-11-20","2016-12-23")
    dbinterface.Add_League("2017LPL春季赛","2017-01-14","2017-04-10")
    dbinterface.Add_League("2017LPL夏季赛","2017-05-26","2017-09-01")
    dbinterface.Add_League("2017LPL秋季赛","2016-09-26","2016-11-25")
    dbinterface.Add_League("2017LPL冬季赛","2016-12-11","2017-01-03")
    dbinterface.Add_League("季中冠军赛","2017-05-26","2017-09-01")
    
    dbinterface.Add_League("2016全国总决赛","2016-08-21","2016-11-06")
    dbinterface.Add_League("2017全国总决赛","2017-09-23","2017-11-04")
    dbinterface.Add_League("DNF第十届格斗大赛","2017-08-13","2017-09-14")
    dbinterface.Add_League("DNF第九届格斗大赛","2017-04-15","2017-06-24")
    dbinterface.Add_League("DNF第八届格斗大赛","2017-01-23","2017-03-11")
    dbinterface.Add_League("2017炉石传说世界锦标赛","2017-07-03","2017-09-13")
    dbinterface.Add_League("2016炉石传说世界锦标赛","2017-04-15","2017-06-24")
    dbinterface.Add_League("2016炉石传说中美对抗赛","2016-09-26","2016-11-25")
    dbinterface.Add_League("2016炉石传说中欧对抗赛","2016-12-11","2017-01-03")
    dbinterface.Add_League("2017炉石传说中欧对抗赛","2016-12-11","2017-01-03")

    for i in range(21,200):
        j = random.randint(1,5)
        if j == 1:
            dbinterface.Add_League("Test_League%d"%i,"2016-03-13","2016-06-30")
        elif j == 2:
            dbinterface.Add_League("Test_League%d"%i,"2016-07-20","2016-10-19")
        elif j == 3:
            dbinterface.Add_League("Test_League%d"%i,"2017-02-24","2017-05-14")
        elif j == 4:
            dbinterface.Add_League("Test_League%d"%i,"2017-06-26","2017-09-18")
        elif j == 5:
            dbinterface.Add_League("Test_League%d"%i,"2017-09-22","2017-12-27")


#game_info  data
def ADD_GAME():
    for i in range(1,200):
        dbinterface.Add_Game("Name%d"%i,"Time%d"%i,"Location%d"%i,random.randint(1,200),"暂无")
    

    
#club_info  data
def ADD_CLUB():
    dbinterface.Add_Club("InvictusGaming","王思聪","暂无","2010-01-01","暂无")
    dbinterface.Add_Club("TeamWE","瑞派","暂无","2010-01-01","暂无")
    dbinterface.Add_Club("EHOME,HtmL","暂无","暂无","2010-01-01","暂无")
    dbinterface.Add_Club("DK电子竞技俱乐部","清扬","暂无","2010-01-01","暂无")
    dbinterface.Add_Club("LGD电子竞技俱乐部","FTD","暂无","2010-01-01","暂无")

    for i in range(6,200):
        dbinterface.Add_Club("Test%d电子竞技俱乐部"%i,"Sponsor%d"%i,"暂无","2010-01-01","暂无")
    
#team_info  data
def ADD_TEAM():
    for i in range(1,200):
        dbinterface.Add_Team("Name%d"%i,"Coach%d"%i,"暂无",random.randint(1,100),random.randint(1,200))

    
#player_info  data
def ADD_PLAYER():
    for i in range(1,200):
        dbinterface.Add_Player(random.randint(1,20),"Name%d"%i,i%2,"暂无",random.randint(1,100))
    
#league_result  data
def ADD_LEAGUE_RESULT():
    for i in range(1,200):
        dbinterface.Add_League_Result(i,random.randint(1,200),"暂无")
    
    
#game_competitor  data
def ADD_GAME_COM():
    for i in range(1,200):
        dbinterface.Add_Game_Competitor(random.randint(1,200),random.randint(1,100),random.randint(1,100),random.randint(0,1))
    
    

def add_all_data() :
    ADD_ESPORT()
    ADD_LEAGUE()
    ADD_GAME()
    ADD_CLUB()
    ADD_TEAM()
    ADD_PLAYER()
    ADD_LEAGUE_RESULT()
    ADD_GAME_COM()
