import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import random
import re
import json
from Lists import Lists
from Lists import sqlite
import sqlite3 as sq
from items import variables
# from vk_api.longpoll import VkLongPoll, VkEventType

#ввести свои токен и группу
vk_session = vk_api.VkApi(token = '') 
longpoll = VkBotLongPoll(vk_session, )


with sq.connect("Characters.db") as con:
    cur = con.cursor()

def calculate_skill_result(user_id, skill_name, attribute_func, skill_func): #бросок кубов 
    num_dices = 3
    num_sides = 6
    totals = [random.randint(1, num_sides) for _ in range(num_dices)]
    result2 = '+'.join(str(total) for total in totals)
    result = sum(totals)

    preResultAtribAndSkill = attribute_func(user_id) + skill_func(user_id)
    result += attribute_func(user_id) + skill_func(user_id) + int(variables.s_get_modifier(user_id))
    sender(id, f'{name} - Результат: {result} ({result2}+{preResultAtribAndSkill}). \n Модификатор: {variables.s_get_modifier(user_id)}')

def calculate_skill_autoresult(character_name, skill_modifires): #сумма атрибута и навыка которые выше 
    num_dices = 3
    num_sides = 6
    totals = [random.randint(1, num_sides) for _ in range(num_dices)]
    result2 = '+'.join(str(total) for total in totals)
    result = sum(totals)

    result += skill_modifires + int(variables.s_get_automodifier(character_name))
    print(f'{name} - Результат: {result} ({result2}+{skill_modifires}). \n Модификатор: {variables.s_get_automodifier(character_name)}')
    return result

#клавиатура со ссылками
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

def get_but_badim (text, color):
    return{
        "action": { 
        "type": "open_link",
        "link": "https://docs.google.com/document/d/17-kjdewuhSiAvZMnZwvGXY3uaLTmWKZQi0jMVMAxiFg/edit",
        "payload": "{\"button\": \"" + "1" + "\"}",
        "label": f"{text}"
          }
          }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but_mainChar('Характеристики', 'positive'), get_but_magic('Магия', 'positive')],
        [get_but_strenth('Воины', 'positive'), get_but_agil('Ловкачи', 'positive')],
        [get_but_race('Играбельные расы', 'positive'), get_but_badim ('Бадим', 'positive')]
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




for event in longpoll.listen(): #слушаем сообщения чата
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            
            id = event.chat_id
            msg = event.object.message['text'].lower()
            user_id = event.object.message['from_id']

            Lists.modifiers
            Lists.usernames

            if id >= 0: #проверка что айди принадлежит участнику чата, а не другому боту
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

                if msg == "привет, голубь":
                    sender(id, f'Привет, {name}!')

                if msg == "/модификатор":
                    if user_id in Lists.modifiers:
                        mod_dict = Lists.modifiers[user_id]
                        mod_value = list(mod_dict.values())[0]
                        sender(id, f'@id{user_id} - модификатор действий равен {mod_value}')
                    else:
                        sender(id, f'@id{user_id} - у вас нет модификатора')


                if msg == '/меню' and user_id == 455017138:
                    senderMenu(id, f'@id{user_id} Меню обновлено')

                pattern = r'/(\d+)?к(\d+)([+\-]\d+)?' #паттерн броска кубов
                patternGiveItems = r"/([\w\s]+) (\d+)?" #паттерн для получения предметов

                if msg == 'голубь кто я':
                    random_adjective = random.choice(Lists.adjectives)
                    random_noun = random.choice(Lists.nouns)
                    sender(id, f'{name} Вы - {random_adjective} {random_noun}')
                if msg == 'новосибирск':
                    sender('НО ВО СИ БИР СК')


