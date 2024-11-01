-- This script lists all records from the second_table with a score >= 10
-- in the database hbtn_0c_0, ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
