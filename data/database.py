import sqlite3

conn = sqlite3.connect('db.db')
cur = conn.cursor()
cur.execute(
    f'''CREATE TABLE IF NOT EXISTS users (user_id INTEGER, is_blocked INTEGER, is_admin INTEGER, full_name TEXT, phone TEXT, time TEXT, id INTEGER, language TEXT);''')
cur.execute(
    f'''CREATE TABLE IF NOT EXISTS channels(channel_id INTEGER, user_id INTEGER, name TEXT, is_required INTEGER); ''')
cur.execute(f'''CREATE TABLE IF NOT EXISTS messages(message_id INTEGER, user_id INTEGER, receiver TEXT, message TEXT, time TEXT);''')
conn.commit()

#host = 'https://shohrux1.pythonanywhere.com'
host = 'http://127.0.0.1:8000'

