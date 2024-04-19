import sqlite3

conn = sqlite3.connect('users.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users 
             (user_id INTEGER PRIMARY KEY, username TEXT, subscribed INTEGER DEFAULT 0)''')


def add_user(user_id, username): # Add user to database
    c.execute('INSERT OR IGNORE INTO users (user_id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()

def get_username(user_id): # Get username by user_id
    c.execute('SELECT username FROM users WHERE user_id = ?', (user_id,))
    return c.fetchone()[0]

def get_users_count(): # Get users count
  c.execute('SELECT COUNT(*) FROM users')
  return c.fetchone()[0]

def set_subscribed(user_id, subscribed): # Set subscribed status
    c.execute('UPDATE users SET subscribed = ? WHERE user_id = ?', (subscribed, user_id))
    conn.commit()

def get_subscribed(user_id): # Get subscribed status
    c.execute('SELECT subscribed FROM users WHERE user_id = ?', (user_id,))
    return c.fetchone()[0]

