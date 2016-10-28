from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login(request):
    return HttpResponse(u"login success")


def regist(request):
    return HttpResponse(u"regist success")


def updateTime(request):
    return HttpResponse(u"update success")

@csrf_exempt
def testPost(request):
    test = request.POST.get('test','')
    return HttpResponse(test)