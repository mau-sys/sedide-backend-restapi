from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

#from . import crud, models, schemas
#from .database import SessionLocal, engine

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

'''
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

'''
#-----------------------------------------
#   THESE ARE FROM MY PROJECT
#-----------------------------------------

@app.get("/")
def hello_world():
    return "helloWorld"

@app.get("/roles/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="User not found")
    return role

@app.get("/roles/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles

@app.post("/roles/", response_model=schemas.Role)
def create_role(role: schemas.Role, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    return crud.create_role(db=db, role=role)

@app.patch("/roles/{role_id}", response_model = schemas.Role)
def update_role(
    role_id: int,
    updated_fields: schemas.Role,
    db: Session = Depends(get_db),
):
    return crud.update_role(db, role_id, updated_fields)

@app.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id)
    return crud.delete_role(db=db, role=role)

#-------------------
# USER HTTP REQUESTS
#-------------------

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    return user

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.post("/users/{role_id}", response_model=schemas.User)
def create_user(user: schemas.User, role_id: int, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_user(db=db, user=user, role_id=role_id)

@app.patch("/users/{user_id}", response_model = schemas.User)
def update_user(
    user_id: int,
    updated_fields: schemas.User,
    db: Session = Depends(get_db),
):
    return crud.update_user(db, user_id, updated_fields)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    return crud.delete_user(db=db, user=user)


#---------------------------
# PSYCHOLOGIST HTTP REQUESTS
#---------------------------


@app.get("/psychologists/{psychologist_id}", response_model=schemas.Psychologist)
def read_psychologist(psychologist_id: int, db: Session = Depends(get_db)):
    db_psychologist = crud.get_psychologist(db, psychologist_id=psychologist_id)
    return db_psychologist

@app.get("/psychologists/", response_model=list[schemas.Psychologist])
def read_psychologists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    psychologists = crud.get_psychologists(db, skip=skip, limit=limit)
    return psychologists

@app.post("/psychologists/{user_id}", response_model=schemas.Psychologist)
def create_psychologist(psychologist: schemas.Psychologist, user_id: int, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_psychologist(db=db, psychologist=psychologist, user_id=user_id)

@app.patch("/psychologists/{psychologist_id}", response_model = schemas.Psychologist)
def update_psychologist(
    psychologist_id: int,
    updated_fields: schemas.Psychologist,
    db: Session = Depends(get_db),
):
    return crud.update_psychologist(db, psychologist_id, updated_fields)

@app.delete("/psychologists/{psychologist_id}")
def delete_psychologist(psychologist_id: int, db: Session = Depends(get_db)):
    psychologist = crud.get_psychologist(db, psychologist_id)
    return crud.delete_psychologist(db=db, psychologist=psychologist)


#---------------------------
# PATIENT HTTP REQUESTS
#---------------------------


@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id=patient_id)
    return patient

@app.get("/patients/", response_model=list[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients

@app.post("/patients/{user_id}/{psychologist_id}/", response_model=schemas.Patient)
def create_patient(patient: schemas.Patient, user_id: int, psychologist_id: int, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_patient(db=db, patient=patient, user_id=user_id, psychologist_id=psychologist_id)

@app.patch("/patients/{patient_id}", response_model = schemas.Patient)
def update_patient(
    patient_id: int,
    updated_fields: schemas.Patient,
    db: Session = Depends(get_db),
):
    return crud.update_patient(db, patient_id, updated_fields)

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    return crud.delete_patient(db=db, patient=patient)

#----------------------------------
# DEPRESSIVE DISORDER HTTP REQUESTS
#----------------------------------

@app.get("/depressive_disorders/{depressive_disorder_id}", response_model=schemas.Depressive_Disorder)
def read_depressive_disorder(depressive_disorder_id: int, db: Session = Depends(get_db)):
    depressive_disorder = crud.get_depressive_disorder(db, depressive_disorder_id=depressive_disorder_id)
    return depressive_disorder

@app.get("/depressive_disorders/", response_model=list[schemas.Depressive_Disorder])
def read_depressive_disorders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    depressive_disorders = crud.get_depressive_disorders(db, skip=skip, limit=limit)
    return depressive_disorders

@app.post("/depressive_disorders/", response_model=schemas.Depressive_Disorder)
def create_depressive_disorder(depressive_disorder: schemas.Depressive_Disorder, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_depressive_disorder(db=db, depressive_disorder=depressive_disorder)

@app.patch("/depressive_disorders/{depressive_disorder_id}", response_model = schemas.Depressive_Disorder)
def update_depressive_disorder(
    depressive_disorder_id: int,
    updated_fields: schemas.Depressive_Disorder,
    db: Session = Depends(get_db),
):
    return crud.update_depressive_disorder(db, depressive_disorder_id, updated_fields)

@app.delete("/depressive_disorders/{depressive_disorder_id}")
def delete_depressive_disorder(depressive_disorder_id: int, db: Session = Depends(get_db)):
    depressive_disorder = crud.get_depressive_disorder(db, depressive_disorder_id)
    return crud.delete_depressive_disorder(db=db, patient=depressive_disorder)


#----------------------------------
# DIAGNOSTIC REPORT HTTP REQUESTS
#----------------------------------



@app.get("/diagnostic_reports/{diagnostic_report_id}", response_model=schemas.Diagnostic_Report)
def read_diagnostic_report(diagnostic_report_id: int, db: Session = Depends(get_db)):
    diagnostic_report = crud.get_psychologist(db, diagnostic_report_id=diagnostic_report_id)
    return diagnostic_report

@app.get("/diagnostic_reports/", response_model=list[schemas.Diagnostic_Report])
def read_diagnostic_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diagnostic_reports = crud.get_diagnostic_reports(db, skip=skip, limit=limit)
    return diagnostic_reports

@app.post("/diagnostic_reports/{psychologist_id}/{patient_id}/{depressive_disorder_id}", response_model=schemas.Diagnostic_Report)
def create_diagnostic_report(diagnostic_report: schemas.Diagnostic_Report, psychologist_id: int, patient_id: int, depressive_disorder_id: int, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_patient(db=db, diagnostic_report=diagnostic_report, psychologist_id=psychologist_id, patient_id=patient_id, depressive_disorder_id=depressive_disorder_id)

@app.patch("/diagnostic_reports/{diagnostic_report_id}", response_model = schemas.Diagnostic_Report)
def update_diagnostic_report(
    diagnostic_report_id: int,
    updated_fields: schemas.Patient,
    db: Session = Depends(get_db),
):
    return crud.update_diagnostic_report(db, diagnostic_report_id, updated_fields)

@app.delete("/diagnostic_reports/{diagnostic_report_id}")
def delete_diagnostic_report(diagnostic_report_id: int, db: Session = Depends(get_db)):
    diagnostic_report = crud.get_diagnostic_report(db, diagnostic_report_id)
    return crud.delete_diagnostic_report(db=db, diagnostic_report=diagnostic_report)
