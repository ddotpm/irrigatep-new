from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ....app import models, schemas
from ....app.deps import get_db
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=schemas.Part)
def create_part(part: schemas.PartCreate, db: Session = Depends(get_db)):
    db_part = models.Part(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

@router.get("/", response_model=List[schemas.Part])
def read_parts(
    skip: int = 0,
    limit: int = 100,
    manufacturer: Optional[str] = None,
    low_stock: Optional[bool] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Part)
    if manufacturer:
        query = query.filter(models.Part.manufacturer == manufacturer)
    if low_stock:
        query = query.filter(models.Part.quantity_in_stock <= models.Part.reorder_point)
    return query.offset(skip).limit(limit).all()

@router.get("/{part_id}", response_model=schemas.Part)
def read_part(part_id: int, db: Session = Depends(get_db)):
    db_part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return db_part

@router.put("/{part_id}", response_model=schemas.Part)
def update_part(
    part_id: int,
    part: schemas.PartUpdate,
    db: Session = Depends(get_db)
):
    db_part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    
    for field, value in part.dict(exclude_unset=True).items():
        setattr(db_part, field, value)
    
    db.commit()
    db.refresh(db_part)
    return db_part

@router.delete("/{part_id}")
def delete_part(part_id: int, db: Session = Depends(get_db)):
    db_part = db.query(models.Part).filter(models.Part.id == part_id).first()
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    
    db.delete(db_part)
    db.commit()
    return {"message": "Part deleted successfully"}

@router.get("/low-stock/", response_model=List[schemas.Part])
def get_low_stock_parts(db: Session = Depends(get_db)):
    return db.query(models.Part).filter(
        models.Part.quantity_in_stock <= models.Part.reorder_point
    ).all() 