import pymysql
import random
import dbinterface

db = pymysql.connect('localhost', 'root', 'huhuhu917531', 'esport')
cursor = db.cursor()
    
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
    
    dbinterface.Add_League("S6世界总决赛","2016-08-21","2016-11-06")
    dbinterface.Add_League("S7世界总决赛","2017-09-23","2017-11-04")
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
    dbinterface.Add_Game("LPL春季赛第一周周一第一场","2017-01-19","上海浦东新区陆家嘴168号正大广场9楼",6,"RNG 0:2 IM")
    dbinterface.Add_Game("LPL春季赛第一周周一第二场","2017-01-19","上海浦东新区陆家嘴168正大广场9楼",6,"IG 2:0 OMG")
    dbinterface.Add_Game("LPL春季赛第一周周二第一场","2017-01-20","上海浦东新区陆家嘴168号正大广场9楼",6,"WE 2:1 NB")
    dbinterface.Add_Game("LPL春季赛第一周周二第二场","2017-01-20","上海浦东新区陆家嘴168号正大广场9楼",6,"EDG 2:0 VG")
    dbinterface.Add_Game("LPL春季赛第一周周三第一场","2017-01-21","上海浦东新区陆家嘴168号正大广场9楼",6,"IM 2:1 LGD")
    dbinterface.Add_Game("LPL春季赛第一周周三第二场","2017-01-21","上海浦东新区陆家嘴168号正大广场9楼",6,"SS 2:0 IG")
    dbinterface.Add_Game("LPL春季赛第一周周三第三场","2017-01-21","上海浦东新区陆家嘴168号正大广场9楼",6,"RNG 2:1 OMG")
    dbinterface.Add_Game("lolS7总决赛四分之一决赛第一场","2017-10-19","广州体育馆",12,"LZ 0:3 SSG")
    dbinterface.Add_Game("lolS7总决赛四分之一决赛第二场","2017-10-20","广州体育馆",12,"SKT 3:2 MSF")
    dbinterface.Add_Game("lolS7总决赛四分之一决赛第三场","2017-10-21","广州体育馆",12,"RNG 0:3 FNC")

    dbinterface.Add_Game("lolS7总决赛四分之一决赛第四场","2017-10-22","广州体育馆",12,"WE 1:3 SSG")
    dbinterface.Add_Game("lolS7总决赛半决赛第一场","2017-10-28","上海东方体育中心",12,"RNG 2:3 SKT")
    dbinterface.Add_Game("lolS7总决赛半决赛第二场","2017-10-29","上海东方体育中心",12,"WE 1:3 SSG")
    dbinterface.Add_Game("lolS7总决赛决赛第一场","2017-10-28","北京国家体育馆 鸟巢",12,"SSG 3:0 SKT")
    dbinterface.Add_Game("中欧对抗赛小组赛第一轮一场","2017-05-04","上海东方体育中心",20,"Xixo 3:0 lovelychook")
    dbinterface.Add_Game("中欧对抗赛小组赛第一轮二场","2017-05-04","上海东方体育中心",20,"Orange 3:2 SuperJJ")
    dbinterface.Add_Game("中欧对抗赛小组赛第一轮三场","2017-05-04","上海东方体育中心",20,"OMJasonZhou 3:1 K神")
    dbinterface.Add_Game("中欧对抗赛小组赛第一轮四场","2017-05-04","上海东方体育中心",20,"Shtan 3:2 OMHam")
    dbinterface.Add_Game("中欧对抗赛小组赛第二轮一场","2017-05-05","上海东方体育中心",20,"OmZero 3:2 SuperJJ")
    dbinterface.Add_Game("中欧对抗赛小组赛第二轮二场","2017-05-05","上海东方体育中心",20,"ahqDogggg 1:3 Rdu")
    
    for i in range(21,200):
        dbinterface.Add_Game("Name%d"%i,"2010-01-01","Location%d"%i,random.randint(1,20),"暂无")
    

    
