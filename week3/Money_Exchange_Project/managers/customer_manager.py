from database import create_connection
import sqlite3


class Customer:
    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address
        self.last_inserted_id = 0

    def __repr__(self):
        return f"Customer {self.name}, email {self.email} and address {self.address}"

    def create_customer(self):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO customer (name, email, address) VALUES (?, ?, ?)", (self.name, self.email, self.address))
            conn.commit()
            self.last_inserted_id = cursor.lastrowid
            print("Customer added successfully.")
        except sqlite3.IntegrityError:
            print("Customer already added.")
        conn.close()

    @staticmethod
    def view_customer():
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer")
        rows = cursor.fetchall()
        conn.close()
        return rows

    @staticmethod
    def search_customer(name: str):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer WHERE name LIKE ?", ('%' + name + '%',))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def delete_customer(self):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM customer WHERE id = ?", (self.last_inserted_id,))
        conn.commit()
        conn.close()
        print("🗑️ Customer deleted.")
