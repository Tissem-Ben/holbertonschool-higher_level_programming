#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost",  # Ajout de la virgule ici
        user=username,     # Ajout de la virgule ici
        passwd=password,   # Ajout de la virgule ici
        db=db_name         # Ajout de la virgule ici
    )
    cursor = db.cursor()

    # Exécution de la requête SQL
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "INNER JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )

    # Récupérer les résultats et les afficher
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture de la connexion
    cursor.close()
    db.close()
