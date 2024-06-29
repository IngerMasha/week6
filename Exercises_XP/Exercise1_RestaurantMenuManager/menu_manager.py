

import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        try:
            conn = psycopg2.connect(dbname="restaurant", user="postgres", password="0000000000")
            cursor = conn.cursor()
            cursor.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s", (name,))
            item = cursor.fetchone()
            cursor.close()
            conn.close()
            if item:
                return MenuItem(item[0], item[1])
            else:
                return None
        except psycopg2.Error as e:
            print(f"Error while retrieving item: {e}")
            return None
    @classmethod
    def all_items(cls):
        try:
            conn = psycopg2.connect(dbname="restaurant", user="postgres", password="0000000000")
            cursor = conn.cursor()
            cursor.execute("SELECT item_name, item_price FROM Menu_Items")
            items = cursor.fetchall()
            cursor.close()
            conn.close()
            return [MenuItem(item[0], item[1]) for item in items]
        except psycopg2.Error as e:
            print(f"Error while retrieving all items: {e}")
            return []