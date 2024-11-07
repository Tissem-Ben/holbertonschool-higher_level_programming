#!/usr/bin/python3
"""Script to update a state in the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine to connect to MySQL
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost:3306/{database_name}'
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the state with id=2 and update its name
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
