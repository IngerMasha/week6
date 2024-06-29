import psycopg2
import bcrypt
from psycopg2 import IntegrityError


def connect_db():
    return psycopg2.connect(dbname="users_db", user="postgres", password="0000000000", host="localhost", port="5432")


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def check_password(conn, username, password):
    with conn.cursor() as cursor:
        cursor.execute('SELECT password FROM users WHERE username = %s', (username,))
        result = cursor.fetchone()
        if result:
            hashed_password = result[0]
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
        else:
            return False


def add_user(conn, username, password):
    hashed_password = hash_password(password)
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        conn.commit()


def main():
    conn = connect_db()

    logged_in = None

    while True:
        action = input("Enter 'login' to log in, 'exit' to exit: ").strip().lower()

        if action == "exit":
            break
        elif action == "login":
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            if check_password(conn, username, password):
                print("You have successfully logged in.")
                logged_in = username
            else:
                signup = input("User does not exist. Would you like to sign up? (yes/no): ").strip().lower()
                if signup == "yes":
                    while True:
                        new_username = input("Enter a new username: ").strip()
                        new_password = input("Enter a password: ").strip()

                        try:
                            add_user(conn, new_username, new_password)
                            print("You have successfully registered. You can now log in.")
                            break
                        except IntegrityError:
                            print("This username is already taken. Please choose another username.")
                elif signup == "no":
                    continue
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid command. Please enter 'login' or 'exit'.")

    conn.close()


if __name__ == "__main__":
    main()
