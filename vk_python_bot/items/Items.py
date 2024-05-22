import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import random
import re
import requests
import json
# from vk_api.longpoll import VkLongPoll, VkEventType


vk_session = vk_api.VkApi(token = 'vk1.a.e1SIlY7nzncfBbX6u7io0S19bWGH-nP-LrRR6fXAMr9z0mkO80Dvlk66smj4RtFea9xoMiR8_-vYl5RxW46TtLBndvzYrNFBAxiyE4C2EYNDMtpIFQtv2HlcUvUPXnyizQj3xHmwXbVZ7lxOh_5gFSnBHSLw4b9jfBihc-mNhhb1SsjpFm2IuiaMjVj26GeXzebdkipbtzjm0sgXhgXOQg')
longpoll = VkBotLongPoll(vk_session, 218279129)

def get_but_mainChar (text, color):
    return{
        "action": { 
        "type": "open_link",
        "link": "https://docs.google.com/document/d/1r4xje5BO2z7aYtYj5sGqfejFWpQNYwrMKnLt5QYWWWs/edit",
        "payload": "{\"button\": \"" + "1" + "\"}",
        "label": f"{text}"
          }
          }

def get_but_agil (text, color):
    return{
        "action": { 
        "type": "open_link",
        "link": "https://docs.google.com/document/d/1Pydesj0y03i6HHBVxwffRWSGZqB-KPv5LtgGs5drI1U/edit",
        "payload": "{\"button\": \"" + "1" + "\"}",
        "label": f"{text}"
          }
          }

def get_but_strenth (text, color):
    return{
        "action": { 
        "type": "open_link",
        "link": "https://docs.google.com/document/d/1Kbp4wBAjdGstSQF6ApINioqaRvbEcGzSp7YNQGLhD3k/edit",
        "payload": "{\"button\": \"" + "1" + "\"}",
        "label": f"{text}"
          }
          }

def get_but_magic (text, color):
    return{
        "action": { 
        "type": "open_link",
        "link": "https://docs.google.com/document/d/1O_OTPJuYt8Y1Baf0yUDnQamFb6ULf0nVJGbuvgyqDy4/edit",
        "payload": "{\"button\": \"" + "1" + "\"}",
        "label": f"{text}"
          }
          }

