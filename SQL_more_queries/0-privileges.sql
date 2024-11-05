-- Check user privileges for user_0d_1 and user_0d_2
SELECT user, host, privilege FROM information_schema.user_privileges
WHERE user IN ('user_0d_1', 'user_0d_2')
ORDER BY user, host;

-- Create user_0d_1 with all privileges if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