############ВЫДАЧА ПРЕДМЕТОВ####################

                if patternGiveItems == r"/([\w\s]+) (\d+)?": #and user_id == 455017138: получаем итемы
                    match = re.match(patternGiveItems, msg)
                    if match:
                        dontneed = match.group(1)
                        num_items = match.group(2)
                        if dontneed == "предметы":
                            if int(num_items) > len(Lists.items):
                                num_items = len(Lists.items)
                            random_items = random.sample(list(Lists.items.values()), int(num_items))
                            message = "Предметы:\n"
                            for item in random_items:
                                message += "- " + item + "\n"
                            sender(id, message)
                            
                    else:
                        print('не тот бросок')

############ Автобой, разработка в процессе ####################
                sentence = "Это предложение будет разбито на группы слов"           
                def generate_pattern():
                    # Паттерн для поиска групп слов
                    return r'\b\w+\b'

                def split_sentence(sentence):
                    # Получаем паттерн
                    pattern = generate_pattern()
                    # Разбиваем предложение по паттерну
                    result = re.findall(pattern, sentence)
                    return result
                
                
                    # Пример использования
                if msg == "команда игроков" and user_id == 455017138:
                    sender(id, f'Напишите имена команды игроков без использования знаков препинания')
                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            if event.from_chat:
                                
                                id = event.chat_id
                                players_team = event.object.message['text'].lower()
                                user_id = event.object.message['from_id']

                                result_players_team = split_sentence(players_team)
                                print(result_players_team)
                                break

                if msg == "команда врагов" and user_id == 455017138:
                    sender(id, f'Напишите имена команды врагов без использования знаков препинания')
                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            if event.from_chat:
                                
                                id = event.chat_id
                                enemies_team = event.object.message['text'].lower()
                                user_id = event.object.message['from_id']

                                result_enemies_team = split_sentence(enemies_team)
                                print(result_enemies_team)
                                break

                if msg == "/следующий":
                    variables.shift_list_left(result_players_team)
                    sender(id, f'{result_players_team}')

                #if msg == "/ставка команда 1":
                    

                if msg == "автобой":

                    while not result_players_team or result_enemies_team: #проверяем есть ли в листе что-то
                        enemy_name = result_enemies_team[0]
                        player_name = result_players_team[0]

                        enemy_strenght_attack_check = variables.m_get_autostrength(enemy_name) + variables.s_get_melee_autocombat(enemy_name)
                        enemy_strenght_defence_check = variables.m_get_autostrength(enemy_name) + variables.s_get_autoblocking(enemy_name)
                        enemy_agile_attack_check = variables.s_get_autofencing(enemy_name) + variables.m_get_autoagile(enemy_name)
                        enemy_agile_dodge_check = variables.m_get_autoagile(enemy_name) + variables.s_get_autododging(enemy_name)

                        player_strenght_attack_check = variables.m_get_autostrength(player_name) + variables.s_get_melee_autocombat(player_name)
                        player_strenght_defence_check = variables.m_get_autostrength(player_name) + variables.s_get_autoblocking(player_name)
                        player_agile_attack_check = variables.s_get_autofencing(player_name) + variables.m_get_autoagile(player_name)
                        player_agile_dodge_check = variables.m_get_autoagile(player_name) + variables.s_get_autododging(player_name)

                        player_attack_strenght = variables.m_get_attack_damage(player_name)
                        player_attack_speed = variables.m_get_attack_speed(player_name)

                        enemy_attack_strenght = variables.m_get_attack_damage(enemy_name)
                        enemy_attack_speed = variables.m_get_attack_speed(enemy_name)
                        #enemy_attack_check
                        #enemy_defence_check
                        #player_attack_check
                        #player_defence_check
                        #чекаем что у врага выше и берем это как модификатор
                        if enemy_strenght_attack_check > enemy_agile_attack_check:
                            enemy_attack_check = enemy_strenght_attack_check
                        else:
                            enemy_attack_check = enemy_agile_attack_check

                        if enemy_strenght_defence_check > enemy_agile_dodge_check:
                            enemy_defence_check = enemy_strenght_defence_check
                        else: 
                            enemy_defence_check = enemy_agile_dodge_check

                        #чекаем что у игрока выше и берем это как модификатор
                            
                        if player_strenght_attack_check > player_agile_attack_check:
                            player_attack_check = player_strenght_attack_check
                        else:
                            player_attack_check = player_agile_attack_check
                            
                        if player_strenght_defence_check > player_agile_dodge_check:
                            player_defence_check = player_strenght_defence_check
                        else: 
                            player_defence_check = player_agile_dodge_check

                        while variables.m_get_autohp(player_name) > 0 and variables.m_get_autohp(enemy_name) > 0: #чекаем хп

                            player_reaction = variables.s_get_autoreaction (player_name) + variables.m_get_autoperception(player_name)
                            enemy_reaction = variables.s_get_autoreaction (enemy_name) + variables.m_get_autoperception(enemy_name)

                            player_reaction_result = calculate_skill_autoresult(player_name, player_reaction)
                            enemy_reaction_result = calculate_skill_autoresult(enemy_name, enemy_reaction)

                            if player_reaction_result > enemy_reaction_result: 
                                for i in range (player_attack_speed): #атака игрока исходя из его количества действий КОЛИЧЕСТВО ДЕЙСТВИЙ ОТСЧИТЫВАЕСЯ С НУЛЯ В БД СТАВИТЬ НА 1 ЕД МЕНЬШЕ

                                    player_result = calculate_skill_autoresult(player_name, player_attack_check)
                                    enemy_result = calculate_skill_autoresult(enemy_name, enemy_defence_check)

                                    print ("сходил игрок, чек реакции:", {player_reaction_result}, {enemy_reaction_result})

                                    if player_result > enemy_result: ### если попал то выполняется логика нанесения урона и предварительного высчитывания статов
                                        enemy_hp = variables.m_get_autohp(enemy_name)
                                        player_dmg = variables.m_get_attack_damage(player_name)
                                        enemy_armor_flat = variables.m_get_autoarmor_flat(enemy_name) 

                                        if variables.m_get_autoarmor_current(enemy_name) > 0: ############ посчитать армор куррент НЕ ЗАБЫТЬ СДЕЛАТЬ КРИТ
                                            enemy_armor_current = variables.m_get_autoarmor_current(enemy_name) #берем армор из бд
                                            enemy_armor_current -= player_dmg #снижаем прочность
                                            player_dmg -= enemy_armor_flat #снижаем урон на количество брони
                                            
                                            if player_dmg < 0: 
                                                player_dmg = 0
                                            enemy_hp -= player_dmg
                                            variables.m_update_autohp(enemy_name, enemy_hp) #переписываем хп врага при наличии армора
                                            variables.m_update_auto_current_armor(enemy_name, enemy_armor_current) #переписываем армор врага
                                        else:
                                            enemy_hp -= player_dmg
                                            variables.m_update_autohp(enemy_name, enemy_hp) #переписываем хп врага если у него нет армора

                                for i in range (enemy_attack_speed):

                                    player_result = calculate_skill_autoresult(player_name, player_attack_check)
                                    enemy_result = calculate_skill_autoresult(enemy_name, enemy_defence_check)

                                    print ("сходил враг, чек реакции:", {enemy_reaction_result}, {player_reaction_result})

                                    if player_result < enemy_result: ### если попал то выполняется логика нанесения урона и предварительного высчитывания статов
                                        player_hp = variables.m_get_autohp(player_name)
                                        enemy_dmg = variables.m_get_attack_damage(enemy_name)
                                        player_armor_flat = variables.m_get_autoarmor_flat(player_name) 

                                        if variables.m_get_autoarmor_current(player_name) > 0: ############ посчитать армор куррент НЕ ЗАБЫТЬ СДЕЛАТЬ КРИТ
                                            player_armor_current = variables.m_get_autoarmor_current(player_name) #берем армор из бд
                                            player_armor_current -= enemy_dmg #снижаем прочность
                                            enemy_dmg -= player_armor_flat #снижаем урон на количество брони
                                            
                                            if enemy_dmg < 0: 
                                                enemy_dmg = 0
                                            player_hp -= enemy_dmg
                                            variables.m_update_autohp(player_name, player_hp) #переписываем хп врага при наличии армора
                                            variables.m_update_auto_current_armor(player_name, player_armor_current) #переписываем армор врага
                                        else:
                                            player_hp -= enemy_dmg
                                            variables.m_update_autohp(player_name, player_hp) #переписываем хп врага если у него нет армора
                            else:
                                for i in range (enemy_attack_speed):

                                    player_result = calculate_skill_autoresult(player_name, player_attack_check)
                                    enemy_result = calculate_skill_autoresult(enemy_name, enemy_defence_check)

                                    print ("сходил враг, чек реакции:", {enemy_reaction_result}, {player_reaction_result})

                                    if player_result < enemy_result: ### если попал то выполняется логика нанесения урона и предварительного высчитывания статов
                                        player_hp = variables.m_get_autohp(player_name)
                                        enemy_dmg = variables.m_get_attack_damage(enemy_name)
                                        player_armor_flat = variables.m_get_autoarmor_flat(player_name) 

                                        if variables.m_get_autoarmor_current(player_name) > 0: ############ посчитать армор куррент НЕ ЗАБЫТЬ СДЕЛАТЬ КРИТ
                                            player_armor_current = variables.m_get_autoarmor_current(player_name) #берем армор из бд
                                            player_armor_current -= enemy_dmg #снижаем прочность
                                            enemy_dmg -= player_armor_flat #снижаем урон на количество брони
                                            
                                            if enemy_dmg < 0: 
                                                enemy_dmg = 0
                                            player_hp -= enemy_dmg
                                            variables.m_update_autohp(player_name, player_hp) #переписываем хп врага при наличии армора
                                            variables.m_update_auto_current_armor(player_name, player_armor_current) #переписываем армор врага
                                        else:
                                            player_hp -= enemy_dmg
                                            variables.m_update_autohp(player_name, player_hp) #переписываем хп врага если у него нет армора

                                for i in range (player_attack_speed): #атака игрока исходя из его количества действий КОЛИЧЕСТВО ДЕЙСТВИЙ ОТСЧИТЫВАЕСЯ С НУЛЯ В БД СТАВИТЬ НА 1 ЕД МЕНЬШЕ

                                    player_result = calculate_skill_autoresult(player_name, player_attack_check)
                                    enemy_result = calculate_skill_autoresult(enemy_name, enemy_defence_check)

                                    print ("сходил игрок, чек реакции:", {player_reaction_result}, {enemy_reaction_result})

                                    if player_result > enemy_result: ### если попал то выполняется логика нанесения урона и предварительного высчитывания статов
                                        enemy_hp = variables.m_get_autohp(enemy_name)
                                        player_dmg = variables.m_get_attack_damage(player_name)
                                        enemy_armor_flat = variables.m_get_autoarmor_flat(enemy_name) 

                                        if variables.m_get_autoarmor_current(enemy_name) > 0: ############ посчитать армор куррент НЕ ЗАБЫТЬ СДЕЛАТЬ КРИТ
                                            enemy_armor_current = variables.m_get_autoarmor_current(enemy_name) #берем армор из бд
                                            enemy_armor_current -= player_dmg #снижаем прочность
                                            player_dmg -= enemy_armor_flat #снижаем урон на количество брони
                                            
                                            if player_dmg < 0: 
                                                player_dmg = 0
                                            enemy_hp -= player_dmg
                                            variables.m_update_autohp(enemy_name, enemy_hp) #переписываем хп врага при наличии армора
                                            variables.m_update_auto_current_armor(enemy_name, enemy_armor_current) #переписываем армор врага
                                        else:
                                            enemy_hp -= player_dmg
                                            variables.m_update_autohp(enemy_name, enemy_hp) #переписываем хп врага если у него нет армора
                        else:
                            if variables.m_get_autohp(player_name) > 0:
                                print ("победил игрок!", "Осталось хп: ", {variables.m_get_autohp(player_name)}, ", осталось брони: ", {variables.m_get_autoarmor_current(player_name)})
                                sender(id, f'Победил игрок! Осталось хп: {variables.m_get_autohp(player_name)}, осталось брони: {variables.m_get_autoarmor_current(player_name)}')
                                break
                            else: 
                                print ("победил враг!", "Осталось хп: ", {variables.m_get_autohp(enemy_name)}, ", осталось брони: ", {variables.m_get_autoarmor_current(enemy_name)})
                                sender(id, f'Победил враг! Осталось хп: {variables.m_get_autohp(enemy_name)}, осталось брони: {variables.m_get_autoarmor_current(enemy_name)}')
                                break

                    else:
                        break

             
                    
