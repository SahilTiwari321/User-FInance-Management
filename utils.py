from datetime import datetime

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

def format_currency(amount):
    return f"₹{amount:,.2f}"

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a number.")

def print_transaction_row(row):
    print(f"{row[0]} | {row[1].capitalize():7} | {row[2]:10} | {format_currency(row[3]):>10} | {row[4]}")
