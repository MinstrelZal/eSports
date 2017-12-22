from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from .forms import *
import dbinterface

# Create your views here.
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if(isinstance(obj, datetime.datetime)):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif(isinstance(obj, datetime.date)):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

@csrf_exempt
def User_Register(request):
    if(request.method == 'POST'):
        data = json.dumps(request.POST)
        data = json.loads(data)
        username = str(data.get('username'))
        password1 = str(data.get('password1'))
        password2 = str(data.get('password2'))
        
        registerform = Register_Form({'username':username, 'password1':password1, 'password2':password2})
        if(registerform.is_valid()):
            sql = 'INSERT INTO user_info (username, password) VALUES ("%s", "%s");' % (username, password1)
            try:
                dbinterface.cursor.execute(sql)
                dbinterface.db.commit()
            except:
                dbinterface.db.rollback()
                print('backend/views.py    Error: Unable to insert into user_info')
                return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
            return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))
        else:
            print('backend/views.py    Error: Register_Form is not valid')
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))

@csrf_exempt
def Login(request):
    if(request.method == 'POST'):
        data = json.dumps(data)
        data = json.loads(data)
        username = str(data.get('username'))
        password = str(data.get('password'))
        sql = 'SELECT password FROM user_info WHERE username=%s;' % (username)
        try:
            dbinterface.cursor.execute(sql)
            result = dbinterface.cursor.fetchall()
        except:
            print('backend/views.py    Error: Unable to select from user_info')
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        if(len(result) != 1):
                print('backend/views.py    Error: username error')
                return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        if(result[0][0] == password):
            sql = 'UPDATE user_info SET is_loggedin=1 WHERE username=%s' % (username)
            try:
                dbinterface.cursor.execute(sql)
                dbinterface.db.commit()
            except:
                print('backend/views.py    Error: Unable to update user_info')
                return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
            return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))
        print('backend/views.py    Error: password error')
        return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))

@csrf_exempt
def Logout(request):
    if(request.method == 'POST'):
        data = json.dumps(data)
        data = json.loads(data)
        sql = 'UPDATE user_info SET is_loggedin=0 WHERE username=%s' % (username)
        try:
            dbinterface.cursor.execute(sql)
            dbinterface.db.commit()
        except:
            print('backend/views.py    Error: Unable to update user_info')
            return HttpResponse(json.dumps({'error': 1}, cls=ComplexEncoder))
        return HttpResponse(json.dumps({'error': 0}, cls=ComplexEncoder))