############ЧЕКИ КУБОВ####################
                if pattern == r'/(\d+)?к(\d+)([+\-]\d+)?':

                # разбираем строку с помощью регулярных выражений
                    pattern = r'/(\d+)?к(\d+)([+\-]\d+)?'
                    match = re.match(pattern, msg)

                    if match:
                # кубики, грани и модификатор
                        num_dice = int(match.group(1) or 1)
                        num_sides = int(match.group(2))
                        modifier1 = int(match.group(3) or 0)
                    

                # бросаем кубики и считаем сумму
                        totals = [random.randint(1, num_sides) for _ in range(num_dice)]
                        result2 = ''
                        for total in totals:
                            result2 += str(total) + "+"
                        result = sum(totals)

                        if user_id in Lists.modifiers:
                            mod_dict = Lists.modifiers[user_id]
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
########################Подсказки############################
                if msg == "/помоги" or msg == "/помощь" or msg == "/подсказка":
                    sender(id, f'{name} - Команды: \n 1. Взять персонажа: /взять (имя персонажа) \n 2. Положить персонажа: /положить (имя персонажа) \n 3. Узнать кто взят: /персонаж \n Перед игрой необходимо сначала положить персонажа (если нужен другой), а затем уже взять нового \n Персонажи названы по именам')

