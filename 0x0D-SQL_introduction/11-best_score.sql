-- List all records with a score >= 10 in descending order
-- SELECT score, name FROM second_table ORDER BY score >= 10 DESC;
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
