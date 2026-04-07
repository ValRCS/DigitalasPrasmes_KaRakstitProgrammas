# vispirms importējam nepieciešamās bibliotēkas
import mysql.connector

# izveidojam savienojumu ar MySQL datubāzi
db = mysql.connector.connect(
    host="localhost",  # datubāzes servera adrese
    user="root",       # lietotājvārds
    password="root123", # parole, aizvietojiet ar savu paroli
    #FIXME password nav vēlams rakstīt tieši kodā, labāk izmantot vides mainīgos vai konfigurācijas failu    
    database="skola"   # datubāzes nosaukums
)

print(db) # izdruka savienojuma objektu, lai pārliecinātos, ka savienojums ir izveidots veiksmīgi

# izveidojam kursora objektu, lai varētu izpildīt SQL vaicājumus
cursor = db.cursor()
print(cursor) # izdruka kursora objektu, lai pārliecinātos, ka tas ir izveidots veiksmīgi

# izpildām SQL vaicājumu, lai iegūtu datus no tabulas "skoleni"
cursor.execute("SELECT * FROM skoleni") # tātad iekšā tekstā ir SQL vaicājums, kas izvēlas visus datus no tabulas "skoleni"
result = cursor.fetchall() # atgriež visus rezultātus kā sarakstu ar rindiņām, kur katra rindiņa ir tuplis ar kolonnas vērtībām
print(result) # izdruka iegūtos datus, lai pārliecinātos, ka vaicājums ir izpildīts veiksmīgi

# apskatīsim piemēru ar parametriem, lai izvairītos no SQL injekcijas
# tātad mums būs meklētā klase 10a
# mekleta_klase = "10a"
# # un SQL šablons, kur mēs izmantosim %s kā vietturis parametram
# sql = "SELECT * FROM skoleni WHERE klase = %s"
# vertiba = (mekleta_klase,) # parametri jāievieto kā korteža (tuple), pat ja ir tikai viens parametrs, jābūt komatam
# cursor.execute(sql, vertiba) # izpildām vaicājumu ar parametri
# result = cursor.fetchall() # atgriež visus rezultātus kā sarakstu ar rindiņām, kur katra rindiņa ir tuplis ar kolonnas vērtībām
# print(result) # izdruka iegūtos datus, lai pārliecinātos, ka vaicājums ir izpildīts veiksmīgi

# meklēsim skolēnus ar vidējo atzīmi virs 8.0
mekleta_atzime = 8.0
sql = "SELECT * FROM skoleni WHERE videja_atzime > %s"
vertiba = (mekleta_atzime,) # parametri jāievieto kā korteža (tuple), pat ja ir tikai viens parametrs, jābūt komatam
cursor.execute(sql, vertiba) # izpildām vaicājumu ar parametri
result = cursor.fetchall() # atgriež visus rezultātus kā sarakstu ar rindiņām, kur katra rindiņa ir tuplis ar kolonnas vērtībām
print(result) # izdruka iegūtos datus, lai pārliecinātos, ka vaicājums ir izpildīts veiksmīgi

# kā izdrukāt kolonnas nosaukumus?
# cursor.description atgriež informāciju par kolonnām, kur katrs elements ir tuplis ar kolonnas informāciju, un pirmā vērtība ir kolonnas nosaukums
kolonnas = [kolonna[0] for kolonna in cursor.description] # izveidojam sarakstu ar kolonnas nosaukumiem, izmantojot list comprehension
print(kolonnas) # izdruka kolonnas nosaukumus