########################взять персонажа############################
                patternTakeCharacter = r"/([\w\s]+) ([\w\s]+)"
                if patternTakeCharacter == r"/([\w\s]+) ([\w\s]+)":
                    match = re.match(patternTakeCharacter, msg)
                    if match:
                        taking = match.group(1)
                        char_name = match.group(2)
                        if taking == "взять":
                            db_file = 'Characters.db'  
                            search_term = char_name  
                            new_id = user_id  
                            variables.update_id(db_file, search_term, new_id)
                            sender(id, f'{name} - Взят персонаж: {variables.find_character(user_id)}')

########################положить персонажа############################
                patternDropCharacter = r"/([\w\s]+) ([\w\s]+)"
                if patternTakeCharacter == r"/([\w\s]+) ([\w\s]+)":
                    match = re.match(patternDropCharacter, msg)
                    if match:
                        droping = match.group(1)
                        char_name = match.group(2)
                        if taking == "положить":
                            db_file = 'Characters.db'  # Замените на имя вашей базы данных
                            search_term = char_name  # Замените на значение, которое нужно найти
                            new_id = 1  # Замените на новое значение айди
                            variables.update_id(db_file, search_term, new_id)

########################кто взят############################
                patternFindCharacter = r"/([\w\s]+)"
                if patternFindCharacter == r"/([\w\s]+)":
                    match = re.match(patternFindCharacter, msg)
                    if match:
                        finding = match.group(1)
                        if finding == "персонаж":
                            response_message = f'{name} - Взят персонаж: {variables.find_character(user_id)}\n'
                            try:
                                character_data = variables.get_character_stats(user_id)
                                for character in character_data:
                                    print("Character data:")
                                    for column, value in character.items():
                                        response_message += f"{column}: {value}\n"
                            except Exception as e:
                                print(f"An error occurred: {e}")
                            print(f'{variables.find_character(user_id)}')
                            sender(id, response_message)

            try:
