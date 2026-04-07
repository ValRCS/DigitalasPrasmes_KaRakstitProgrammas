import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root123",
    database="skola"
)


cursor = conn.cursor()
print("Savienojums izveidots")
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.execute("SELECT * FROM skoleni")
print(cursor.fetchall())

cursor.close()
conn.close()