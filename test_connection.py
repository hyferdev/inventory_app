#!/usr/bin/env python3
import pyodbc
from getpass import getpass

# Prompt user for Azure SQL connection details
server = input("Enter the Azure SQL Server name: ").strip()
database = input("Enter the Azure SQL Database name: ").strip()
username = input("Enter your Azure SQL username: ").strip()
password = getpass("Enter your Azure SQL password: ").strip()  # Hidden input for security

try:
    # Establish connection
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )
    print("Connection to Azure SQL Server was successful!")
    conn.close()

except Exception as e:
    print("Failed to connect to Azure SQL Server:")
    print(e)

