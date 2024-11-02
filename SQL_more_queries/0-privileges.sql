-- This SQL script retrieves the privileges of all users
SELECT 
    GRANTEE, 
    TABLE_CATALOG, 
    PRIVILEGE_TYPE 
FROM 
    information_schema.role_table_grants 
WHERE 
    GRANTEE != 'PUBLIC';
