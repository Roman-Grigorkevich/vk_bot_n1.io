# -*- coding: utf-8 -*-
# скрипт был создан Создан Р. Григоркевичем +++
import vk_api
import time
import random
from logic import*

token = 'db092bba9f025e26f7e4dace072ac184f26e8a3316a56788c93b8ddde8cc0aff2d38ca7dd0b703c00d74b'

vk = vk_api.VkApi(token=token)

def readNsend(user, bot):
    ret=False
    if body.lower() == user:
        vk.method("messages.send", {"peer_id": id, "message": bot})
        ret=True
    return ret

def subsTo(text,to):
    i=0; a='0'
    while i<len(text):
        if to==text[i]:
            a=i
            i=len(text)
            break
        else:
            i+=1
    if a=='0':
        a=2
    return a

def checkSymb(text,symbol):
    a=False
    for i in text:
        if i==symbol:
            a=True
    return a

# Srart

vk._auth_token()
print("Start")

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if readNsend("?","Я зашифрую твои сообщения. "+
             "Напиши мне 'текст;ключ', и я отправлю тебе, твоё сообщение, но уже зашифрованное. "+
             "Что бы расшифровать мой код напиши мне 'текст;-ключ'"):{}
            elif readNsend("?правила","Я понимаю как кириллицу  так и латиницу, "+
                "а также цифры и некоторые знаки."):{}
            else:
                print('+')
                user_s=body.lower()
                _key=random.randint(4,40)
                hk=True
                answer=user_s
                if checkSymb(user_s,';'):
                    _key=subsTo(user_s,';')
                    answer=user_s[0:_key]
                    _key=int(user_s[_key+1:len(user_s)])
                    hk=False
                vk.method("messages.send", {"peer_id": id, "message": coding(answer,_key)})
                if hk:
                    vk.method("messages.send", {"peer_id": id, "message": "🔑:"+str(_key)})

    except Exception as E:
        time.sleep(1)
