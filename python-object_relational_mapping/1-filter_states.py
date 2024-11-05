#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments de connexion
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Création d'un curseur pour exécuter des requêtes
    cursor = db.cursor()

    # Exécution de la requête pour sélectionner les états dont le nom commence par 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    )

    # Récupération et affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
