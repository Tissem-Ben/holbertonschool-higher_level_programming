-- This script lists all records with a name in second_table in the hbtn_0c_0 database
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
