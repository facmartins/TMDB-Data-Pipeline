
# 🎬 TMDB Movie Data Pipeline
An ETL data engineering project that extracts popular movie data from the TMDB API, transforms and cleans it using Python, and loads it into SQL Server for analysis.

---

## 🛠️ Technologies
- Python 3.14
- Pandas
- Requests
- PyODBC
- SQL Server
- TMDB API

---

## 🏗️ Pipeline Architecture
TMDB API → Extract → Transform → Load → SQL Server

---

## 📋 Requirements Specification

### Objective
Build an ETL pipeline that extracts popular movie data from the TMDB API, transforms and cleans it, and loads it into SQL Server for analysis.

### Data Source
- API: The Movie Database (TMDB)
- Endpoint: /movie/popular
- Format: JSON
- Frequency: Manual

### Functional Requirements
- Extract the most popular movies from the API
- Remove duplicate and missing data
- Convert dates to correct format
- Load data into SQL Server
- Enable analysis via SQL queries

### Business Rules
- Remove movies without release date
- Remove movies with popularity ≤ 0
- Popularity rounded to 2 decimal places

---

## 📁 Project Structure
├── pipeline.py           # ETL pipeline
├── config.py             # API credentials (not included)
├── create_tables.sql     # SQL Server table creation
├── analysis_queries.sql  # SQL analysis queries
└── README.md             # Project documentation

---

## 📊 SQL Analysis

### Top 10 Most Popular Movies
SELECT TOP 10 title, popularity
FROM Movies
ORDER BY popularity DESC

### Total Movies by Year
SELECT 
    YEAR(release_date) AS year,
    COUNT(*) AS total_movies
FROM Movies
GROUP BY YEAR(release_date)
ORDER BY year DESC

### Average Popularity by Year
SELECT 
    YEAR(release_date) AS year,
    ROUND(AVG(popularity), 2) AS avg_popularity
FROM Movies
GROUP BY YEAR(release_date)
ORDER BY avg_popularity DESC

---

## ⚙️ How to Run
1. Clone the repository
2. Install dependencies:
pip install pandas requests pyodbc

3. Create a config.py file with your credentials:
API_KEY = "your_tmdb_api_key"
BASE_URL = "https://api.themoviedb.org/3"

4. Create the database and tables using create_tables.sql
5. Run the pipeline:
python pipeline.py

---

## 👩‍💻 Author
Flávia de Castro | Data Engineering Student
Portugal 🇵🇹
[LinkedIn](https://www.linkedin.com/in/flaviadecastroprojects)