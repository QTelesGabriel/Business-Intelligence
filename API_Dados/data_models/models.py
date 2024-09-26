from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created = Column(DateTime)

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    updated = Column(DateTime)
    task = Column(String)
    priority = Column(String)
    status = Column(String)
    userID = Column(Integer, ForeignKey("user.id"))
    user = relationship('User')
