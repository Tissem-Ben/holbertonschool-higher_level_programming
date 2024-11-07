#!/usr/bin/python3
"""Script to fetch cities by state from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Arguments for MySQL username, password and database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database using SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch all cities along with their states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print cities in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
