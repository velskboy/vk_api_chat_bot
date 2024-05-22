import sqlite3 as sq



def get_character_stats(user_id):
    connection = sq.connect("Characters.db")
    cursor = connection.cursor()

    query = "SELECT * FROM Characters WHERE id = ?"
    cursor.execute(query, (user_id,))
    filtered_data = []
    rows = cursor.fetchall()
    
    
    columns = [description[0] for description in cursor.description]

   

    for row in rows:
        print(row)
        row_data = {}
        for column, cell in zip(columns[4:], row[4:]):
            if isinstance(cell, int) and cell > 0:
                row_data[column] = cell
        if row_data:
            print(row)
            filtered_data.append(row_data)
    cursor.close()
    connection.close()
    
    return filtered_data

def get_user_id_from_db():
    connection = sq.connect("Characters.db")
    cursor = connection.cursor()

    # Выполнить запрос для получения user_id из столбца id
    query = "SELECT id FROM Characters"
    cursor.execute(query)

    # Извлечь все значения user_id из результата запроса
    user_ids = [row[0] for row in cursor.fetchall()]

    # Закрыть соединение с базой данных
    cursor.close()
    connection.close()

    return user_ids

def find_character(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT имяПерсонажа FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            strength_value = row[0]
            return strength_value
        else:
            return None
        
def shift_list_left(lst):
    # Сохраняем первый элемент
    first_element = lst[0]
    # Сдвигаем каждый элемент на одну позицию влево
    for i in range(len(lst) - 1):
        lst[i] = lst[i + 1]
    # Помещаем первый элемент в конец списка
    lst[-1] = first_element

def update_id(db_file, search_term, new_id):
    connection = sq.connect(db_file)
    cursor = connection.cursor()

    # Выполнить обновление значения айди для соответствующих строк
    query = "UPDATE Characters SET id = ? WHERE имяПерсонажа = ?"
    cursor.execute(query, (new_id, search_term))

    # Применить изменения
    connection.commit()

    # Закрыть соединение с базой данных
    cursor.close()
    connection.close()

def m_get_strength(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT СИЛА FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            strength_value = row[0]
            return strength_value
        else:
            return None
        
def m_get_autohp(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Здоровье FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            hp_value = row[0]
            return hp_value
        else:
            return None
        
def m_get_attack_damage (character_name): ####################################################
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Урон FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            attack_value = row[0]
            return attack_value
        else:
            return None
        
def m_get_attack_speed (character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT КоличествоАтак FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            attack_speed = row[0]
            return attack_speed
        else:
            return None
        
def m_update_autohp(character_name, new_hp):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        # Обновляем значение Здоровье для заданного имениПерсонажа
        cur.execute("UPDATE characters SET Здоровье=? WHERE имяПерсонажа=?", (new_hp, character_name))
        con.commit()  # Не забудьте подтвердить изменения

def m_update_auto_current_armor(character_name, new_armor):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        # Обновляем значение Здоровье для заданного имениПерсонажа
        cur.execute("UPDATE characters SET БроняТелоТекущая=? WHERE имяПерсонажа=?", (new_armor, character_name))
        con.commit()  # Не забудьте подтвердить изменения
        
def m_get_autostrength(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT СИЛА FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            strength_value = row[0]
            return strength_value
        else:
            return None
        
def m_get_autoarmor_flat (character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT БроняТелоФлат FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            flat_armor = row[0]
            return flat_armor
        else:
            return None
        
def m_get_autoarmor_current (character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT БроняТелоТекущая FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            flat_armor = row[0]
            return flat_armor
        else:
            return None

def s_get_weightlifting (user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ТяжелаяАтлетика FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            get_weightlifting = row[0]
            return get_weightlifting
        else:
            return None
        
def s_get_hand_combat (user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT РукопашныйБой FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            hand_combat = row[0]
            return hand_combat
        else:
            return None
        
def s_get_hand_autocombat (character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT РукопашныйБой FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            hand_combat = row[0]
            return hand_combat
        else:
            return None
               
        
def s_get_blocking (user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Блокирование FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            blocking = row[0]
            return blocking
        else:
            return None
        
def s_get_autoblocking (character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Блокирование FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            blocking = row[0]
            return blocking
        else:
            return None


def s_get_melee_combat(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT БлижнийБой FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            melee_combat = row[0]
            return melee_combat
        else:
            return None
        
def s_get_melee_autocombat(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT БлижнийБой FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            melee_combat = row[0]
            return melee_combat
        else:
            return None
        
def m_get_agile(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ЛОВКОСТЬ FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            agile = row[0]
            return agile
        else:
            return None
        
def m_get_autoagile(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ЛОВКОСТЬ FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            agile = row[0]
            return agile
        else:
            return None
        
def s_get_athletics(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ЛегкаяАтлетика FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            athletics = row[0]
            return athletics
        else:
            return None
        
def s_get_picklocking(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ВзломЗамков FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            picklocking = row[0]
            return picklocking
        else:
            return None
        
def s_get_dodging(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Уклонение FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            dodging = row[0]
            return dodging
        else:
            return None
        
def s_get_autododging(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Уклонение FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            dodging = row[0]
            return dodging
        else:
            return None
        
def s_get_fencing(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Фехтование FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            fencing = row[0]
            return fencing
        else:
            return None

def s_get_autofencing(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Фехтование FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            fencing = row[0]
            return fencing
        else:
            return None
        
def s_get_crouching(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Маскировка FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            crouching = row[0]
            return crouching
        else:
            return None
        
def s_get_shooting(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Стрельба FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            shooting = row[0]
            return shooting
        else:
            return None
        
def s_get_throwing(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Метание FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            throwing = row[0]
            return throwing
        else:
            return None
        
def m_get_bodytype(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ТЕЛОСЛОЖЕНИЕ FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            bodytype = row[0]
            return bodytype
        else:
            return None
        
def s_get_mainresistance(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ОбщееСопротивление FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            mainresistance = row[0]
            return mainresistance
        else:
            return None
        
def s_get_heavyarmour(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT НошениеТяжелыхДоспехов FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            heavyarmour = row[0]
            return heavyarmour
        else:
            return None
        
def m_get_intelligence(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ИНТЕЛЛЕКТ FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            intelligence = row[0]
            return intelligence
        else:
            return None
        
def s_get_magicalArt(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT МагическоеИскусство FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            magicalArt = row[0]
            return magicalArt
        else:
            return None
        
def s_get_crafting(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Ремесло FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            crafting = row[0]
            return crafting
        else:
            return None
        
def s_get_demonology(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Демонология FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            demonology = row[0]
            return demonology
        else:
            return None
        
def s_get_smithing(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT КузнечноеДело FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            smithing = row[0]
            return smithing
        else:
            return None
        
def s_get_leathercraft(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Кожевничество FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            leathercraft = row[0]
            return leathercraft
        else:
            return None
        
def s_get_Engeneering(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Инженерия FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            Engeneering = row[0]
            return Engeneering
        else:
            return None
        
def s_get_alchemy(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Алхимия FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            alchemy = row[0]
            return alchemy
        else:
            return None
        
def s_get_knowlege(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Знания FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            knowlege = row[0]
            return knowlege
        else:
            return None
        
def s_get_faking(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Подделка FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            faking = row[0]
            return faking
        else:
            return None
        
def s_get_curing(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Медицина FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            curing = row[0]
            return curing
        else:
            return None
        
def s_get_surviving(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Выживание FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            surviving = row[0]
            return surviving
        else:
            return None
        
def s_get_will(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Воля FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            will = row[0]
            return will
        else:
            return None
        
def m_get_perception(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ВОСПРИЯТИЕ FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            perception = row[0]
            return perception
        else:
            return None
        
def m_get_autoperception(name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ВОСПРИЯТИЕ FROM characters WHERE имяПерсонажа=?", (name,))
        row = cur.fetchone()
        if row is not None:
            perception = row[0]
            return perception
        else:
            return None
        
def s_get_attention(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Внимательность FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            attention = row[0]
            return attention
        else:
            return None
        
def s_get_hawkeye(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ОрлиныйГлаз FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            hawkeye = row[0]
            return hawkeye
        else:
            return None
        
def s_get_reaction(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Реакция FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            reaction = row[0]
            return reaction
        else:
            return None
        
def s_get_autoreaction(name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Реакция FROM characters WHERE имяПерсонажа=?", (name,))
        row = cur.fetchone()
        if row is not None:
            reaction = row[0]
            return reaction
        else:
            return None
        
def s_get_estimating(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Оценка FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            estimating = row[0]
            return estimating
        else:
            return None
        
def m_get_empathy(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ЭМПАТИЯ FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            empathy = row[0]
            return empathy
        else:
            return None
        
def s_get_threaten(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Угрозы FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            threaten = row[0]
            return threaten
        else:
            return None
        
def s_get_belief(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Убеждение FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            belief = row[0]
            return belief
        else:
            return None
        
def s_get_leadership(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Лидерство FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            leadership = row[0]
            return leadership
        else:
            return None
        
def s_get_artistic(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Искусства FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            artistic = row[0]
            return artistic
        else:
            return None
        
def s_get_impersation(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Перевоплощение FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            impersation = row[0]
            return impersation
        else:
            return None
        
def s_get_lying(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Ложь FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            lying = row[0]
            return lying
        else:
            return None
        
def s_get_modifier(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Модификатор FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            modifier = row[0]
            return modifier
        else:
            return None
        
def s_get_automodifier(character_name):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Модификатор FROM characters WHERE имяПерсонажа=?", (character_name,))
        row = cur.fetchone()
        if row is not None:
            modifier = row[0]
            return modifier
        else:
            return None
        
def s_get_heavyshoot(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ТяжелаяСтрельба FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            heavyshoot = row[0]
            return heavyshoot
        else:
            return None
        
def s_get_gossip(user_id):
    with sq.connect("Characters.db") as con:
        cur = con.cursor()
        cur.execute("SELECT Воровство FROM characters WHERE id=?", (user_id,))
        row = cur.fetchone()
        if row is not None:
            gossip = row[0]
            return gossip
        else:
            return None