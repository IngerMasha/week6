import psycopg2

def create_database():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="0000000000")
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE users_db")
        cursor.close()
        conn.close()

        print("База данных 'users_db' успешно создана.")

    except psycopg2.Error as e:
        print("Ошибка при создании базы данных:")
        print(e)

def create_users_table():
    try:
        conn = psycopg2.connect(dbname="users_db", user="postgres", password="0000000000")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Таблица 'users' успешно создана.")
    except psycopg2.Error as e:
        print("Ошибка при создании таблицы 'users':")
        print(e)

if __name__ == "__main__":
    create_database()
    create_users_table()
