# LOAD — carregar dados para o SQL Server
from pipeline import df
import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=TMDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
           INSERT INTO Filmes (title, release_date, popularity)
           VALUES (?, ?, ?)
       """, row["title"], row["release_date"], row["popularity"])

conn.commit()
cursor.close()
conn.close()

print("✅ Dados carregados no SQL Server com sucesso!")