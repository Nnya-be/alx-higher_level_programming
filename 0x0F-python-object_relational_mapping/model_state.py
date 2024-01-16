#!/usr/bin/python3
"""
Contains the class definition for the state and an instance
Base=declarative_base().
"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String


Base = declarative_base()


class State(Base):
    """State Representations."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
