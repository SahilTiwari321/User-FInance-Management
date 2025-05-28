import sqlite3
import hashlib
from database import get_connection, DB_NAME

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    password_hash = hash_password(password)
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        return True, "User registered successfully."
    except sqlite3.IntegrityError:
        return False, "Username already exists."
    finally:
        conn.close()

def login(username, password):
    password_hash = hash_password(password)
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password_hash = ?', (username, password_hash))
    user = c.fetchone()
    conn.close()
    return (True, "Login successful.") if user else (False, "Invalid credentials.")

def get_user_id(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT id FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user[0] if user else None
