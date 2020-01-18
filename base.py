from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date

Base = declarative_base()

class BodyPartTpl(Base):
    __tablename__ = 'bodyPartTpl'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name