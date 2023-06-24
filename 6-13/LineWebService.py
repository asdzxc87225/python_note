#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 09:52:42 2023

@author: wuichen
"""

#引用Flask
from flask import Flask #Flask類別
from flask import request
#變成前端進行送訊息回Line Bot程序 引用 Http Client
import requests
#建構一個Flask類別個體物件(Instance)
app=Flask(__name__) #__name__取出__main__字串

#-----------撰寫Conroller-Action----------------------
#Line WebHook 規範的服務 Request Method:POST
#無需回應值
@app.route('/linebot',methods=['POST'])
def lineService():
    #透過local request proxy 獲取傳遞資訊???
    weekData=request.get_json()#dict物件
    eventList=weekData['events']#List物件
    evetData=eventList[0]#dict物件
    userId=evetData['source']['userId']#前端使用者識別（系統編號）
    if evetData['message']['type']=='text':
        #才取聊天內容
        message=evetData['message']['text']#取得聊天內容
        #整理鸚鵡回應話
        content=f'我是鸚鵡機器人，你:{userId} 說的是：{message}'
        #透過Line Bot send push message API 進行回應到使用者 先借助line bot 在推到使用者端
        #要設定http header:Content-Type:application/json  及 Authorization: Bearer {channel access token}
        myHeader={'Content-Type':'application/json','Authorization':'Bearer 6VBw56Nqe1F7z09NXdXiZSsFMqt1QTACeuuXiG6ypzmYbHUR31jh1ckQeKGSIZdBS8bCNmDMiG2CZ9vhVpTUm/ugg/ejKWtlsbmzPFgPsOEmFond1snkIAT/WDhOvLJPNrmlw++uisQdIMO6HQf/IgdB04t89/1O/w1cDnyilFU='}
        requests.post('https://api.line.me/v2/bot/message/push',headers=myHeader,data='{"to":"'+userId+'","messages":[{"type":"text","text":"'+content+'"}]}')
        print(content)
        return content
    

#設定Entry Point 主程式 starter啟動網站系統
if __name__=='__main__':
    #啟動網站伺服器
    app.run('localhost',5000) #TCP/IP Port 有些被預設使用 80(正式網站)
    