def get_but_race (text, color):
    return{
        "action": { 
        "type": "open_link",
        "link": "https://docs.google.com/document/d/15BOdFzcZ3i2FRZ0yAfy47MF2h55ZPohT8HmUT-w1j2M/edit",
        "payload": "{\"button\": \"" + "1" + "\"}",
        "label": f"{text}"
          }
          }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but_mainChar('Характеристики', 'positive'), get_but_magic('Магия', 'positive')],
        [get_but_strenth('Воины', 'positive'), get_but_agil('Ловкачи', 'positive')],
        [get_but_race('Играбельные расы', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

def sender (id, text):
    post = {
        'chat_id' : id, 
        'message' : text, 
        'random_id' : 0
        }
    vk_session.method('messages.send', post)

def senderMenu (id, text):
    post = {
        'chat_id' : id, 
        'message' : text, 
        'random_id' : 0,
        'keyboard': keyboard
        }
    
    vk_session.method('messages.send', post)




for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            
            id = event.chat_id
            msg = event.object.message['text'].lower()
            user_id = event.object.message['from_id']

            modifiers = {
               103802965: {'mod_Luda': 0}, 
               326361262: {'mod_Kona': 0},
               318281950: {'mod_Vadim': 0},
               35967942:  {'mod_Nasya': -1},
               71393261:  {'mod_Orteme': 0},
               138379997: {'mod_Gribizzi': -3},
               169099200: {'mod_Aniki': 0},
               49600967:  {'mod_Mikh': 0},
               455017138: {'mod_Ya': 0},
               64032557:  {'mod_Alena': 0},
            }

            usernames = {
               'Людмила Черняева': 103802965, 
               'Kona Ni': 326361262,
               'Вадим Белый': 318281950,
               'Анастасия Гречанникова':  35967942,
               'Артем Ширшов':  71393261,
               'Лиза Морозова': 138379997,
               'Владислав Аникин': 169099200,
               'Михаил Гречанников':  49600967,
               'Хитрая Волынка': 455017138,
               'Алёна Рудина':  64032557,
            }

            with open('modifiers.json', 'w') as file:
                json.dump(modifiers, file)

            mod_Luda = 0
            mod_Kona = 0 
            mod_Vadim = 0
            mod_Nasya = -1
            mod_Orteme = 0
            mod_Gribizzi = -3
            mod_Aniki = 0
            mod_Mikh = 0
            mod_Ya = 0
            mod_Alena = 0

            if id >= 0:
                if msg == '/контрактик':
                    cups = 3
                    sender(id, f'В одном из {cups} cтаканов шарик, угадаешь в каком?')
                    ball_cup = random.randint(1, cups)
                    # Ждем сообщения от пользователя
                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            if event.from_chat:
                                
                                id = event.chat_id
                                msg = event.object.message['text'].lower()
                                user_id = event.object.message['from_id']

                        # Проверяем, является ли текст числом от 1 до cups
                                if msg.isdigit() and 1 <= int(msg) <= cups:
                            # Если номер стакана совпадает с номером стакана, в котором находится шарик
                                    if int(msg) == ball_cup:
                                        sender(id, f'Ха ха ладно ты угадал')
                                        break
                            # Если номер стакана не совпадает с номером стакана, в котором находится шарик
                                    else:
                                        sender(id, f'М-да, а потом такие говорят, что не читали договор! Шарик был в стакане {ball_cup}. Еще разок?')
                                        break
                #гау
                #mod_Luda = 0
                #mod_Kona = 0 
                #mod_Vadim = 0
                #mod_Nasya = -1
                #mod_Orteme = 0
                #mod_Gribizzi = -3
                #mod_Aniki = 0
                #mod_Mikh = 0
                #mod_Ya = 0

                def get_name(from_id):
                    if from_id > 0:
                        info = getting_api.users.get(user_ids=from_id)[0]
                        full_name = info.get('first_name') + ' ' + info['last_name']
                        return full_name
                    else:
                        return "Unknown User"


                getting_api = vk_session.get_api()

                name = get_name(event.object.message['from_id'])


                if msg == "/мой айди":
                    sender(id, f'@id{user_id} - ваш айди')

                if msg == "/модификатор":
                    if user_id in modifiers:
                        mod_dict = modifiers[user_id]
                        mod_value = list(mod_dict.values())[0]
                        sender(id, f'@id{user_id} - модификатор действий равен {mod_value}')
                    else:
                        sender(id, f'@id{user_id} - у вас нет модификатора')


                if msg == '/меню' and user_id == 455017138:
                    senderMenu(id, f'@id{user_id} Меню обновлено')

                pattern = r'/(\d+)?к(\d+)([+\-]\d+)?'

                print (mod_Kona)
                        


                if pattern == r'/(\d+)?к(\d+)([+\-]\d+)?':

                # разбираем строку с помощью регулярных выражений
                    pattern = r'/(\d+)?к(\d+)([+\-]\d+)?'
                    match = re.match(pattern, msg)

                    if match:
                # извлекаем количество кубиков, количество граней и модификатор из регулярного выражения
                        num_dice = int(match.group(1) or 1)
                        num_sides = int(match.group(2))
                        modifier1 = int(match.group(3) or 0)

                # бросаем кубики и считаем сумму
                        #total = sum([random.randint(1, num_sides) for _ in range(num_dice)])
                        totals = [random.randint(1, num_sides) for _ in range(num_dice)]
                        result2 = ''
                        for total in totals:
                            result2 += str(total) + "+"
                        result = sum(totals)

                        if user_id in modifiers:
                            mod_dict = modifiers[user_id]
                            mod_value = list(mod_dict.values())[0]
                            preResult = int(modifier1) + int(mod_value)
                            result += preResult
                            if mod_value == 0:
                                sender(id, f'{name} - Результат: {result} ({result2}{preResult})')
                            elif mod_value < 0:
                                sender(id, f'{name} - Результат: {result} ({result2}{preResult}). \n Вы ранены, штраф: {mod_value}')
                            elif mod_value > 0: 
                                sender(id, f'{name} - Результат: {result} ({result2}{preResult}). \n Вы усилены на: {mod_value} ')                    
                    else:
                        print("Ошибка: неправильный формат описания броска.")

                    




