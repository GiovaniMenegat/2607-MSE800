from database import create_connection
import sqlite3

class Exchange:
    def __init__(self, original_amount: float, final_amount: float, date: str, exchange_rate_id: int, customer_id: int):
        self.original_amount = original_amount
        self.final_amount = final_amount
        self.date = date
        self.exchange_rate_id = exchange_rate_id
        self.customer_id = customer_id

    def __repr__(self):
        return f"Exchange original_amount {self.original_amount}, final_amount {self.final_amount}, date {self.date}, exchange_rate_id {self.exchange_rate_id} and customer_id {self.customer_id}"

    def create_exchange(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO exchange (original_amount, final_amount, date, exchange_rate_id, customer_id) VALUES (?, ?, ?, ?, ?)", (self.original_amount, self.final_amount, self.date, self.exchange_rate_id, self.customer_id))
            conn.commit()
            print("Exchange added successfully.")
        except sqlite3.IntegrityError:
            print("Exchange already added.")
        conn.close()

    @staticmethod
    def view_exchange():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exchange")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_exchange_by_id(id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exchange WHERE id = ?", (id,))
        rows = cursor.fetchall()
        conn.close()
        return rows
