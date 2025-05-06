from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from .database import Base

class ProjectStatus(enum.Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)
    address = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Boolean, default=True)  # active/inactive

    projects = relationship("Project", back_populates="client")
    invoices = relationship("Invoice", back_populates="client")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    name = Column(String, index=True)
    description = Column(Text)
    start_date = Column(DateTime(timezone=True))
    end_date = Column(DateTime(timezone=True))
    status = Column(Enum(ProjectStatus))
    location = Column(String)
    total_area = Column(Float)
    project_type = Column(String)  # residential/commercial/agricultural
    budget = Column(Float)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    client = relationship("Client", back_populates="projects")
    work_orders = relationship("WorkOrder", back_populates="project")
    invoices = relationship("Invoice", back_populates="project")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String)
    contact_info = Column(String)
    certification = Column(String)
    hire_date = Column(DateTime(timezone=True))
    status = Column(Boolean, default=True)  # active/inactive
    hourly_rate = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    work_orders = relationship("WorkOrder", back_populates="employee")

class Equipment(Base):
    __tablename__ = "equipment"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    model = Column(String)
    manufacturer = Column(String)
    purchase_date = Column(DateTime(timezone=True))
    status = Column(Boolean, default=True)  # available/in_use
    maintenance_schedule = Column(String)
    last_maintenance_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    maintenance_records = relationship("MaintenanceSchedule", back_populates="equipment")

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    manufacturer = Column(String)
    model = Column(String)
    unit_price = Column(Float)
    quantity_in_stock = Column(Integer)
    reorder_point = Column(Integer)
    supplier_info = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    amount = Column(Float)
    issue_date = Column(DateTime(timezone=True))
    due_date = Column(DateTime(timezone=True))
    status = Column(String)  # pending/paid/overdue
    payment_terms = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project", back_populates="invoices")
    client = relationship("Client", back_populates="invoices")

class WorkOrder(Base):
    __tablename__ = "work_orders"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    description = Column(Text)
    status = Column(String)  # pending/in_progress/completed
    scheduled_date = Column(DateTime(timezone=True))
    completion_date = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    project = relationship("Project", back_populates="work_orders")
    employee = relationship("Employee", back_populates="work_orders")

class MaintenanceSchedule(Base):
    __tablename__ = "maintenance_schedules"

    id = Column(Integer, primary_key=True, index=True)
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    last_maintenance = Column(DateTime(timezone=True))
    next_maintenance = Column(DateTime(timezone=True))
    maintenance_type = Column(String)
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    equipment = relationship("Equipment", back_populates="maintenance_records") 