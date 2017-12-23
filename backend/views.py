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
        result = dbinterface.User_List()
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
        etype = int(data.get('etype'))
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
        etype = int(data.get('etype'))
        if(dbinterface.Alter_ESport(esport_id, name, etype) == 1):
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))

# URL: esport/list/
@csrf_exempt
def ESport_List(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        result = dbinterface.ESport_List()
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
        result = dbinterface.League_List()
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
def Game_List():
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        result = dbinterface.Game_List()
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))
