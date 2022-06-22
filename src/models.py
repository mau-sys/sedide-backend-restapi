from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#from .database import Base
from database import Base

'''
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
'''
# ---------------------------------
# These are my project models
# ---------------------------------

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    title = Column(String(20))

    users = relationship("User", backref="role")


class User(Base):
    __tablename__= "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(String(10))
    is_active = Column(Boolean, default=True)
    
    role_id = Column(Integer, ForeignKey("role.id"))

    psychologists = relationship("Psychologist", backref="user")
    patients = relationship("Patient", backref="user")


class Psychologist(Base):
    __tablename__ = "psychologist"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(60))
    last_name = Column(String(60))
    email = Column(String(50))

    user_id = Column(Integer, ForeignKey("user.id"))

    patients = relationship("Patient", backref="psychologist")
    diagnostic_reports = relationship("Diagnostic_Report", backref="psychologist")


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(60))
    last_name = Column(String(60))
    gender = Column(String(9))
    age = Column(Integer)
    level_of_education = Column(String(30))
    birthplace = Column(String(50))
    phone = Column(String(12))
    email = Column(String(50))

    user_id = Column(Integer, ForeignKey("user.id"))
    psychologist_id = Column(Integer, ForeignKey("psychologist.id"))

    diagnostic_reports = relationship("Diagnostic_Report", backref="patient")


class Depressive_Disorder(Base):
    __tablename__= "depressive_disorder"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(900))
    symptom = Column(String(900))
    treatment = Column(String(900))

    diagnostic_reports = relationship("Diagnostic_Report", backref="depressive_disorder")


class Diagnostic_Report(Base):
    __tablename__ = "diagnostic_report"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=datetime.now())

    psychologist_id = Column(Integer, ForeignKey("psychologist.id"))
    patient_id = Column(Integer, ForeignKey("patient.id"))
    depressive_disorder_id = Column(Integer, ForeignKey("depressive_disorder.id"))