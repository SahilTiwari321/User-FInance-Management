from database import get_connection
from utils import get_current_date

def add_transaction(user_id, amount, type_, category, description):
    date = get_current_date()
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO transactions (user_id, date, amount, type, category, description)
        VALUES (?, ?, ?, ?, ?, ?)''', (user_id, date, amount, type_, category, description))
    conn.commit()
    conn.close()

def get_transactions(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        SELECT date, type, category, amount, description 
        FROM transactions WHERE user_id = ? 
        ORDER BY date DESC''', (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows
