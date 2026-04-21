from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Nation(Base):
    __tablename__ = "nations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    confederation = Column(String, nullable=False)
    group_name = Column(String, nullable=False)
    fifa_rank = Column(Integer, nullable=True)

    players = relationship("Player", back_populates="nation")

class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String, nullable=False)
    jersey_number = Column(Integer, nullable=False)
    nation_id = Column(Integer, ForeignKey("nations.id"), nullable=False)

    nation = relationship("Nation", back_populates="players")