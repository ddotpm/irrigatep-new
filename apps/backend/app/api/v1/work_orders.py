from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ....app import models, schemas
from ....app.deps import get_db
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=schemas.WorkOrder)
def create_work_order(work_order: schemas.WorkOrderCreate, db: Session = Depends(get_db)):
    # Verify project and employee exist
    project = db.query(models.Project).filter(models.Project.id == work_order.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    employee = db.query(models.Employee).filter(models.Employee.id == work_order.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    db_work_order = models.WorkOrder(**work_order.dict())
    db.add(db_work_order)
    db.commit()
    db.refresh(db_work_order)
    return db_work_order

@router.get("/", response_model=List[schemas.WorkOrder])
def read_work_orders(
    skip: int = 0,
    limit: int = 100,
    status: Optional[str] = None,
    project_id: Optional[int] = None,
    employee_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.WorkOrder)
    if status:
        query = query.filter(models.WorkOrder.status == status)
    if project_id:
        query = query.filter(models.WorkOrder.project_id == project_id)
    if employee_id:
        query = query.filter(models.WorkOrder.employee_id == employee_id)
    return query.offset(skip).limit(limit).all()

@router.get("/{work_order_id}", response_model=schemas.WorkOrder)
def read_work_order(work_order_id: int, db: Session = Depends(get_db)):
    db_work_order = db.query(models.WorkOrder).filter(models.WorkOrder.id == work_order_id).first()
    if db_work_order is None:
        raise HTTPException(status_code=404, detail="Work order not found")
    return db_work_order

@router.put("/{work_order_id}", response_model=schemas.WorkOrder)
def update_work_order(
    work_order_id: int,
    work_order: schemas.WorkOrderUpdate,
    db: Session = Depends(get_db)
):
    db_work_order = db.query(models.WorkOrder).filter(models.WorkOrder.id == work_order_id).first()
    if db_work_order is None:
        raise HTTPException(status_code=404, detail="Work order not found")
    
    for field, value in work_order.dict(exclude_unset=True).items():
        setattr(db_work_order, field, value)
    
    db.commit()
    db.refresh(db_work_order)
    return db_work_order

@router.delete("/{work_order_id}")
def delete_work_order(work_order_id: int, db: Session = Depends(get_db)):
    db_work_order = db.query(models.WorkOrder).filter(models.WorkOrder.id == work_order_id).first()
    if db_work_order is None:
        raise HTTPException(status_code=404, detail="Work order not found")
    
    db.delete(db_work_order)
    db.commit()
    return {"message": "Work order deleted successfully"}

@router.get("/project/{project_id}", response_model=List[schemas.WorkOrder])
def get_project_work_orders(project_id: int, db: Session = Depends(get_db)):
    return db.query(models.WorkOrder).filter(models.WorkOrder.project_id == project_id).all()

@router.get("/employee/{employee_id}", response_model=List[schemas.WorkOrder])
def get_employee_work_orders(employee_id: int, db: Session = Depends(get_db)):
    return db.query(models.WorkOrder).filter(models.WorkOrder.employee_id == employee_id).all() 