

import psycopg2

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            conn = psycopg2.connect(dbname="restaurant", user="postgres", password="0000000000")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)", (self.name, self.price))
            conn.commit()
            cursor.close()
            conn.close()
            print("Item was added successfully.")
        except psycopg2.Error as e:
            print(f"Error while adding item: {e}")

    def delete(self):
        try:
            conn = psycopg2.connect(dbname="restaurant", user="postgres", password="0000000000")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (self.name,))
            conn.commit()
            cursor.close()
            conn.close()
            print("Item was deleted successfully.")
        except psycopg2.Error as e:
            print(f"Error while deleting item: {e}")

    def update(self, new_name, new_price):
        try:
            conn = psycopg2.connect(dbname="restaurant", user="postgres", password="0000000000")
            cursor = conn.cursor()
            cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                           (new_name, new_price, self.name))
            conn.commit()
            cursor.close()
            conn.close()
            print("Item was updated successfully.")
        except psycopg2.Error as e:
            print(f"Error while updating item: {e}")
