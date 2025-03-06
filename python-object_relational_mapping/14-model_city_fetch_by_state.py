#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Get MySQL credentials from arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and bind it to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects sorted by id, joining with State
    cities = session.query(City).join(State).order_by(City.id).all()

    # Print results
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
