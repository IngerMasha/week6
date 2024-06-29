import psycopg2

try:
    # Подключаемся к существующему серверу PostgreSQL (обычно localhost)
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="0000000000")
    conn.autocommit = True
    cursor = conn.cursor()

    # Создаем новую базу данных "restaurant", если она еще не существует
    cursor.execute("CREATE DATABASE restaurant")

    # Закрываем курсор и соединение
    cursor.close()
    conn.close()

    print("База данных 'restaurant' успешно создана.")

except psycopg2.Error as e:
    print("Ошибка при создании базы данных:")
    print(e)
try:
    # Подключаемся к базе данных "restaurant"
    conn = psycopg2.connect(dbname="restaurant", user="postgres", password="0000000000")
    cursor = conn.cursor()

    # Создаем таблицу Menu_Items
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Menu_Items (
            item_id SERIAL PRIMARY KEY,
            item_name VARCHAR(30) NOT NULL,
            item_price SMALLINT DEFAULT 0
        )
    """)
    conn.commit()

    # Закрываем курсор и соединение
    cursor.close()
    conn.close()

    print("Таблица 'Menu_Items' успешно создана.")

except psycopg2.Error as e:
    print("Ошибка при создании таблицы Menu_Items:")
    print(e)
