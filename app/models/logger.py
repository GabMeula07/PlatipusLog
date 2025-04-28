from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import  relationship
import uuid

Base = declarative_base()

class LoggerModel(Base):
    __tablename__ = 'logger'  

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    logs = relationship("Log", back_populates="logger") 


class Log(Base): 

    __tablename__ = 'log'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    date = Column(DateTime, nullable=False)
    message = Column(Text(), nullable=False)
    
    logger_id = Column(String(36), ForeignKey('logger.id'), nullable=False)  
    logger = relationship("LoggerModel", back_populates="logs") 
