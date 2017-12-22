from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
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

