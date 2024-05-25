from pydantic import BaseModel
from datetime import datetime

class InvoiceBase(BaseModel):
    number: str
    amount: float
    status: str
    date: datetime

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(BaseModel):
    number: str = None
    amount: float = None
    status: str = None
    date: datetime = None

class Invoice(InvoiceBase):
    id: int

    class Config:
        from_attributes = True


