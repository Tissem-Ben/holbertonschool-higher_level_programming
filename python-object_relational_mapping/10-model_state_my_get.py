#!/usr/bin/python3
"""shebang script"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupérer les arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Diviser l'URL de connexion en plusieurs parties
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:'
        f'{mysql_password}@localhost:3306/{database_name}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Rechercher l'état avec le nom donné
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
