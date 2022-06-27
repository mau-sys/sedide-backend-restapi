from cgi import test
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

#from . import crud, models, schemas
#from .database import SessionLocal, engine

import crud
import models
import schemas
from database import SessionLocal, engine
from knowledge_engine import DiagnosisOfDepressiveDisorder


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
# -----------------------------------------
#   THESE ARE FROM MY PROJECT
# -----------------------------------------


@app.get("/")
def hello_world():
    return "helloWorld"


@app.get("/rol/{role_id}", response_model=schemas.Role)
def read_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id=role_id)
    if role is None:
        raise HTTPException(status_code=404, detail="User not found")
    return role


@app.get("/roles/", response_model=list[schemas.Role])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles


@app.post("/rol/", response_model=schemas.Role)
def create_role(role: schemas.Role, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    return crud.create_role(db=db, role=role)


@app.patch("/rol/{role_id}", response_model=schemas.Role)
def update_role(
    role_id: int,
    updated_fields: schemas.Role,
    db: Session = Depends(get_db),
):
    return crud.update_role(db, role_id, updated_fields)


@app.delete("/rol/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    role = crud.get_role(db, role_id)
    return crud.delete_role(db=db, role=role)

# -------------------
# USER HTTP REQUESTS
# -------------------


@app.get("/user/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id=user_id)
    return user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/user", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_user(db=db, user=user)


@app.patch("/user/{user_id}", response_model=schemas.User)
def update_user(
    user_id: int,
    updated_fields: schemas.User,
    db: Session = Depends(get_db),
):
    return crud.update_user(db, user_id, updated_fields)


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    return crud.delete_user(db=db, user=user)


# ---------------------------
# PSYCHOLOGIST HTTP REQUESTS
# ---------------------------


@app.get("/psychologist/{psychologist_id}", response_model=schemas.Psychologist)
def read_psychologist(psychologist_id: int, db: Session = Depends(get_db)):
    db_psychologist = crud.get_psychologist(
        db, psychologist_id=psychologist_id)
    return db_psychologist


@app.get("/psychologists/", response_model=list[schemas.Psychologist])
def read_psychologists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    psychologists = crud.get_psychologists(db, skip=skip, limit=limit)
    return psychologists


@app.post("/psychologist", response_model=schemas.Psychologist)
def create_psychologist(psychologist: schemas.Psychologist, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_psychologist(db=db, psychologist=psychologist)


@app.patch("/psychologist/{psychologist_id}", response_model=schemas.Psychologist)
def update_psychologist(
    psychologist_id: int,
    updated_fields: schemas.Psychologist,
    db: Session = Depends(get_db),
):
    return crud.update_psychologist(db, psychologist_id, updated_fields)


@app.delete("/psychologist/{psychologist_id}")
def delete_psychologist(psychologist_id: int, db: Session = Depends(get_db)):
    psychologist = crud.get_psychologist(db, psychologist_id)
    return crud.delete_psychologist(db=db, psychologist=psychologist)


# ---------------------------
# PATIENT HTTP REQUESTS
# ---------------------------


@app.get("/patient/{patient_id}", response_model=schemas.Patient)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id=patient_id)
    return patient


@app.get("/patients/", response_model=list[schemas.Patient])
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, skip=skip, limit=limit)
    return patients


@app.post("/patient", response_model=schemas.Patient)
def create_patient(patient: schemas.Patient, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_patient(db=db, patient=patient)


@app.patch("/patient/{patient_id}", response_model=schemas.Patient)
def update_patient(
    patient_id: int,
    updated_fields: schemas.Patient,
    db: Session = Depends(get_db),
):
    return crud.update_patient(db, patient_id, updated_fields)


@app.delete("/patient/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    return crud.delete_patient(db=db, patient=patient)

# ----------------------------------
# DEPRESSIVE DISORDER HTTP REQUESTS
# ----------------------------------


@app.get("/depressive_disorder/{depressive_disorder_id}", response_model=schemas.Depressive_Disorder)
def read_depressive_disorder(depressive_disorder_id: int, db: Session = Depends(get_db)):
    depressive_disorder = crud.get_depressive_disorder(
        db, depressive_disorder_id=depressive_disorder_id)
    return depressive_disorder


@app.get("/depressive_disorders/", response_model=list[schemas.Depressive_Disorder])
def read_depressive_disorders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    depressive_disorders = crud.get_depressive_disorders(
        db, skip=skip, limit=limit)
    return depressive_disorders


@app.post("/depressive_disorder/", response_model=schemas.Depressive_Disorder)
def create_depressive_disorder(depressive_disorder: schemas.Depressive_Disorder, db: Session = Depends(get_db)):
    #db_role = crud.get_user_by_email(db, email=user.email)
    #role = crud.get_role(db, role_id=role_id)
    return crud.create_depressive_disorder(db=db, depressive_disorder=depressive_disorder)


@app.patch("/depressive_disorder/{depressive_disorder_id}", response_model=schemas.Depressive_Disorder)
def update_depressive_disorder(
    depressive_disorder_id: int,
    updated_fields: schemas.Depressive_Disorder,
    db: Session = Depends(get_db),
):
    return crud.update_depressive_disorder(db, depressive_disorder_id, updated_fields)


@app.delete("/depressive_disorder/{depressive_disorder_id}")
def delete_depressive_disorder(depressive_disorder_id: int, db: Session = Depends(get_db)):
    depressive_disorder = crud.get_depressive_disorder(
        db, depressive_disorder_id)
    return crud.delete_depressive_disorder(db=db, depressive_disorder=depressive_disorder)


# ----------------------------------
# PREGUNTA BASE HTTP REQUESTS
# ----------------------------------

@app.get("/pregunta_base/{pregunta_base_id}", response_model=schemas.Pregunta_Base)
def read_pregunta_base(pregunta_base_id: int, db: Session = Depends(get_db)):
    pregunta_base = crud.get_pregunta_base(
        db, pregunta_base_id=pregunta_base_id)
    return pregunta_base


@app.get("/preguntas_base/", response_model=list[schemas.Pregunta_Base])
def read_preguntas_base(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    preguntas_base = crud.get_preguntas_base(
        db, skip=skip, limit=limit)
    return preguntas_base


@app.post("/pregunta_base/", response_model=schemas.Pregunta_Base)
def create_pregunta_base(pregunta_base: schemas.Pregunta_Base, db: Session = Depends(get_db)):
    return crud.create_pregunta_base(db=db, pregunta_base=pregunta_base)


'''@app.patch("/pregunta_base/{pregunta_base}", response_model=schemas.Depressive_Disorder)
def update_pregunta_base(
    depressive_disorder_id: int,
    updated_fields: schemas.Depressive_Disorder,
    db: Session = Depends(get_db),
):
    return crud.update_depressive_disorder(db, depressive_disorder_id, updated_fields)'''


@app.delete("/pregunta_base/{pregunta_base_id}")
def delete_depressive_disorder(pregunta_base_id: int, db: Session = Depends(get_db)):
    pregunta_base = crud.get_pregunta_base(
        db, pregunta_base_id)
    return crud.delete_pregunta_base(db=db, pregunta_base=pregunta_base)


# ----------------------------------
# TEST HTTP REQUESTS
# ----------------------------------

@app.get("/test/{test_id}", response_model=schemas.Test)
def read_test(test_id: int, db: Session = Depends(get_db)):
    test = crud.get_test(
        db, test_id=test_id)
    return test


@app.get("/tests/", response_model=list[schemas.Test])
def read_tests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tests = crud.get_tests(
        db, skip=skip, limit=limit)
    return tests


@app.post("/test/", response_model=schemas.Test)
def create_test(test: schemas.Test, db: Session = Depends(get_db)):
    return crud.create_test(db=db, test=test)


'''@app.patch("/test/{test}", response_model=schemas.Depressive_Disorder)
def update_test(
    depressive_disorder_id: int,
    updated_fields: schemas.Depressive_Disorder,
    db: Session = Depends(get_db),
):
    return crud.update_depressive_disorder(db, depressive_disorder_id, updated_fields)'''


@app.delete("/test/{test_id}")
def delete_test(test_id: int, db: Session = Depends(get_db)):
    test = crud.get_test(
        db, test_id)
    return crud.delete_pregunta_base(db=db, test=test)




# ----------------------------------
# PREGUNTA_TEST HTTP REQUESTS
# ----------------------------------

@app.post("/pregunta_test/", response_model=schemas.Pregunta_Test)
def create_pregunta_test(pregunta_test: schemas.Pregunta_Test, db: Session = Depends(get_db)):
    return crud.create_pregunta_test(db=db, pregunta_test=pregunta_test)



@app.get("/pregunta_test/{pregunta_test_id}", response_model=schemas.Pregunta_Test)
def read_pregunta_test(pregunta_test_id: int, db: Session = Depends(get_db)):
    pregunta_test = crud.get_pregunta_test(
        db, pregunta_test_id=pregunta_test_id)
    return pregunta_test


@app.get("/pregunta_tests/", response_model=list[schemas.Pregunta_Test])
def read_pregunta_tests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pregunta_tests = crud.get_pregunta_tests(
        db, skip=skip, limit=limit)
    return pregunta_tests


@app.delete("/pregunta_test/{pregunta_test_id}")
def delete_pregunta_test(pregunta_test_id: int, db: Session = Depends(get_db)):
    pregunta_test = crud.get_pregunta_test(
        db, pregunta_test_id)
    return crud.delete_pregunta_test(db=db, pregunta_test=pregunta_test)


# ----------------------------------
# DIAGNOSTIC REPORT
# ----------------------------------

@app.post("/diagnostic_report/", response_model=schemas.Diagnostic_Report)
def create_diagnostic_report(diagnostic_report: schemas.Diagnostic_Report, db: Session = Depends(get_db)):
    return crud.create_diagnostic_report(db=db, diagnostic_report=diagnostic_report)



@app.get("/diagnostic_report/{diagnostic_report_id}", response_model=schemas.Diagnostic_Report)
def read_diagnostic_report(diagnostic_report_id: int, db: Session = Depends(get_db)):
    diagnostic_report = crud.get_diagnostic_report(
        db, diagnostic_report_id=diagnostic_report_id)
    return diagnostic_report


@app.get("/diagnostic_reports/", response_model=list[schemas.Diagnostic_Report])
def read_diagnostic_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    diagnostic_reports = crud.get_diagnostic_reports(
        db, skip=skip, limit=limit)
    return diagnostic_reports


@app.delete("/diagnostic_report/{diagnostic_report_id}")
def delete_diagnostic_report(diagnostic_report_id: int, db: Session = Depends(get_db)):
    diagnostic_report = crud.get_diagnostic_report(
        db, diagnostic_report_id)
    return crud.delete_diagnostic_report(db=db, diagnostic_report=diagnostic_report)


@app.post("/run/")
def run_diagnosis(rpta: schemas.Rptas):
        engine = DiagnosisOfDepressiveDisorder()
        engine.symptom_1(rpta.rpt1)
        engine.symptom_2(rpta.rpt2)
        engine.symptom_3(rpta.rpt3)
        engine.symptom_4(rpta.rpt4)
        engine.symptom_5(rpta.rpt5)
        engine.symptom_6(rpta.rpt6)
        engine.symptom_7(rpta.rpt7)
        engine.symptom_8(rpta.rpt8)
        engine.symptom_9(rpta.rpt9)
        engine.symptom_10(rpta.rpt10)
        engine.symptom_11(rpta.rpt11)
        engine.symptom_12(rpta.rpt12)
        engine.symptom_13(rpta.rpt13)
        engine.symptom_14(rpta.rpt14)
        engine.symptom_15(rpta.rpt15)
        engine.symptom_16(rpta.rpt16)
        engine.symptom_17(rpta.rpt17)
        engine.symptom_18(rpta.rpt18)
        engine.symptom_19(rpta.rpt19)
        engine.symptom_20(rpta.rpt20)
        engine.symptom_21(rpta.rpt21)
        engine.symptom_22(rpta.rpt22)
        engine.symptom_23(rpta.rpt23)
        engine.symptom_24(rpta.rpt24)
        engine.symptom_25(rpta.rpt25)
        engine.symptom_26(rpta.rpt26)
        engine.symptom_27(rpta.rpt27)
        engine.symptom_28(rpta.rpt28)
        engine.symptom_29(rpta.rpt29)
        engine.symptom_30(rpta.rpt30)
        engine.symptom_31(rpta.rpt31)
        engine.symptom_32(rpta.rpt32)
        engine.symptom_33(rpta.rpt33)
        engine.symptom_34(rpta.rpt34)
        engine.symptom_35(rpta.rpt35)
        engine.symptom_36(rpta.rpt36)
        engine.symptom_37(rpta.rpt37)

        
        engine.disorder_1()
        '''engine.reset()
        return engine.run()'''



# ----------------------------------
# DIAGNOSTIC REPORT HTTP REQUESTS ANTERIOR A YOEL
# ----------------------------------


'''@app.get("/diagnostic_reports/{diagnostic_report_id}", response_model=schemas.Diagnostic_Report)
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
'''
