#!/usr/bin/env python3
''' Task 0 module '''
from sqlalchemy import Column, String, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    ''' creates a table for user '''
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250), nullable=True)
    restore_token = Column(VARCHAR(250), nullable=True)
