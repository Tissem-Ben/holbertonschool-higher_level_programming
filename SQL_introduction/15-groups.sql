-- This script lists the number of records with the same score in second_table in the hbtn_0c_0 database
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
