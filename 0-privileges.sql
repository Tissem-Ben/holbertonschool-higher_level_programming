-- 0-privileges.sql
-- Grant privileges to Tissem

-- Step 1: Grant read access to the entire database
GRANT SELECT ON *.* TO 'Tissem'@'localhost';

-- Step 2: Grant read and write access to a specific database
GRANT SELECT, INSERT, UPDATE, DELETE ON `hbtn_0c_0`.* TO 'Tissem'@'localhost';

-- Step 3: Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;

-- Optional: Show grants for the user
SHOW GRANTS FOR 'Tissem'@'localhost';

