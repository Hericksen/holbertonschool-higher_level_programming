#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and state name from arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create the engine and bind it to the database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the state with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
