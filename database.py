import sqlite3



def create_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "DROP TABLE IF EXISTS login"
    cursor.execute(query)
    conn.commit()

    query = "CREATE TABLE login(username VARCHAR UNIQUE, password VARCHAR)"
    cursor.execute(query)
    conn.commit()

def add_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "INSERT OR IGNORE INTO login (username, password) VALUES (?, ?)"
    cursor.execute(query, (username, password))
    conn.commit()

def check_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = 'SELECT * FROM login WHERE username = ? AND password = ?'
    cursor.execute(query, (str(username), str(password)))
    result = cursor.fetchone()
    conn.commit()
    print('[DEBUG][check] result:', result)
    return result



# --- main ---




#create_table()  # use only once


#add_user("admin", "admin")