#club_info  data
def ADD_CLUB():
    dbinterface.Add_Club("InvictusGaming","暂无","2013年俱乐部英雄联盟分部斩获S3全球总决赛亚军。\n \
                                      2014年俱乐部英雄联盟分部在S4全球总决赛中再次获得亚军。\n \
                                      2017年S7全球总决赛 四强","2009-03-04","王思聪")
    dbinterface.Add_Club("TeamWE","瑞派","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2003-04-27","唐镇,杨天等")
    dbinterface.Add_Club("EHOME,HtmL","暂无","2014年 \n \
                                    第一届德玛西亚杯冠军 \n\
                                    英雄联盟职业联赛春季赛	亚军 \n\
                                    2015 \n \
                                    英雄联盟职业联赛夏季赛季军","2007-11-08","吴秀丽等")
    dbinterface.Add_Club("DK电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2006-11-07","李哲浩，王彬尧等")
    dbinterface.Add_Club("LGD电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2005-11-03","胡祥瑞")
    dbinterface.Add_Club("RNG","暂无","2014年 \n \
                                    第一届德玛西亚杯冠军 \n\
                                    英雄联盟职业联赛春季赛	亚军 \n\
                                    2015 \n \
                                    英雄联盟职业联赛夏季赛季军","2004-03-01","杨天宝")
    dbinterface.Add_Club("IMay电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2003-05-05","郭志林")
    dbinterface.Add_Club("OMG电子竞技俱乐部","暂无","2014年 \n \
                                    第一届德玛西亚杯冠军 \n\
                                    英雄联盟职业联赛春季赛	亚军 \n\
                                    2015 \n \
                                    英雄联盟职业联赛夏季赛季军 \n \
                                    德玛西亚杯年终总决赛亚军","2009-06-16","强文涛")
    dbinterface.Add_Club("NB电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2015-07-25","潘林")
    dbinterface.Add_Club("EDG电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2013-09-23","张文")

    dbinterface.Add_Club("VG电子竞技俱乐部","暂无","2013LPL春季赛冠军 \n \
                                        2013LPL年春季赛13连胜","2011-12-11","赵东来")
    dbinterface.Add_Club("LGD电子竞技俱乐部","暂无","2013LPL春季赛冠军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2012-11-18","赵月初")
    dbinterface.Add_Club("SS电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2013-10-17","涂雅")
    dbinterface.Add_Club("LZ电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2014-04-16","果然翁")
    dbinterface.Add_Club("SKT电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2013-04-01","林雄")
    dbinterface.Add_Club("MSF电子竞技俱乐部","暂无","2013年俱乐部英雄联盟分部斩获S3全球总决赛亚军。\n \
                                      2014年俱乐部英雄联盟分部在S4全球总决赛中再次获得亚军。\n \
                                      2017年S7全球总决赛 四强","2012-06-24","万春菊")
    dbinterface.Add_Club("FNC电子竞技俱乐部","暂无","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军","2013-08-09","秦磊")
    
    for i in range(18,200):
        dbinterface.Add_Club("Test%d电子竞技俱乐部"%i,"Sponsor%d"%i,"暂无","2010-01-01","暂无")
    
