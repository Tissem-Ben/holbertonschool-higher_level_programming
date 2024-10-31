-- This script lists all the tables in a specified database
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'my_database'
