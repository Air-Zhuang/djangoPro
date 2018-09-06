# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json

# Create your views here.
def Login(request):
    if request.method=='POST':
        result ={}
        username=request.POST.get('username')
        password=request.POST.get('password')
        result['user']=username
        result['pwd']=password
        result = json.dumps(result)
        return HttpResponse(result, content_type='application/json;charset=utf-8')
    else:
        return render_to_response('login.html')

def Login2(request):
    if request.method=='GET':
        result={}
        username=request.GET.get('username')
        mobile= request.GET.get('mobile')
        data=request.GET.get('data')
        result['user']=username
        result['mobileNum']=mobile
        result['data']=data
        result=json.dumps(result)
        return HttpResponse(result,content_type='application/json;charset=utf-8')