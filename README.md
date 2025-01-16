# Inventory App

The Inventory App is a Flask-based application that allows you to manage an inventory system with an Azure SQL Database (or another SQL database of your choice). This example uses **Azure SQL Database** as the backend.

## Prerequisites

Before you start, ensure you have the following:
1. **Python 3.6 or later** installed.
2. **Azure SQL Database** (or any other SQL database). You can follow [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/azure-sql/database/quickstart-create-sql-database) to create an Azure SQL Database. This app uses Azure SQL Database in the example configuration.
3. **ODBC Driver 18 for SQL Server** installed:
   - Follow the installation guide for your operating system in the [Microsoft Docs](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server).

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/inventory_app.git
cd inventory_app
```

### 2. Create a Virtual Environment
Create and activate a virtual environment for dependency management:

#### Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Required Python Packages
Install the required dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Testing Your SQL Connection

### Configure Database Connection
Before running the application, ensure your database connection is configured correctly:
1. You will be prompted to enter:
   - **Azure SQL Server name** (e.g., `your-server-name.database.windows.net`).
   - **Database name**.
   - **Username**.
   - **Password**.

### Test the Connection
Run the `test_connection.py` script to verify your SQL database connection:

```bash
python test_connection.py
```

If the connection is successful, you'll see a confirmation message.

---

## Running the Inventory App

1. Start the Flask application:

```bash
python inventory_app.py
```

2. Open a web browser and navigate to the server's IP address on port `5000` (HTTP only):

```text
http://<server-ip>:5000
```

Replace `<server-ip>` with the IP address of the server where the app is running.

---

## Notes

- **SQL Database**: This app assumes you are using an Azure SQL Database. However, you can use other SQL databases if you configure the connection properly.
- **Security**: The app runs on HTTP for simplicity in this example. For production environments, consider using HTTPS for secure communication.
- **Port Configuration**: The app runs on port `5000` by default. Ensure this port is open on your server.

---

## Additional Resources

- [How to Create an Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/quickstart-create-sql-database)
- [Download ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
