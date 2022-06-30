
from datetime import date
from unicodedata import name
from sqlalchemy import false, true, update
from sqlalchemy.orm import Session

#from . import models, schemas
import models
import schemas

'''
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
'''
# ---------------------------------
# These are my project crud
# ---------------------------------

#   Role CRUD


def create_role(db: Session, role: schemas.Role):
    db_role = models.Role(title=role.title)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_role(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()


def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()


def update_role(db: Session, role_id: int, updated_fields: schemas.Role):
    db.execute(
        update(models.Role)
        .where(models.Role.id == role_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def delete_role(db: Session, role: schemas.Role):
    db.delete(role)
    db.commit()

#   User CRUD


def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username,
                          password=user.password, role_id=user.role_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_userByCredenciales(db: Session, username: str, password: str):
    return db.query(models.User).filter(models.User.username == username, models.User.password == password).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, updated_fields: schemas.User):
    db.execute(
        update(models.User)
        .where(models.User.id == user_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()

#   Psychologist CRUD


def create_psychologist(db: Session, psychologist: schemas.Psychologist):
    db_psychologist = models.Psychologist(
        first_name=psychologist.first_name,
        last_name=psychologist.last_name,
        email=psychologist.email,
        user_id=psychologist.user_id)
    db.add(db_psychologist)
    db.commit()
    db.refresh(db_psychologist)
    return db_psychologist


def get_psychologist(db: Session, psychologist_id: int):
    return db.query(models.Psychologist).filter(models.Psychologist.id == psychologist_id).first()


def get_psychologistByUser(db: Session, user_id: int):
    return db.query(models.Psychologist).filter(models.Psychologist.user_id == user_id).first()


def get_psychologists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Psychologist).offset(skip).limit(limit).all()


def update_psychologist(db: Session, psychologist_id: int, updated_fields: schemas.Psychologist):
    db.execute(
        update(models.Psychologist)
        .where(models.Psychologist.id == psychologist_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def delete_psychologist(db: Session, psychologist: schemas.Psychologist):
    db.delete(psychologist)
    db.commit()


#   Patient CRUD

def create_patient(db: Session, patient: schemas.Patient):
    db_patient = models.Patient(
        first_name=patient.first_name,
        last_name=patient.last_name,
        gender=patient.gender,
        age=patient.age,
        level_of_education=patient.level_of_education,
        birthplace=patient.birthplace,
        phone=patient.phone,
        email=patient.email,
        user_id=patient.user_id,
        psychologist_id=patient.psychologist_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def get_patientByUser(db: Session, user_id: int):
    return db.query(models.Patient).filter(models.Patient.user_id == user_id).first()


def update_patient(db: Session, patient_id: int, updated_fields: schemas.Patient):
    db.execute(
        update(models.Patient)
        .where(models.Patient.id == patient_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def delete_patient(db: Session, patient: schemas.Patient):
    db.delete(patient)
    db.commit()

#   Depressive_Disorder CRUD


def create_depressive_disorder(db: Session, depressive_disorder: schemas.Depressive_Disorder):
    db_depressive_disorder = models.Depressive_Disorder(
        name=depressive_disorder.name,
        description=depressive_disorder.description,
        symptom=depressive_disorder.symptom,
        treatment=depressive_disorder.treatment)
    db.add(db_depressive_disorder)
    db.commit()
    db.refresh(db_depressive_disorder)
    return db_depressive_disorder


def get_depressive_disorder(db: Session, depressive_disorder_id: int):
    return db.query(models.Depressive_Disorder).filter(models.Depressive_Disorder.id == depressive_disorder_id).first()


def get_depressive_disorders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Depressive_Disorder).offset(skip).limit(limit).all()


def update_depressive_disorder(db: Session, depressive_disorder_id: int, updated_fields: schemas.Depressive_Disorder):
    db.execute(
        update(models.Depressive_Disorder)
        .where(models.Depressive_Disorder.id == depressive_disorder_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def update_test_Cancelar(db: Session, test_id: int, updated_fields: schemas.Test):
    db.execute(
        update(models.Test)
        .where(models.Test.id == test_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields


def delete_depressive_disorder(db: Session, depressive_disorder: schemas.Depressive_Disorder):
    db.delete(depressive_disorder)
    db.commit()


#   Pregunta Base CRUD

def create_pregunta_base(db: Session, pregunta_base: schemas.Pregunta_Base):
    db_pregunta_base = models.Pregunta_Base(
        description=pregunta_base.description)
    db.add(db_pregunta_base)
    db.commit()
    db.refresh(db_pregunta_base)
    return db_pregunta_base


def get_pregunta_base(db: Session, pregunta_base_id: int):
    return db.query(models.Pregunta_Base).filter(models.Pregunta_Base.id == pregunta_base_id).first()


def get_preguntas_base(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pregunta_Base).offset(skip).limit(limit).all()


'''def update_pregunta_base(db: Session, depressive_disorder_id: int, updated_fields: schemas.Depressive_Disorder):
    db.execute(
        update(models.Depressive_Disorder)
        .where(models.Depressive_Disorder.id == depressive_disorder_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields'''


def delete_pregunta_base(db: Session, pregunta_base: schemas.Pregunta_Base):
    db.delete(pregunta_base)
    db.commit()

#   Test CRUD


def create_test(db: Session, test: schemas.Test):
    db_test = models.Test(
        date=test.date,
        patient_id=test.patient_id,
        psychologist_id=test.psychologist_id,
        observation=test.observation,
        is_active=test.is_active)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test


def get_test(db: Session, test_id: int):
    return db.query(models.Test).filter(models.Test.id == test_id).first()


def get_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).offset(skip).limit(limit).all()

def get_testsActiveByUser(patient_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).filter(models.Test.is_active == 1 and models.Test.patient_id == patient_id  ).offset(skip).limit(limit).all()


def get_testsInactiveByUser(patient_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Test).filter( models.Test.is_active == 0 and models.Test.patient_id == patient_id ).offset(skip).limit(limit).all()


'''def update_test(db: Session, depressive_disorder_id: int, updated_fields: schemas.Depressive_Disorder):
    db.execute(
        update(models.Depressive_Disorder)
        .where(models.Depressive_Disorder.id == depressive_disorder_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields'''


def delete_test(db: Session, test: schemas.Test):
    db.delete(test)
    db.commit()

#   Pregunta test CRUD

def create_pregunta_test(db: Session, pregunta_test: schemas.Pregunta_Test):
    db_pregunta_test = models.Pregunta_Test(
        date=pregunta_test.date,
        test_id=pregunta_test.test_id,
        pregunta_base_id=pregunta_test.pregunta_base_id,
        rpta=pregunta_test.rpta,
        is_active=pregunta_test.is_active)
    db.add(db_pregunta_test)
    db.commit()
    db.refresh(db_pregunta_test)
    return db_pregunta_test


def get_pregunta_test(db: Session, pregunta_test_id: int):
    return db.query(models.Pregunta_Test).filter(models.Pregunta_Test.id == pregunta_test_id).first()


def get_pregunta_tests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pregunta_Test).offset(skip).limit(limit).all()

def delete_pregunta_test(db: Session, pregunta_test: schemas.Pregunta_Test):
    db.delete(pregunta_test)
    db.commit()


#   Diagnostic_Report   CRUD



def create_diagnostic_report(db: Session, diagnostic_report: schemas.Diagnostic_Report):
    db_diagnostic_report = models.Diagnostic_Report(
        date=diagnostic_report.date,
        test_id=diagnostic_report.test_id,
        depressive_disorder_id=diagnostic_report.depressive_disorder_id)
    db.add(db_diagnostic_report)
    db.commit()
    db.refresh(db_diagnostic_report)
    return db_diagnostic_report


def get_diagnostic_report(db: Session, diagnostic_report_id: int):
    return db.query(models.Diagnostic_Report).filter(models.Diagnostic_Report.id == diagnostic_report_id).first()


def get_diagnostic_reports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Diagnostic_Report).offset(skip).limit(limit).all()

def get_diagnostic_reportsByTestId(test_id: int, db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Diagnostic_Report).filter(models.Diagnostic_Report.test_id == test_id).offset(skip).limit(limit).all()

def delete_diagnostic_report(db: Session, diagnostic_report: schemas.Diagnostic_Report):
    db.delete(diagnostic_report)
    db.commit()








# anterior diagnostic report


'''def create_diagnostic_report(db: Session, diagnostic_report: schemas.Diagnostic_Report, psychologist_id: int, patient_id: int, depressive_disorder_id: int):
    db_diagnostic_report = models.Diagnostic_Report(
        psychologist_id=psychologist_id, 
        patient_id=patient_id,
        depressive_disorder=depressive_disorder_id)
    db.add(db_diagnostic_report)
    db.commit()
    db.refresh(db_diagnostic_report)
    return db_diagnostic_report

def get_diagnostic_report(db: Session, diagnostic_report_id: int):
    return db.query(models.Diagnostic_Report).filter(models.Diagnostic_Report.id == diagnostic_report_id).first()

def get_diagnostic_reports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Diagnostic_Report).offset(skip).limit(limit).all()

def update_diagnostic_report(db: Session, diagnostic_report_id: int, updated_fields: schemas.Diagnostic_Report):
    db.execute(
        update(models.Diagnostic_Report)
        .where(models.Diagnostic_Report.id == diagnostic_report_id)
        .values(updated_fields.dict(exclude_unset=True))
    )
    db.flush()
    db.commit()
    return updated_fields

def delete_diagnostic_report(db: Session, diagnostic_report: schemas.Diagnostic_Report):
    db.delete(diagnostic_report)
    db.commit()'''
