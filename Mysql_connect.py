import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'SecondHand_BookWeb'
}

try:
    cnx = mysql.connector.connect(**config)
    cnx.ping(reconnect=True, attempts=3, delay=5)  # 測試連接是否正常
    print("Connected to MySQL database.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
else:
    cnx.close()
