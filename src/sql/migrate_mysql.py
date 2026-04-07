import mysql.connector
from mysql.connector import Error

def main():
    try:
        # 1. Connect to database
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="root123", # note bad practice to hardcode credentials, but for demo purposes it's fine
            database="skola"
        )

        if conn.is_connected():
            print("Connected to MySQL")

        cursor = conn.cursor()

        # 2. Drop table (for repeatable demo)
        cursor.execute("DROP TABLE IF EXISTS skoleni")

        # 3. Create table
        create_table_sql = """
        CREATE TABLE skoleni (
            id INT AUTO_INCREMENT PRIMARY KEY,
            vards VARCHAR(50),
            uzvards VARCHAR(50),
            klase_id INT,
            videja_atzime FLOAT
        )
        """
        cursor.execute(create_table_sql)
        print("Table created")

        # 4. Insert data (parameterized → safe)
        insert_sql = """
        INSERT INTO skoleni (vards, uzvards, klase_id, videja_atzime)
        VALUES (%s, %s, %s, %s)
        """

        data = [
            ("Anna", "Bērziņa", 1, 8.5),
            ("Jānis", "Kalniņš", 1, 7.2),
            ("Marta", "Ozoliņa", 2, 9.1),
        ]

        cursor.executemany(insert_sql, data)
        conn.commit()

        print(f"{cursor.rowcount} rows inserted")

        # 5. Verify results
        cursor.execute("SELECT * FROM skoleni")

        rows = cursor.fetchall()
        print("\nData in table:")
        for row in rows:
            print(row)

    except Error as e:
        print("Error:", e)

    finally:
        # 6. Cleanup
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nConnection closed")

if __name__ == "__main__":
    main()