from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ....app import models, schemas
from ....app.deps import get_db
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=schemas.Invoice)
def create_invoice(invoice: schemas.InvoiceCreate, db: Session = Depends(get_db)):
    # Verify client and project exist
    client = db.query(models.Client).filter(models.Client.id == invoice.client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    project = db.query(models.Project).filter(models.Project.id == invoice.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db_invoice = models.Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@router.get("/", response_model=List[schemas.Invoice])
def read_invoices(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    client_id: Optional[int] = None,
    project_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Invoice)
    if status:
        query = query.filter(models.Invoice.status == status)
    if client_id:
        query = query.filter(models.Invoice.client_id == client_id)
    if project_id:
        query = query.filter(models.Invoice.project_id == project_id)
    return query.offset(skip).limit(limit).all()

@router.get("/{invoice_id}", response_model=schemas.Invoice)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

@router.put("/{invoice_id}", response_model=schemas.Invoice)
def update_invoice(
    invoice_id: int,
    invoice: schemas.InvoiceUpdate,
    db: Session = Depends(get_db)
):
    db_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    for field, value in invoice.dict(exclude_unset=True).items():
        setattr(db_invoice, field, value)
    
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

@router.delete("/{invoice_id}")
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    
    db.delete(db_invoice)
    db.commit()
    return {"message": "Invoice deleted successfully"}

@router.get("/client/{client_id}", response_model=List[schemas.Invoice])
def get_client_invoices(client_id: int, db: Session = Depends(get_db)):
    return db.query(models.Invoice).filter(models.Invoice.client_id == client_id).all()

@router.get("/project/{project_id}", response_model=List[schemas.Invoice])
def get_project_invoices(project_id: int, db: Session = Depends(get_db)):
    return db.query(models.Invoice).filter(models.Invoice.project_id == project_id).all() 