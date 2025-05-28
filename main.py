import auth
import finance
import reports
import budget
from database import init_all_tables
from utils import get_positive_float, print_transaction_row

def show_menu():
    print("\n1. Add Transaction\n2. View Transactions\n3. View Report\n4. Set Budget\n5. Check Budget\n0. Exit")

def main():
    init_all_tables()
    print("Welcome to Personal Finance Manager")
    choice = input("1. Register\n2. Login\n> ")

    username = input("Username: ")
    password = input("Password: ")

    success, msg = auth.register(username, password) if choice == "1" else auth.login(username, password)
    print(msg)
    if not success:
        return

    user_id = auth.get_user_id(username)

    while True:
        show_menu()
        option = input("> ")

        if option == "1":
            t_type = input("Type (income/expense): ").lower()
            if t_type not in ['income', 'expense']:
                print("Invalid type.")
                continue
            category = input("Category: ")
            amount = get_positive_float("Amount: ")
            desc = input("Description: ")
            finance.add_transaction(user_id, amount, t_type, category, desc)

        elif option == "2":
            transactions = finance.get_transactions(user_id)
            for row in transactions:
                print_transaction_row(row)

        elif option == "3":
            period = input("Period (monthly/yearly): ").lower()
            summary = reports.get_summary(user_id, period)
            for row in summary:
                print(f"{row[0]} | {row[1].capitalize():7}: ₹{row[2]:,.2f}")

        elif option == "4":
            category = input("Category: ")
            limit = get_positive_float("Monthly limit: ")
            budget.set_budget(user_id, category, limit)
            print(" Budget set successfully.")

        elif option == "5":
            category = input("Category: ")
            spent, limit, exceeded = budget.check_budget(user_id, category)
            print(f"Spent: ₹{spent:,.2f} / ₹{limit:,.2f}")
            if exceeded:
                print(" Budget exceeded!")

        elif option == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
