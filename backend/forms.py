from django import forms
import re
from backend import dbinterface

class Register_Form(forms.Form):
    username = forms.CharField(required=True, max_length=30)
    password1 = forms.CharField(required=True, max_length=30)
    password2 = forms.CharField(required=True, max_length=30)

    def clean_username(self):
        username = str(self.cleaned_data['username'])
        if(len(username) < 1 or len(username) > 30):
            raise forms.ValidationError('用户名长度必须为30位以内')
        sql = "SELECT id FROM user_info WHERE username=%s;" % (username)
        try:
            dbinterface.cursor.execute(sql)
            if(dbinterface.cursor.rowcount > 0):
                raise forms.ValidationError('用户名已被注册')
        except:
            print('backend/dbinterface.py    Error: Unable to select from user_info')
        return username
    
    def clean_password1(self):
        password1 = str(self.cleaned_data['password1'])
        if(len(password1) < 8 or len(password1) > 30):
            raise forms.ValidationError('密码长度必须为8-30位')
        return password1

    def clean_password2(self):
        password2 = str(self.cleaned_data['password2'])
        password1 = str(self.cleaned_data['password1'])
        if(password2 != password1):
            raise forms.ValidationError('两次输入的密码不一致')
        return password2
