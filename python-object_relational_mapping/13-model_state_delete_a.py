#!/usr/bin/python3
"""shebang script"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture les arguments de la ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Créer l'engine pour se connecter à MySQL
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
    )

    # Créer une session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Supprimer tous les états qui contiennent la lettre "a"
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()

    # Supprimer les états trouvés
    for state in states_to_delete:
        session.delete(state)

    # Commiter les changements dans la base de données
    session.commit()

    # Fermer la session
    session.close()
