from database import create_connection
import sqlite3

class Currency:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.last_inserted_id = 0

    def __repr__(self):
        return f"Currency {self.name} and country {self.country}"

    def create_currency(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO currency (name, country) VALUES (?, ?)", (self.name, self.country))
            conn.commit()
            self.last_inserted_id = cursor.lastrowid
            print("Currency added successfully.")
        except sqlite3.IntegrityError:
            print("Currency already added.")
        conn.close()

    @staticmethod
    def view_currency():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM currency")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_currency(name):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM currency WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_currency(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM currency WHERE id = ?", (self.last_inserted_id,))
        conn.commit()
        conn.close()
        print("🗑️ currency deleted.")
