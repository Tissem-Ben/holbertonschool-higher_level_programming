-- This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server
SELECT 
    GRANTEE, 
    TABLE_CATALOG, 
    PRIVILEGE_TYPE 
FROM 
    information_schema.role_table_grants 
WHERE 
    GRANTEE IN ('user_0d_1', 'user_0d_2');

