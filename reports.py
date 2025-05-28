from database import get_connection

def get_summary(user_id, period='monthly'):
    conn = get_connection()
    c = conn.cursor()

    query = '''
        SELECT strftime('%Y-%m', date) as period, type, SUM(amount)
        FROM transactions
        WHERE user_id = ?
        GROUP BY period, type
    ''' if period == 'monthly' else '''
        SELECT strftime('%Y', date) as period, type, SUM(amount)
        FROM transactions
        WHERE user_id = ?
        GROUP BY period, type
    '''

    c.execute(query, (user_id,))
    results = c.fetchall()
    conn.close()
    return results
