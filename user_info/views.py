# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import json
import simplejson
# Create your views here.
from user_info.models import UserInfo


@csrf_exempt
def login(request):
    return HttpResponse(u"login success")

@csrf_exempt
def regist(request):
    userName = request.POST.get('user_name', '')
    password = request.POST.get('password', '')
    ##查找是否user_name已存在
    isNameExist = UserInfo.objects.filter(user_name=userName)
    if len(isNameExist) == 0 :
        userInfo = UserInfo(user_name=userName, password=password)
        userInfo.save()
        return HttpResponse(u"regist success")
    else:
        return HttpResponse(u"name exist!!")


def updateTime(request):
    return HttpResponse(u"update success")


@csrf_exempt
def testPost(request):
    test = request.POST.get('test', '')
    # return JsonResponse({"key": test})
    return HttpResponse(json.dumps(test))


@csrf_exempt
def getUserInfo(request):
    name = request.POST.get('user_name', '')
    data1 = UserInfos.objects.filter(user_name=name)
    data2 = serializers.serialize("json", UserInfos.objects.filter(user_name=name))
    data3 = simplejson.dumps([{'user_name': o.user_name,
                               'last_time': o.last_time} for o in data2])
    return HttpResponse(data3)
