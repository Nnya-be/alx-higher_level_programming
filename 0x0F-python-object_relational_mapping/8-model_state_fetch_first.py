#!/usr/bin/python3
"""Prints the first State object from the hbtn_0e_6_usa db."""
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    usr, pas, db = argv[1], argv[2], argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pas}@localhost:3306/{db}",
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}, {first_state.name}")
    else:
        print("Nothing")

    session.close()
