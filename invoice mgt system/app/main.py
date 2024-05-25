from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .db import get_db, engine
from .model import Base, Invoice
from .schemas import InvoiceCreate, InvoiceUpdate, Invoice as InvoiceSchema
from .crud import get_invoice, get_invoices, create_invoice, update_invoice, delete_invoice

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/invoices/", response_model=InvoiceSchema)
def create_new_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    return create_invoice(db=db, invoice=invoice)

@app.get("/invoices/", response_model=List[InvoiceSchema])
def read_invoices(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    invoices = get_invoices(db, skip=skip, limit=limit)
    return invoices

@app.get("/invoices/{invoice_id}", response_model=InvoiceSchema)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

@app.put("/invoices/{invoice_id}", response_model=InvoiceSchema)
def update_existing_invoice(invoice_id: int, invoice: InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return update_invoice(db=db, invoice_id=invoice_id, invoice=invoice)

@app.delete("/invoices/{invoice_id}", response_model=InvoiceSchema)
def delete_existing_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = get_invoice(db, invoice_id=invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    delete_invoice(db=db, invoice_id=invoice_id)
    return db_invoice
