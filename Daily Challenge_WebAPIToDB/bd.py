import psycopg2


def create_countries_db():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="0000000000"
        )
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE countries")
        cursor.close()
        conn.close()
        print("База данных 'countries' успешно создана.")

    except psycopg2.Error as e:
        print("Ошибка при создании базы данных:")
        print(e)


def create_countries_table():
    try:
        conn = psycopg2.connect(
            dbname="countries",
            user="postgres",
            password="0000000000"
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS countries (
                country_id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                capital VARCHAR(100),
                subregion VARCHAR(100),
                population INT
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Таблица 'countries' успешно создана.")
    except psycopg2.Error as e:
        print("Ошибка при создании таблицы:")
        print(e)


def insert_country_data(countries_data):
    try:
        conn = psycopg2.connect(
            dbname="countries",
            user="postgres",
            password="0000000000"
        )
        cursor = conn.cursor()
        for country_data in countries_data:
            name = country_data['name']
            capital = country_data['capital']
            subregion = country_data['subregion']
            population = country_data['population']
            query = """
                INSERT INTO countries (name, capital, subregion, population)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (name, capital, subregion, population))
        conn.commit()
        print("Данные успешно добавлены в таблицу 'countries'.")
    except psycopg2.Error as e:
        print("Ошибка при добавлении данных:")
        print(e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