########################ближний бой############################
                if msg in ["/бли", "/ближнийбой", "/ближний"]:
                    calculate_skill_result(user_id, "БлижнийБой", variables.m_get_strength, variables.s_get_melee_combat)
                
########################тяжелая стрельба############################
                if msg in ["/тстр", "/тстрельба", "/тяжстр"]:
                    calculate_skill_result(user_id, "ТяжелаяСтрельба", variables.m_get_strength, variables.s_get_heavyshoot)
                
########################Тяжелая атлетика############################
                if msg in ["/та", "/тяж", "/тяжелаяатлетика"]:
                    calculate_skill_result(user_id, "ТяжелаяАтлетика", variables.m_get_strength, variables.s_get_weightlifting)

########################Рукопашный бой############################
                if msg in ["/рук", "/рукопашный", "/рукопашныйбой"]:
                    calculate_skill_result(user_id, "РукопашныйБой", variables.m_get_strength, variables.s_get_hand_combat)

########################Блокирование############################
                if msg in ["/блок", "/бло", "/блокирование", "/парирование"]:
                    calculate_skill_result(user_id, "Блокирование", variables.m_get_strength, variables.s_get_blocking)

########################Легкая атлетика############################
                if msg in ["/ла", "/лег", "/легкаяатлетика"]:
                    calculate_skill_result(user_id, "ЛегкаяАтлетика", variables.m_get_agile, variables.s_get_athletics)