#team_info  data
def ADD_TEAM():
    dbinterface.Add_Team("RNG","火狐","2013年俱乐部英雄联盟分部斩获S3全球总决赛亚军。\n \
                                      2014年俱乐部英雄联盟分部在S4全球总决赛中再次获得亚军。\n \
                                      2017年S7全球总决赛 四强",6,1)
    dbinterface.Add_Team("IM","克里斯","2016年04月12日，2016 LSPL职业联赛春季赛冠军（EDE时期） \n \
                                       2016年08月15日，2016LPL职业联赛季军 \n \
                                       2016年11月13日，2016德玛西亚杯-苏州武汉亚军 \n \
                                       2017年06月04日，2017德玛西亚杯•金鹰电竞站亚军",7,1)
    dbinterface.Add_Team("IG","玛法","2014年 \n \
                                    第一届德玛西亚杯冠军 \n\
                                    英雄联盟职业联赛春季赛	亚军 \n\
                                    英雄联盟职业联赛夏季赛季军",1,1)
    dbinterface.Add_Team("OMG","SMLZ","2013LPL春季赛冠军 \n \
                                        2013LPL年春季赛13连胜",8,1)
    dbinterface.Add_Team("WE","周浩","2015年  \n \
                                     IEM9世界总决赛 \n \
                                     德玛西亚杯重庆站殿军 \n \
                                     2017年MSI季中邀请赛四强 \n \
                                     2017英雄联盟全球总决赛四强 ",2,1)
    
    dbinterface.Add_Team("NB","周啸天","2015年  \n \
                                     IEM9世界总决赛 \n \
                                     2017年MSI季中邀请赛四强 \n \
                                     2017英雄联盟全球总决赛四强 ",9,1)
    dbinterface.Add_Team("EDG","王明月","2013LPL春季赛冠军 \n \
                                        2013LPL年春季赛13连胜",10,1)
    dbinterface.Add_Team("VG","东方月初","2015 \n \
                                    英雄联盟职业联赛春季赛季军\n \
                                    德玛西亚杯年终总决赛亚军 \n \
                                    全国电子竞技大赛冠军",11,1)
    dbinterface.Add_Team("LGD","蛮兔","2015年  \n \
                                     IEM9世界总决赛 \n \
                                     德玛西亚杯重庆站殿军 \n \
                                     2017年MSI季中邀请赛四强 \n \
                                     2017英雄联盟全球总决赛四强 ",12,1)
    dbinterface.Add_Team("SS","旭旭宝宝","2013年俱乐部英雄联盟分部斩获S3全球总决赛亚军。\n 2014年俱乐部英雄联盟分部在S4全球总决赛中再次获得亚军。\n \
                                      2017年S7全球总决赛 四强",13,1)

    dbinterface.Add_Team("LZ","jaychou","2013LPL春季赛冠军 \n \
                                        2013LPL年春季赛13连胜",14,1)
    dbinterface.Add_Team("SKT","王加仑","2015年  \n \
                                     IEM9世界总决赛 \n \
                                     2017年MSI季中邀请赛四强 \n \
                                     2017英雄联盟全球总决赛四强 ",15,1)
    dbinterface.Add_Team("MSF","辰南","2015 \n \
                                    英雄联盟职业联赛春季赛季军\n \
                                    德玛西亚杯年终总决赛亚军 \n \
                                    全国电子竞技大赛冠军",16,1)
    
    dbinterface.Add_Team("FNC","唐三","2013年俱乐部英雄联盟分部斩获S3全球总决赛亚军。\n \
                                      2017年8月25日，LPL夏季赛半决赛，RNG战队3-2战胜WE战队并成功晋级S7总决赛；9月1日，RNG战队2-3负于EDG战队获得2017LPL夏季赛亚军。\n \
                                      2017年S7全球总决赛 四强",17,1)
    
    for i in range(15,200):
        dbinterface.Add_Team("Name%d"%i,"Coach%d"%i,"暂无",random.randint(1,20),random.randint(1,20))

    
