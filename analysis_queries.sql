


---------------------------
-- ANALYSIS QUERIES
-- TMDB Movie Data Pipeline
---------------------------

-- top 10 most popular movies
SELECT TOP 10
title, 
popularity
FROM Movies
ORDER BY popularity DESC



--Total movies by year
SELECT
	YEAR (release_date) AS years,
	COUNT (*) AS total_movies
FROM Movies
GROUP BY YEAR (release_date)
ORDER BY years DESC


--Average popularity by year
SELECT
	YEAR(release_date) AS years,
	ROUND(AVG(popularity), 2) AS popularity_avg
FROM Movies
GROUP BY YEAR(release_date)
ORDER BY popularity_avg DESC
