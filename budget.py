from database import get_connection
from datetime import datetime

def set_budget(user_id, category, limit):
    month = datetime.now().strftime('%Y-%m')
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO budgets (user_id, category, limit, month)
        VALUES (?, ?, ?, ?)
    ''', (user_id, category, limit, month))
    conn.commit()
    conn.close()

def check_budget(user_id, category):
    month = datetime.now().strftime('%Y-%m')
    conn = get_connection()
    c = conn.cursor()

    c.execute('''
        SELECT SUM(amount) FROM transactions
        WHERE user_id = ? AND category = ? AND type = 'expense' AND strftime('%Y-%m', date) = ?
    ''', (user_id, category, month))
    spent = c.fetchone()[0] or 0

    c.execute('''
        SELECT limit FROM budgets WHERE user_id = ? AND category = ? AND month = ?
    ''', (user_id, category, month))
    result = c.fetchone()
    conn.close()

    return spent, result[0], spent > result[0] if result else (spent, 0, False)
