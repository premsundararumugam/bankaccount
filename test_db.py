import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bank_db"
    )

    print("Connected to MySQL successfully!")

    conn.close()

except Exception as e:
    print("Error:", e)