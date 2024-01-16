#!/usr/bin/python3
"""
Contains the class definition for the state and an instance
Base=declarative_base().
"""
import sqlalchemy
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()
class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == '__main__':
    user, password, db=sys.argv[1], sys.argv[2], sys.argv[3]
    
    engine = create_engine(f"mysql://{user}:{password}@localhost:3306/{db}")

    Base.metadata.create_all(engine)
