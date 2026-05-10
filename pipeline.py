# IMPORT LIBRARIES
import requests
import pandas as pd
import pyodbc
from config import API_KEY, BASE_URL

# EXTRACT
url = f"{BASE_URL}/movie/popular?api_key={API_KEY}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    movies = data["results"]

    # TRANSFORM
    df = pd.DataFrame(movies)
    df = df[["title", "release_date", "popularity"]]
    df = df.drop_duplicates()
    df["title"] = df["title"].str.strip()
    df = df.dropna(subset=["release_date", "popularity"])
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df = df[df["popularity"] > 0]
    df["popularity"] = df["popularity"].round(2)

    print("\n📊 Dados organizados:")
    print(df.head())

    # LOAD
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=.\\SQLEXPRESS;"
        "DATABASE=TMDB;"
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO Movies (title, release_date, popularity)
            VALUES (?, ?, ?)
        """, row["title"], row["release_date"], row["popularity"])

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Dados carregados no SQL Server com sucesso!")

else:
    print("❌ Erro:", response.status_code)