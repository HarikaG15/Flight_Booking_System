# Import the MySQL Connector module
# This module allows Python to connect to a MySQL database

import mysql.connector

# Connect to database
db = mysql.connector.connect(
    host="localhost",    # Server
    user="root",         # Username
    password="root",     # Password
    database="flightdb"  # Database name
)

cursor = db.cursor()     # Cursor for queries
