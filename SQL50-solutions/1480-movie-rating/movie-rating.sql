(SELECT name AS results
FROM Users u
JOIN MovieRating mr ON u.user_id = mr.user_id
GROUP BY u.user_id, name
ORDER BY COUNT(mr.movie_id) DESC, name
LIMIT 1
)
union all
(SELECT title AS results
FROM Movies m
JOIN MovieRating mr ON m.movie_id = mr.movie_id
WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
GROUP BY m.movie_id, title
ORDER BY AVG(rating) DESC, title
LIMIT 1)
