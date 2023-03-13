-- lists all records with a score >= 10 in the table second_table, display both the score (ordered by score (top first)) and the name
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;