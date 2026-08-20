from database import create_connection
import sqlite3

class ExchangeRate:
    def __init__(self, rate: float, date: str, from_currency_id: int, to_currency_id: int):
        self.rate = rate
        self.date = date
        self.from_currency_id = from_currency_id
        self.to_currency_id = to_currency_id

    def __repr__(self):
        return f"ExchangeRate rate {self.rate}, date {self.date}, from_currency_id {self.from_currency_id}, to_currency_id {self.to_currency_id}"

    def create_exchange_rate(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO exchange_rate (rate, date, from_currency_id, to_currency_id) VALUES (?, ?, ?, ?)", (self.rate, self.date, self.from_currency_id, self.to_currency_id))
            conn.commit()
            print("ExchangeRate added successfully.")
        except sqlite3.IntegrityError:
            print("ExchangeRate already added.")
        conn.close()

    @staticmethod
    def view_exchange_rate():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exchange_rate")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def search_exchange_rate_by_currency_pair(from_currency_id: int, to_currency_id: int):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM exchange_rate WHERE from_currency_id = ? AND to_currency_id = ?", (from_currency_id, to_currency_id))
        rows = cursor.fetchall()
        conn.close()
        return rows