########################Вщлом Замков############################
                if msg in ["/взлом", "/взл", "/отмычка"]:
                    calculate_skill_result(user_id, "ВзломЗамков", variables.m_get_agile, variables.s_get_picklocking)

########################Уклонение############################
                if msg in ["/уклон", "/укл", "/уклонение"]:
                    calculate_skill_result(user_id, "Уклонение", variables.m_get_agile, variables.s_get_dodging)

########################Фехтование############################
                if msg in ["/фехт", "/фех", "/фехтование"]:
                    calculate_skill_result(user_id, "Фехтование", variables.m_get_agile, variables.s_get_fencing)

########################Маскировка############################
                if msg in ["/маск", "/мас", "/маскировка"]:
                    calculate_skill_result(user_id, "Маскировка", variables.m_get_agile, variables.s_get_crouching)

########################Стрельба############################
                if msg in ["/стр", "/стрельба", "/лук"]:
                    calculate_skill_result(user_id, "Стрельба", variables.m_get_agile, variables.s_get_shooting)

########################Метание############################
                if msg in ["/мет", "/метание", "/кидание", "/кинуть"]:
                    calculate_skill_result(user_id, "Метание", variables.m_get_agile, variables.s_get_throwing)

########################Общее сопротивление############################
                if msg in ["/соп", "/общ", "/сопротивление", "/общеесопротивление"]:
                    calculate_skill_result(user_id, "ОбщееСопротивление", variables.m_get_bodytype, variables.s_get_mainresistance)

########################Ношение тяж доспехов############################
                if msg in ["/дос", "/тяждосп", "/тяжелыедоспехи", "/ношениетяжелыхдоспехов"]:
                    calculate_skill_result(user_id, "НошениеТяжелыхДоспехов", variables.m_get_bodytype, variables.s_get_heavyarmour)

######################## МИ ############################
                if msg in ["/ми", "/маг", "/магия", "/магическое", "/магическоеискусство"]:
                    calculate_skill_result(user_id, "МагическоеИскусство", variables.m_get_intelligence, variables.s_get_magicalArt)

######################## Ремесло ############################
                if msg in ["/рем", "/ремесло", "/ремесло"]:
                    calculate_skill_result(user_id, "Ремесло", variables.m_get_intelligence, variables.s_get_crafting)

######################## Демонология ############################
                if msg in ["/дем", "/демонология"]:
                    calculate_skill_result(user_id, "Демонология", variables.m_get_intelligence, variables.s_get_demonology)

######################## Кузнечное Дело ############################
                if msg in ["/куз", "/кузница", "/ковка", "/кузнечноедело"]:
                    calculate_skill_result(user_id, "КузнечноеДело", variables.m_get_intelligence, variables.s_get_smithing)

