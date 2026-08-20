import sqlite3

def create_connection():
    conn = sqlite3.connect("money_exchange.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            address TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS currency (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            country TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS exchange_rate (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rate FLOAT NOT NULL,
            date TEXT NOT NULL,
            from_currency_id INT,
            to_currency_id INT,
            FOREIGN KEY (from_currency_id) REFERENCES currency(id),
            FOREIGN KEY (to_currency_id) REFERENCES currency(id)
        );
        
        CREATE TABLE IF NOT EXISTS exchange (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_amount FLOAT NOT NULL,
            final_amount FLOAT NOT NULL,
            date TEXT NOT NULL,
            exchange_rate_id INT,
            customer_id INT,
            FOREIGN KEY (exchange_rate_id) REFERENCES exchange_rate(id),
            FOREIGN KEY (customer_id) REFERENCES customer(id)
        );
    ''')
    conn.commit()
    conn.close()