#player_info  data
def ADD_PLAYER():
    dbinterface.Add_Player(1,"Dade",1,"在S3世界总决赛和13-14赛季OGN冬季赛决赛中的糟糕表现后，三星集团将他交换到了Blue战队。自那以后，他两次出现在OGN决赛的舞台中，赢得了一座OGN冠军，一次个人MVP还有一次大师赛的冠军。SKT T1 K的Faker和他应该是同一级别的选手，但是Dade可能更占上风。",1)
    dbinterface.Add_Player(2,"mata",1,"虽然S3Ozone在世界比赛上的表现非常不尽人意，但S4的世界总冠军说明了一切。 和Dade，Imp和Dandy组队是任何人的梦想，但是Mata向人们展示了他并不会被这些人的光芒掩盖，而是会将这些队员进一步升华。诚然，SSW的队员几乎都是世界上最强之一，但Mata是这一切的地基。",2)
    dbinterface.Add_Player(3,"诺夏",1,"诺夏曾经登顶国服rank，作为一个辅助可见其真实水平。诺夏在读完高中后就开始进入LOL职业圈，他先是加入了IG明星主播皮小秀的YY战队，最终获得那届YSL的第三名。在全新的2014LPL夏季赛上，诺夏被OMG战队选中，成为战队的替补，他和有着同样经历的爱萝莉一样，靠着自己的实力加入国内一线战队",3)
    dbinterface.Add_Player(4,"kakao",1,"2014OGN夏季赛决赛，那个时候的三星是接替SKT的王朝，而那个时候的三星蓝队是三星王朝的主人。几乎很少有人会认为一路坎坎坷坷的走到决赛的盲选王者会战胜不可一世的三星连队，因为那时的三星蓝队看起来不可战胜。2014OGN夏季赛，Kakao终于为KT集团拿下了早该属于他们的冠军，这迟来了一年的荣耀让Kakao充满了希望和斗志。",4)
    dbinterface.Add_Player(5,"厂长",1,"中国知名电子竞技选手，英雄联盟前WE战队打野选手，现EDG战队打野选手。2012年8月加入WE，中国LOL首个世界冠军——IPL5冠军成员，帮助战队一年内获得十冠。2013年中国LOL全明星成员。2014年加入广州EDG电子竞技俱乐部，帮助战队一年内夺得八冠、迅速成长为国内顶尖强队",5)
    dbinterface.Add_Player(6,"扣肉",1,"Koro1是由诺言推荐进入EDG战队，期初表现并不是很亮眼还时常出现失误，但是进入夏季赛，Koro1也慢慢了适应了比赛的节奏，开始渐入佳境。在比赛中，Koro1也开始成为EDG的一个Carry点，Koro1在比赛中使用的英雄往往都是版本最强势的英雄，跟着版本走无疑是最稳的打法，而且Koro1在使用这些英雄时还十分得心应手",6)
    dbinterface.Add_Player(7,"gogoing",1,"曾经的带头大哥让人闻其声，散其胆。在以前天团的比赛中大哥还是一个有血有肉的汉子，在世界比赛中越南鳄让人害怕。但天团随着粉丝的众多，人气的暴涨，天团已经开始出自己主打歌曲。",7)
    dbinterface.Add_Player(8,"娜美",1,"娜美是从LSPL到LPL的一个励志队员。一路走来辛苦很多，在EDG战队中表现非常出色而引起大家的关注，团战能把输出打满的ADC，但是由于电竞三帅五五开曾经开玩笑的一句话草粉狂魔，而让一些人每逢比赛必黑的选手，娜美本人其实非常低调。没有自拍，没有出专辑，没有发微博，还是一个比较低调实力型选手",8)
    dbinterface.Add_Player(9,"cool",1,"虽然让观众和对手印象深刻的是他的阿狸，不过他慢慢地因为其高超的亚索表现而知名，一个非常能够表达出他顶尖操作的英雄。而现在版本流行的刺客型组合也让他受益良多，比如菲兹，还有其他现在炙手可热的法师瑞兹和奥莉安娜等等。",9)
    dbinterface.Add_Player(10,"小胖",1,"pawn其实成名已久，在去年韩国赛区WCG预选赛上，在第一次遇到Faker时，他就使用豹女单杀了Faker的发条，在这之前Faker只被无状态的辛德拉单杀过。一时间，这个仅仅只有16岁的少年引起了大家的注意。",10)

    
    for i in range(11,200):
        dbinterface.Add_Player(random.randint(1,20),"Name%d"%i,i%2,"暂无",random.randint(1,20))
    
