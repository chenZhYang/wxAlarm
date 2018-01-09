#!/usr/bin/env python
# coding=utf-8
from django.shortcuts import render
import json
import itchat,sys,time
from datetime import datetime
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse


# 默认开启了csrf保护机制，本服务仅作自测使用，加上csrf_exempt去除掉csrf保护
@csrf_exempt
def sendMsg(request):
    print('get into sendMsg')
    print(request.GET)
    print(request.body)
    print(request.POST)
    print(json.dumps(request.GET))
    json_str = json.dumps(request.GET)
    json_to_python = json.loads(json_str)
    SentChatRoomsMsg(json_to_python['name'], json_to_python['context'])
    return HttpResponse('OK')
@csrf_exempt
def sendMsgPost(request):
    if 'POST' == request.method:
        print('get into sendMsgPost')
        #print(json.loads(request.POST))
        print(request.body)
        print(json.loads(request.body))
        #json_str = json.dumps(request.body)
        json_to_python = json.loads(request.body)
        SentChatRoomsMsg(json_to_python['name'], json_to_python['context'])
    return HttpResponse('OK')

def login(request):
    itchat.auto_login(hotReload=2)
    itchat.run()
    return

def SentChatRoomsMsg(name,context):
    itchat.get_chatrooms(update=True)
    iRoom = itchat.search_chatrooms(name)
    for room in iRoom:
        if room['NickName'] == name:
            userName = room['UserName']
            break
    itchat.send_msg(context, userName)
    print("发送时间：" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
                                                                   "发送到：" + name + "\n"
                                                                                   "发送内容：" + context + "\n")
    print("*********************************************************************************")

def index(request):
    return render(request, "alarm/index.html")