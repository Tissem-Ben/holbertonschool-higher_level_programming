#!/usr/bin/python3
"""Script to print the first State object from the database"""

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
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'
    )

    # Create a sessionmaker and bind it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object ordered by id, or None if no state exists
    first_state = session.query(State).order_by(State.id).first()

    # Check if a result was returned, and print it
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
