import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="127.0.0.1", # datubāzes servera adrese, var būt arī "localhost"
    port=3306, # ports var būt arī cits bet tipiski virs 1024, piemēram 3306 ir MySQL standarta ports
    user="root", # var būt arī cits lietotājs, bet parasti ir jāizveido datubāzes lietotājs ar atbilstošām tiesībām
    password="root123", # atkal pareizāk būtu izmantot vides mainīgos vai konfigurācijas failu, nevis rakstīt paroli tieši kodā
    database="skola"
)

sql = "SELECT * FROM skoleni"
# ja lielāks pieprasījums tad varam izmantot """ SQL vaicājumu, lai varētu rakstīt vairākas rindas un tas būtu pārskatāmāk
# sql = """
# SELECT *
# FROM skoleni
# WHERE videja_atzime > 8.0
# """
df = pd.read_sql(sql, conn) # no datubāzes izlasām datus un saglabājam tos DataFrame formātā, izmantojot pandas bibliotēku
# šeit varētu jau glabāt kā CSV vai Excel failu, bet šoreiz tikai izdrukāsim DataFrame, lai pārliecinātos, ka dati ir nolasīti pareizi
print(df)