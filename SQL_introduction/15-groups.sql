-- Number by score
SELECT score, COUNT(*) AS Number
FROM second_table
GROUP BY score
ORDER BY number DESC;
