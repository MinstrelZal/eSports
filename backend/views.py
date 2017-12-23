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
        result = dbinterface.User_List()
        if(type(result) == int):
            return HttpResponse(json.dumps([{'error': 1}], cls=ComplexEncoder))
        return HttpResponse(json.dumps(result, cls=ComplexEncoder))

