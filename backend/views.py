from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from backend import dbinterface

# Create your views here.
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if(isinstance(obj, datetime.datetime)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif(isinstance(obj, datetime.date)):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

# ------------------------------- user_info -----------------------------------
# by MinstrelZal
# 2017-12-22

# URL: user/register_login/
@csrf_exempt
def Register_Login(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        username = str(data.get('username'))
        password = str(data.get('password'))
        if(dbinterface.Register_Login(username, password, 1, 0) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: user/logout/
@csrf_exempt
def Logout(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        username = str(data.get('username'))
        if(dbinterface.Logout(username) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: user/add/
@csrf_exempt
def Add_User(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        username = str(data.get('username'))
        password = str(data.get('password'))
        is_staff = int(data.get('is_staff'))
        if(dbinterface.Add_User(username, password, 0, is_staff) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: user/delete/
@csrf_exempt
def Delete_User(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        user_id = int(data.get('id'))
        if(dbinterface.Delete_User(user_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: user/search/
@csrf_exempt
def Search_User(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        username = str(data.get('username'))
        if(username == ''):
            result = dbinterface.User_List()
        else:
            result = dbinterface.Search_User(username)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: user/alter/
@csrf_exempt
def Alter_User(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        user_id = int(data.get('id'))
        username = str(data.get('username'))
        password = str(data.get('password'))
        is_staff = int(data.get('is_staff'))
        if(dbinterface.Alter_User(user_id, username, password, is_staff) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: user/list/
@csrf_exempt
def User_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        username = str(data.get('username'))
        if(username == ''):
            result = dbinterface.User_List()
        else:
            result = dbinterface.Search_User(username)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))


# ---------------------------------- esport_info ---------------------------------------
# by MinstrelZal
# 2017-12-23

# URL: esport/add/
@csrf_exempt
def Add_ESport(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        etype = str(data.get('type'))
        if(dbinterface.Add_ESport(name, etype) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: esport/delete/
@csrf_exempt
def Delete_ESport(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        esport_id = int(data.get('id'))
        if(dbinterface.Delete_ESport(esport_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: esport/search/
@csrf_exempt
def Search_ESport(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.ESport_List()
        else:
            result = dbinterface.Search_ESport(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: esport/alter/
@csrf_exempt
def Alter_ESport(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)	
        esport_id = int(data.get('id'))
        name = str(data.get('name'))
        etype = str(data.get('type'))
        if(dbinterface.Alter_ESport(esport_id, name, etype) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: esport/list/
@csrf_exempt
def ESport_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.ESport_List()
        else:
            result = dbinterface.Search_ESport(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# ------------------------- league_info & league_result ----------------------------
# by MinstrelZal
# 2017-12-23

# URL: league/add/
@csrf_exempt
def Add_League(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        begin_time = str(data.get('begin_time'))
        end_time = str(data.get('end_time'))
        print(data)
        if(dbinterface.Add_League(name, begin_time, end_time) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: league/delete/
@csrf_exempt
def Delete_League(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        league_id = int(data.get('id'))
        if(dbinterface.Delete_League(league_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: league/search/
@csrf_exempt
def Search_League(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.League_List()
        else:
            result = dbinterface.Search_League(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: league/alter/
@csrf_exempt
def Alter_League(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        league_id = int(data.get('id'))
        name = str(data.get('name'))
        begin_time = str(data.get('begin_time'))
        end_time = str(data.get('end_time'))
        if(dbinterface.Alter_League(league_id, name, begin_time, end_time) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: league/list/
@csrf_exempt
def League_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.League_List()
        else:
            result = dbinterface.Search_League(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))


# URL: league/result/add/
@csrf_exempt
def Add_League_Result(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        league_id = int(data.get('league_id'))
        esport_id = int(data.get('esport_id'))
        result = str(data.get('result'))
        if(dbinterface.Add_League_Result(league_id, esport_id, result) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: league/result/delete/
@csrf_exempt
def Delete_League_Result(request):
     if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        league_id = int(data.get('league_id'))
        if(dbinterface.Delete_League_Result(league_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: league/result/search/
@csrf_exempt
def Search_League_Result(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        league_id = str(data.get('league_id'))
        if(league_id == ''):
            result = dbinterface.League_Result_List()
            return HttpResponse(json.dumps(result, cls=ComplexEncoder))
        else:
            league_id = int(league_id)
            result = dbinterface.Search_League_Result(league_id)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        if(result == {}):
            return HttpResponse(json.dumps([], cls=ComplexEncoder))
        return HttpResponse(json.dumps([result], cls=ComplexEncoder))

# URL: league/result/alter/
@csrf_exempt
def Alter_League_Result(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        league_id = int(data.get('league_id'))
        esport_id = int(data.get('esport_id'))
        result = str(data.get('result'))
        if(dbinterface.Alter_League_Result(league_id, esport_id, result) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: league/result/list/
@csrf_exempt
def League_Result_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        result = dbinterface.League_Result_List()
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# ----------------------------- game_info ------------------------------------
# by MinstrelZal
# 2017-12-23

# URL: game/add/
@csrf_exempt
def Add_Game(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        time = str(data.get('time'))
        location = str(data.get('location'))
        league_id = int(data.get('league_id'))
        result = str(data.get('result'))
        if(dbinterface.Add_Game(name, time, location, league_id, result) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: game/delete/
@csrf_exempt
def Delete_Game(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        game_id = int(data.get('id'))
        if(dbinterface.Delete_Game(game_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: game/search/
@csrf_exempt
def Search_Game(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.Game_List()
        else:
            result = dbinterface.Search_Game(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: game/alter/
@csrf_exempt
def Alter_Game(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        game_id = int(data.get('id'))
        name = str(data.get('name'))
        time = str(data.get('time'))
        location = str(data.get('location'))
        league_id = int(data.get('league_id'))
        result = str(data.get('result'))
        if(dbinterface.Alter_Game(game_id, name, time, location, league_id, result) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: game/list/
@csrf_exempt
def Game_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        if(name == ''):
            result = dbinterface.Game_List()
        else:
            result = dbinterface.Search_Game(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# ---------------------------------- club_info  -----------------------------------
# by MinstrelZal
# 2017-12-23

# URL: club/add/
@csrf_exempt
def Add_Club(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        sponsor = str(data.get('sponsor'))
        achievement = str(data.get('achievement'))
        setup_time = str(data.get('setup_time'))
        founder = str(data.get('founder'))
        if(dbinterface.Add_Club(name, sponsor, achievement, setup_time, founder) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: club/delete/
@csrf_exempt
def Delete_Club(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        club_id = int(data.get('id'))
        if(dbinterface.Delete_Club(club_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: club/search/
@csrf_exempt
def Search_Club(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.Club_List()
        else:
            result = dbinterface.Search_Club(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: club/alter/
@csrf_exempt
def Alter_Club(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        club_id = int(data.get('id'))
        name = str(data.get('name'))
        sponsor = str(data.get('sponsor'))
        achievement = str(data.get('achievement'))
        setup_time = str(data.get('setup_time'))
        founder = str(data.get('founder'))
        if(dbinterface.Alter_Club(club_id, name, sponsor, achievement, setup_time, founder) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: club/list/
@csrf_exempt
def Club_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.Club_List()
        else:
            result = dbinterface.Search_Club(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# ------------------------------- team_info -----------------------------------
# by MinstrelZal
# 2017-12-24

# URL: team/add/
@csrf_exempt
def Add_Team(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        coach = str(data.get('coach'))
        achievement = str(data.get('achievement'))
        club_id = int(data.get('club_id'))
        esport_id = int(data.get('esport_id'))
        if(dbinterface.Add_Team(name, coach, achievement, club_id, esport_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: team/delete/
@csrf_exempt
def Delete_Team(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        team_id = int(data.get('id'))
        if(dbinterface.Delete_Team(team_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: team/search/
@csrf_exempt
def Search_Team(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.Team_List()
        else:
            result = dbinterface.Search_Team(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: team/alter/
@csrf_exempt
def Alter_Team(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        team_id = int(data.get('id'))
        name = str(data.get('name'))
        coach = str(data.get('coach'))
        achievement = str(data.get('achievement'))
        club_id = int(data.get('club_id'))
        esport_id = int(data.get('esport_id'))
        if(dbinterface.Alter_Team(team_id, name, coach, achievement, club_id, esport_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: team/list/
@csrf_exempt
def Team_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        name = str(data.get('name'))
        if(name == ''):
            result = dbinterface.Team_List()
        else:
            result = dbinterface.Search_Team(name)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# ----------------------------------- player_info -------------------------------------------
# by MinstrelZal
# 2017-12-24

# URL: player/add/
@csrf_exempt
def Add_Player(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        game_id = str(data.get('game_id'))
        name = str(data.get('name'))
        gender = int(data.get('gender'))
        achievement = str(data.get('achievement'))
        team_id = int(data.get('team_id'))
        if(dbinterface.Add_Player(game_id, name, gender, achievement, team_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: player/delete/
@csrf_exempt
def Delete_Player(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        player_id = int(data.get('id'))
        if(dbinterface.Delete_Player(player_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: player/search/
@csrf_exempt
def Search_Player(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        game_id = str(data.get('game_id'))
        if(game_id == ''):
            result = dbinterface.Player_List()
        else:
            result = dbinterface.Search_Player(game_id)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

# URL: player/alter/
@csrf_exempt
def Alter_Player(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        player_id = int(data.get('id'))
        game_id = str(data.get('game_id'))
        name = str(data.get('name'))
        gender = int(data.get('gender'))
        achievement = str(data.get('achievement'))
        team_id = int(data.get('team_id'))
        if(dbinterface.Alter_Player(player_id, game_id, name, gender, achievement, team_id) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: player/list/
@csrf_exempt
def Player_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        game_id = str(data.get('game_id'))
        if(game_id == ''):
            result = dbinterface.Player_List()
        else:
            result = dbinterface.Search_Player(game_id)
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