#league_result  data
def ADD_LEAGUE_RESULT():
    
    dbinterface.Add_League_Result(1,1,"本赛季LPL春季赛将采用全新的分组赛制进行比赛")
    dbinterface.Add_League_Result(2,1,"一个强力的打野决定了一个队伍的上限")
    dbinterface.Add_League_Result(3,1,"运营还是打架，谁才能代表LPL")
    dbinterface.Add_League_Result(4,1,"LPL中的打架队和运营队可谓各占半壁江山")
    dbinterface.Add_League_Result(5,1,"EDG模式和金元政策")
    dbinterface.Add_League_Result(6,1,"EDG模式，笔者认为是以运营这一战术为建队核心")
    dbinterface.Add_League_Result(7,1,"老牌俱乐部的阵痛期是否已经到来")
    dbinterface.Add_League_Result(8,1,"去年的WE，今年的OMG和IG，如今看来，境况极其相似")
    dbinterface.Add_League_Result(9,1,"老一批选手的荣光，随着退役而烟消云散，新人们难以")
    dbinterface.Add_League_Result(10,1,"只能苦苦支撑旧时的颜面。老将们或退役或隐退")

    dbinterface.Add_League_Result(11,1,"SS当年一套四保一冠绝天下，QG无敌的团战")
    dbinterface.Add_League_Result(12,1,"SS当年一套四保一冠绝天下，QG无敌的团战")
    dbinterface.Add_League_Result(13,2,"这些队伍，虽然有诸多可圈可点之处，但是我们可以发现")
    dbinterface.Add_League_Result(14,2,"《炉石传说：魔兽英雄传》是一款由暴雪娱乐开集换式")
    dbinterface.Add_League_Result(15,2,"而玩家要做的，就是根据自己现有的卡牌组建合适的卡组")
    dbinterface.Add_League_Result(16,14,"中国大陆地区的独家运营由网易公司代理。游戏背景设")
    dbinterface.Add_League_Result(17,14,"共九位魔兽中的角色作为九种不同的职业")
    dbinterface.Add_League_Result(18,14,"指挥英雄，驱动随从，施展法术，游戏好友或素不相识")
    dbinterface.Add_League_Result(19,14,"2014年3月13日全球同步正式运营。年获A2014")
    dbinterface.Add_League_Result(20,14,"2015年获第二届SXSW游戏大奖年度移动游戏。")
    
    for i in range(21,200):
        dbinterface.Add_League_Result(i,random.randint(1,50),"暂无暂无暂无暂无暂无暂无暂无")
    
    
#game_competitor  data
def ADD_GAME_COM():
    
    dbinterface.Add_Game_Competitor(1,1,2,0)
    dbinterface.Add_Game_Competitor(2,3,4,0)
    dbinterface.Add_Game_Competitor(3,5,6,0)
    dbinterface.Add_Game_Competitor(4,7,8,0)
    dbinterface.Add_Game_Competitor(5,9,10,0)
    dbinterface.Add_Game_Competitor(6,11,12,0)
    dbinterface.Add_Game_Competitor(7,13,14,0)
    dbinterface.Add_Game_Competitor(8,15,16,0)
    dbinterface.Add_Game_Competitor(9,17,18,0)
    dbinterface.Add_Game_Competitor(10,19,20,0)

    dbinterface.Add_Game_Competitor(11,21,22,0)
    dbinterface.Add_Game_Competitor(12,24,23,0)
    dbinterface.Add_Game_Competitor(13,25,26,0)
    dbinterface.Add_Game_Competitor(14,27,28,0)
    dbinterface.Add_Game_Competitor(15,30,29,0)
    dbinterface.Add_Game_Competitor(16,31,32,0)
    dbinterface.Add_Game_Competitor(17,34,33,0)
    dbinterface.Add_Game_Competitor(18,35,36,0)
    dbinterface.Add_Game_Competitor(19,37,38,0)
    dbinterface.Add_Game_Competitor(20,40,39,0)
    
    for i in range(21,200):
        dbinterface.Add_Game_Competitor(i,random.randint(1,100),random.randint(1,100),random.randint(0,1))
    
    

def add_all_data() :
    dbinterface.init(db,cursor)
    ADD_ESPORT()
    ADD_LEAGUE()
    ADD_GAME()
    ADD_CLUB()
    ADD_TEAM()
    ADD_PLAYER()
    ADD_LEAGUE_RESULT()
    ADD_GAME_COM()
