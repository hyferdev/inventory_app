#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import pyodbc
from getpass import getpass
import os

class InventoryApp:
    def __init__(self):
        # Use environment variables if set, otherwise prompt for inputs
        self.server = os.getenv("AZURE_SQL_SERVER") or input("Enter the Azure SQL Server name: ").strip()
        self.database = os.getenv("AZURE_SQL_DATABASE") or input("Enter the Azure SQL Database name: ").strip()
        self.username = os.getenv("AZURE_SQL_USERNAME") or input("Enter your Azure SQL username: ").strip()
        self.password = os.getenv("AZURE_SQL_PASSWORD") or getpass("Enter your Azure SQL password: ").strip()

        # Establish the database connection
        try:
            self.conn = pyodbc.connect(
                f"DRIVER={{ODBC Driver 18 for SQL Server}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"
                "Encrypt=yes;"
                "TrustServerCertificate=no;"
                "Connection Timeout=30;"
            )
            self.cursor = self.conn.cursor()
            print("Connected to Azure SQL Server successfully!")
        except Exception as e:
            print("Failed to connect to Azure SQL Server:")
            print(e)
            exit(1)

    def get_inventory(self):
        query = "SELECT item_name, quantity FROM Inventory"
        self.cursor.execute(query)
        return {row[0]: row[1] for row in self.cursor.fetchall()}

    def add_item(self, item_name, quantity):
        query = "SELECT quantity FROM Inventory WHERE item_name = ?"
        self.cursor.execute(query, (item_name,))
        result = self.cursor.fetchone()

        if result:
            updated_quantity = result[0] + quantity
            update_query = "UPDATE Inventory SET quantity = ? WHERE item_name = ?"
            self.cursor.execute(update_query, (updated_quantity, item_name))
        else:
            insert_query = "INSERT INTO Inventory (item_name, quantity) VALUES (?, ?)"
            self.cursor.execute(insert_query, (item_name, quantity))

        self.conn.commit()

    def check_out_item(self, item_name, quantity):
        query = "SELECT quantity FROM Inventory WHERE item_name = ?"
        self.cursor.execute(query, (item_name,))
        result = self.cursor.fetchone()

        if result and result[0] >= quantity:
            updated_quantity = result[0] - quantity
            if updated_quantity > 0:
                update_query = "UPDATE Inventory SET quantity = ? WHERE item_name = ?"
                self.cursor.execute(update_query, (updated_quantity, item_name))
            else:
                delete_query = "DELETE FROM Inventory WHERE item_name = ?"
                self.cursor.execute(delete_query, (item_name,))
            self.conn.commit()

app = Flask(__name__)

# Instantiate the InventoryApp class once
inventory_app = InventoryApp()

@app.route('/')
def home():
    inventory = inventory_app.get_inventory()
    return render_template('inventory.html', inventory=inventory)

@app.route('/check_in', methods=['POST'])
def check_in():
    item_name = request.form['item_name'].strip()
    quantity = int(request.form['quantity'].strip())
    if item_name and quantity > 0:
        inventory_app.add_item(item_name, quantity)
    return redirect(url_for('home'))

@app.route('/check_out', methods=['POST'])
def check_out():
    item_name = request.form['item_name'].strip()
    quantity = int(request.form['quantity'].strip())
    if item_name and quantity > 0:
        inventory_app.check_out_item(item_name, quantity)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, host="0.0.0.0", port=5000)

