from sqlalchemy import Column, Integer, String, Float, DateTime
from .db import Base

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String, unique=True, index=True, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
