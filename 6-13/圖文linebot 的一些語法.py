# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:23:07 2023

@author: User
"""
#收到訊息
for event in events:
    if isinstance(event, MessageEvent):
        if isinstance(event.mesage, TextMessage):
            
            
#回傳訊息語法
line_bot_api.reply_message(event.reply_token,訊息種類)

#簡單回傳訊息
TextSendMessage(text=文字訊息內容)

#鸚鵡
TextSendMessage(text=event.message.text)

#回傳圖片
ImageSendMessage(original_content_url=原始圖片,priview_image_url=預覽圖片)


#按鈕樣板
樣板變數=TemplateSendMessage(alt_text='不支援樣板時顯示的文字',template=ButtonsTemplate(
             title='標題',
             text='文字內容',
             actions=[
                 第一個按鈕
                 第二個按鈕
                 ........
             ]
                            )
)
line_bot_api.reply_message(event.reply_token, messages=[樣板變數])

#URI按鈕
URIAction(label='按鈕文字',uri='網址')
    
