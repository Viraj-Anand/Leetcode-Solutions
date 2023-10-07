SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs a
JOIN Logs b ON a.id = b.id - 1
JOIN Logs c ON a.id = c.id - 2
WHERE a.num = b.num AND b.num = c.num;
