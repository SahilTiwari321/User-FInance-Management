# User-FInance-Management

A command-line based Python application for managing personal finances. This tool allows users to register/login, track income and expenses, manage budgets, and generate financial reports. It uses SQLite for data persistence.

## Features

-  User registration and authentication
-  Income and expense tracking
-  Budget management and comparison
-  Financial reporting
-  Persistent storage with SQLite

## Folder Structure

```
NEW PROJECT/
├── auth.py            # User registration & authentication
├── budget.py          # Budget-related operations
├── database.py        # Database connection and operations
├── finance.py         # Income and expense tracking logic
├── finance_app.db     # SQLite database file
├── main.py            # Entry point of the application
├── reports.py         # Generate and display financial reports
├── utils.py           # Utility functions
└── __pycache__/       # Python bytecode cache
```

## Requirements

- Python 3.10 or above
- SQLite (comes bundled with Python)

## How to Run

1. Clone or extract the project.
2. Navigate to the project directory.
3. Run the application:

```bash
python main.py
```

## Usage

The application is fully interactive via terminal and guides users through:
- Logging in or registering
- Adding income and expenses
- Viewing budget vs actual expenses
- Generating simple reports