######################## Кожевнечевство ############################
                if msg in ["/кож", "/кожевнечество", "/кожа", "/лезе"]:
                    calculate_skill_result(user_id, "Кожевничество", variables.m_get_intelligence, variables.s_get_leathercraft)

######################## Инженерия ############################
                if msg in ["/инж", "/инженер", "/инженерия"]:
                    calculate_skill_result(user_id, "Инженерия", variables.m_get_intelligence, variables.s_get_Engeneering)

######################## Алхимия ############################
                if msg in ["/алх", "/алхимия", "/химия"]:
                    calculate_skill_result(user_id, "Химия", variables.m_get_intelligence, variables.s_get_alchemy)

######################## Знания ############################
                if msg in ["/зна", "/знания", "/знания"]:
                    calculate_skill_result(user_id, "Знания", variables.m_get_intelligence, variables.s_get_knowlege)

######################## Подделка ############################
                if msg in ["/под", "/подделка", "/подделывание"]:
                    calculate_skill_result(user_id, "Подделка", variables.m_get_intelligence, variables.s_get_faking)

######################## Медицина ############################
                if msg in ["/мед", "/медицина", "/лечение"]:
                    calculate_skill_result(user_id, "Медицина", variables.m_get_intelligence, variables.s_get_curing)

######################## Выживание ############################
                if msg in ["/выж", "/выживание", "/выживание"]:
                    calculate_skill_result(user_id, "Выживание", variables.m_get_intelligence, variables.s_get_surviving)

######################## Воля ############################
                if msg in ["/вол", "/воля", "/вол"]:
                    calculate_skill_result(user_id, "Воля", variables.m_get_intelligence, variables.s_get_will)

######################## Внимательность ############################
                if msg in ["/вни", "/внимательность", "/внимательность"]:
                    calculate_skill_result(user_id, "Внимательность", variables.m_get_perception, variables.s_get_attention)

######################## Орлиный Глаз ############################
                if msg in ["/орл", "/орлиный", "/орлиныйглаз"]:
                    calculate_skill_result(user_id, "ОрлиныйГлаз", variables.m_get_perception, variables.s_get_hawkeye)

######################## Реакция ############################
                if msg in ["/реа", "/реа", "/реакция"]:
                    calculate_skill_result(user_id, "Реакция", variables.m_get_perception, variables.s_get_reaction)

######################## Оценка ############################
                if msg in ["/оце", "/оце", "/оценка"]:
                    calculate_skill_result(user_id, "Оценка", variables.m_get_perception, variables.s_get_estimating)

######################## Угрозы ############################
                if msg in ["/угр", "/угроза", "/угрожать"]:
                    calculate_skill_result(user_id, "Угроза", variables.m_get_empathy, variables.s_get_threaten)

######################## Убеждение ############################
                if msg in ["/убе", "/убеждение", "/убеждать"]:
                    calculate_skill_result(user_id, "Убеждение", variables.m_get_empathy, variables.s_get_belief)

######################## Лидерство ############################
                if msg in ["/лид", "/лид", "/лидерство"]:
                    calculate_skill_result(user_id, "Лидерство", variables.m_get_empathy, variables.s_get_leadership)

######################## Искусство ############################
                if msg in ["/иск", "/иск", "/искусство"]:
                    calculate_skill_result(user_id, "Искусство", variables.m_get_empathy, variables.s_get_artistic)

######################## Перевоплощение ############################
                if msg in ["/пер", "/пер", "/перевоплощение"]:
                    calculate_skill_result(user_id, "Перевоплощение", variables.m_get_empathy, variables.s_get_impersation)

######################## Ложь ############################
                if msg in ["/лож", "/лож", "/ложь"]:
                    calculate_skill_result(user_id, "Ложь", variables.m_get_empathy, variables.s_get_lying)

######################## Слухи ############################
                if msg in ["/слу", "/слу", "/слухи"]:
                    calculate_skill_result(user_id, "Слухи", variables.m_get_empathy, variables.s_get_gossip)

            except:
                sender(id, f'{name} - Возьми персонажа Х_Х')
                pass
