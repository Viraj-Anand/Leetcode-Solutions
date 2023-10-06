SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM (
        SELECT num, COUNT(*) AS count
        FROM MyNumbers
        GROUP BY num
    ) AS Counts
    WHERE count = 1
) AS SingleNumbers;
