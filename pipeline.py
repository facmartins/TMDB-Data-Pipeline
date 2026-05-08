# IMPORTAR BIBLIOTECAS
import requests
import pandas as pd
from config import API_KEY, BASE_URL

# URL DA API
url = f"{BASE_URL}/movie/popular?api_key={API_KEY}"

# PEDIR DADOS À API
response = requests.get(url)

# VERIFICAR SE FUNCIONOU
if response.status_code == 200:
    data = response.json()
    movies = data["results"]

    # TRANSFORM
    df = pd.DataFrame(movies)

    # Filtrar colunas
    df = df[["title", "release_date", "popularity"]]

    # Limpar/transformar os dados
    df = df.drop_duplicates()
    df["title"] = df["title"].str.strip()
    df = df.dropna(subset=["release_date", "popularity"])
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df = df[df["popularity"] > 0]
    df["popularity"] = df["popularity"].round(2)

    print("\n📊 Dados organizados:")
    print(df.head())

    print("✅ Sucesso! Filmes recebidos:\n")

    for movie in movies[:3]:
        print("Título:", movie["title"])
        print("Data:", movie["release_date"])
        print("Popularidade:", movie["popularity"])
        print("-" * 30)

else:
    print("❌ Erro:", response.status_code)