#!/usr/bin/python3
"""Define the State class linked to the states table in MySQL"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Création de la base déclarative
Base = declarative_base()


class State(Base):
    """Links to the 'states' table in the database."""

    __tablename__ = 'states'  # Nom de la table dans la base de données

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
