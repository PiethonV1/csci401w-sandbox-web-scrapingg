
import sqlite3
import os
from datetime import datetime

# Define the path to the directory and database
db_directory = "../data"
db_path = os.path.join(db_directory, 'database.db')

# Ensure the directory exists
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Create or connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Stock_Ticker(
        Ticker VARCHAR (10),
        Open_date DATE,
        Open_Price DECIMAL(6,2),
        High DECIMAL(6,2),
        Low DECIMAL(6,2),
        Close_price DECIMAL(6,2),
        PRIMARY KEY (Ticker, Open_date)
    )        
''')

# Create the favorite_foods table
cursor.execute('''
    CREATE TABLEIF NOT EXISTS User(
        UserName VARCHAR(20) UNIQUE NOT NULL, 
        Email_Addr VARCHAR(100) CHECK (Email_Addr IN ('abcdefghijiklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ','~!@#$%_^&*()')),
        PRIMARY KEY(UserName)
    )           
''')

# Insert 10 sample records for users

# Insert 10 sample records
sample_user = [
    ("Jason Foo", "jason@hinton.io"),
    ("Joe Smith", "joe@example.com"),
    ("Frank", "Frank@gmail.com"),
    ("Bobby", "bob@eyahoo.com"),
    ("Charlie", "charlie@hinton.io"),
    ("Alice2", "alice@gmail.com"),
    ("Eva ", "eve@example.com"),
    ("Frank McAdams", "frank@emx.com"),
    ("Grace Ma", "grace@custom.com"),
    ("Benny C", "Benny@stopshop.com")
]

cursor.executemany('''
    INSERT OR IGNORE INTO users (username, email) 
    VALUES (?, ?)
''', sample_user)

# Insert sample records for favorite_foods for each user
sample_Stock_Ticker = [
    ("GOOG", 2023-11-20T00:00:00, 135.5000, 138.4250, 135.4900, 137.9200),
    ("GOOG", 2023-11-21T00:00:00, 137.5000, 138.9650, 137.7050, 138.6200),
    ("GOOG", 2023-11-22T00:00:00, 139.1000, 141.1000, 139.0000, 140.0200),
    ("AAPL", 2023-11-20T00:00:00, 189.8900, 191.9100, 189.7400, 190.6400),
    ("AAPL", 2023-11-21T00:00:00, 191.4100, 192.9300, 190.8300, 191.3100),
    ("AAPL", 2023-11-22T00:00:00, 191.4900, 192.9300, 190.8300, 191.3100),
    ("MSFT", 2023-11-20T00:00:00, 371.2200, 378.8700, 371.0000, 377.4400),
    ("MSFT", 2023-11-21T00:00:00, 375.6700, 376.2200, 371.1200, 373.0700),
    ("MSFT", 2023-11-22T00:00:00, 378.0000, 379.7900, 374.9700, 377.8500),
    ("GME", 2023-11-20T00:00:00, 13.0000, 13.2000, 12.8000, 12.8000),
    ("GME", 2023-11-21T00:00:00, 12.6500, 12.7200, 12.2600, 12.5500),
    ("GME", 2023-11-22T00:00:00, 12.5600, 12.7100, 12.1900, 12.2900),
]

cursor.executemany('''
    INSERT INTO Stock_Ticker (ticker, Open_date, Open_Price, High, Low, Close_price)
    VALUES (?, datetime.now().date(), ?, ?, ?, ?)
''', sample_Stock_Ticker)
# Commit the changes and close the connection
conn.commit()
conn.close()

print("Script execution completed!")