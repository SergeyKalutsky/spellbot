from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from .db import Base


class Words(Base):

    __tablename__ = 'words'

    word = Column(String(200), primary_key=True, index=True)
    correct = Column(Integer)
    wrong = Column(Integer)