#!/usr/bin/python3
"""Lists all State objecgts that contain letter a from hbtn_0e_6_usa db."""


import sqlalchemy
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    usr, pas, db = argv[1], argv[2], argv[3]
    engine = create_engine(f"mysql+mysqldb://{usr}:{pas}@localhost:3306/{db}",
                           poop_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_a = session.query(State).filter(State.name.like('%a%')).
    order_by(State.id).all()
    for state in state_a:
        print(f"{state.id}: {state.name}")

    session.close()
