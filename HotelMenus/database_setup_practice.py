import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employee'
    name = Column(String(250), nullable=False)
    id = Column(Integer, primary_key=True)

class Address(Base):
    __tablename__ = 'address'
    street = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    zip = Column(String(5), nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship(Employee)


#at end of file
engine = create_engine('sqlite:///employeData.db')
Base.metadata.create_all(engine)