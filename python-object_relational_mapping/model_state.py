#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create the Base instance
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Example of engine creation (not part of the required script, but useful for reference)
# engine = create_engine('mysql+mysqldb://<username>:<password>@localhost:3306/<database_name>')
# Base.metadata.create_all(engine)
