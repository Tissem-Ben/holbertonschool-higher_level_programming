### Contenu du fichier `0-privileges.sql`

Le fichier `0-privileges.sql` doit contenir les instructions SQL nécessaires pour créer les utilisateurs (s'ils n'existent pas déjà) et récupérer leurs privilèges. Voici un exemple de contenu :

```sql
-- Create users if they do not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Display the privileges of user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
