#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:37:45 2023

@author: wuichen
"""

from flask import Flask
app=Flask(__name__)

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


        access_token = 'cqH9zl1U4aUP6ox6X7k7Z2w7BlNz1gUCyZGu011B9XzPKTKzgWJtUuv0oBGxZEAgYUATj8muZXAk3pK1AsX8osFSW40TUQeYRJC2pLcCQ3E1N0pJylgaH0+lxbQ0nTfhUG+PSHcbv 7fO2bN1jTGGdQdB04t89/1O/w1cDnyilFU='
        secret = '975d7ee2febbf4c0868c40931455bbf2'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'ok'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token, 
        TextSendMessage(text=event.message.text))
    
if __name__ == '__main__':
    app.run()
    
