#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture command-line arguments for MySQL credentials and database name
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create an engine to connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
    )

    # Create a sessionmaker and bind it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the 'State' table for states that contain the letter 'a'
    # and order the results by 'id'
    states = session.query(State).filter(State.name.like('%a%')) \
        .order_by(State.id).all()

    # Loop through the states and print their 'id' and 'name'
    if states:
        for state in states:
            print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session to free up resources
    session.close()
