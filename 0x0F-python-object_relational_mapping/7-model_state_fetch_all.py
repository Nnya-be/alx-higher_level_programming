#!/usr/bin/python3
"""Lists all state objects from the databse hbtn_0e_6_usa."""
import sqlalchemy
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    usr, pas, db = argv[1], argv[2], argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pas}@localhost:3306/{db}",
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
