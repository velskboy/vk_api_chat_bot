import sqlite3 as sq


with sq.connect("Characters.db") as con:
    cur = con.cursor()

    
    cur.execute("""CREATE TABLE IF NOT EXISTS characters (
    id INTEGER,
    имя TEXT,
    имяПерсонажа TEXT,
    Здоровье INTEGER,
    МаксимальноеЗдоровье INTEGER,
    Мана INTEGER,
    МаксМана INTEGER,
    СИЛА INTEGER DEFAULT 0,
    ТяжелаяАтлетика INTEGER DEFAULT -4,
    РукопашныйБой INTEGER DEFAULT -4,
    Блокирование INTEGER DEFAULT -4,
    БлижнийБой INTEGER DEFAULT -4,
    ЛОВКОСТЬ INTEGER DEFAULT 0,
    ЛегкаяАтлетика INTEGER DEFAULT -4,
    ВзломЗамков INTEGER DEFAULT -4,
    Уклонение INTEGER DEFAULT -4,
    Фехтование INTEGER DEFAULT -4,
    Маскировка INTEGER DEFAULT -4,
    Стрельба INTEGER DEFAULT -4,
    Метание INTEGER DEFAULT -4,
    ТЕЛОСЛОЖЕНИЕ INTEGER DEFAULT 0,
    ОбщееСопротивление INTEGER DEFAULT -4,
    НошениеТяжелыхДоспехов INTEGER DEFAULT -4,
    ИНТЕЛЛЕКТ INTEGER DEFAULT 0,
    МагическоеИскусство INTEGER DEFAULT -4,
    Ремесло INTEGER DEFAULT -4,
    Демонология INTEGER DEFAULT -4,
    КузнечноеДело INTEGER DEFAULT -4,
    Кожевничество INTEGER DEFAULT -4,
    Инженерия INTEGER DEFAULT -4,
    Алхимия INTEGER DEFAULT -4,
    Знания INTEGER DEFAULT -4,
    Подделка INTEGER DEFAULT -4,
    Медицина INTEGER DEFAULT -4,
    Выживание INTEGER DEFAULT -4,
    Воля INTEGER DEFAULT -4,
    ВОСПРИЯТИЕ INTEGER DEFAULT 0,
    Внимательность INTEGER DEFAULT -4,
    ОрлиныйГлаз INTEGER DEFAULT -4,
    Реакция INTEGER DEFAULT -4,
    Оценка INTEGER DEFAULT -4,
    ЭМПАТИЯ INTEGER DEFAULT 0,
    Угрозы INTEGER DEFAULT -4,
    Убеждение INTEGER DEFAULT -4,
    Лидерство INTEGER DEFAULT -4,
    Искусства INTEGER DEFAULT -4,
    Перевоплощение INTEGER DEFAULT -4,
    Ложь INTEGER DEFAULT -4
    )""")