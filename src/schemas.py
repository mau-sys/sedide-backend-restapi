from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


'''
class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
'''
# ---------------------------------
# These are Schemas from my project
# ---------------------------------

class Role(BaseModel):
    id:  Optional[int]
    title: str

    class Config:
        orm_mode = True


class User(BaseModel):
    #username: EmailStr
    id:  Optional[int]
    username: str
    password: str
    is_active: bool

    role_id: int
    #role_id: Role

    class Config:
        orm_mode = True


class Psychologist(BaseModel):
    id:  Optional[int]
    first_name: str
    last_name: str
    email: str

    user_id: int
    #user_id: User

    class Config:
        orm_mode = True


class Patient(BaseModel):
    id:  Optional[int]
    first_name: str
    last_name: str
    gender: str
    age: int
    level_of_education: str
    birthplace: str
    phone: str
    email: str

    #user_id: User
    #psychologist_id: Psychologist
    user_id: int
    psychologist_id: int

    class Config:
        orm_mode = True


class Depressive_Disorder(BaseModel):
    id:  Optional[int]
    name: str
    description: str
    symptom: str
    treatment: str

    class Config:
        orm_mode = True


class Pregunta_Base(BaseModel):
    id:  Optional[int]
    description: str

    class Config:
        orm_mode = True


class Test(BaseModel):
    id:  Optional[int]
    date: datetime
    patient_id: int
    psychologist_id: int
    observation: str
    is_active: bool
    
    class Config:
        orm_mode = True


class Pregunta_Test(BaseModel):
    id:  Optional[int]
    date: datetime
    #este TEST lo hizo yoel pero creo que es con int
    #test_id: Test
    test_id: int
    #este pregunta base lo hizo yoel pero creo que es con int
    #pregunta_base_id: Pregunta_Base
    pregunta_base_id: int
    rpta: str
    is_active: bool
    
    class Config:
        orm_mode = True


class Diagnostic_Report(BaseModel):
    #date: str

    #psychologist_id: Psychologist
    #patient_id: Patient
    #depressive_disorder_id: Depressive_Disorder

#esto es de yoel pero creo que no estaba bien'''
    #psychologist_id: int
    #patient_id: int
    #depressive_disorder_id: int

    id: Optional[int]
    date: datetime
    test_id: int
    depressive_disorder_id: int

    class Config:
        orm_mode = True



class Rptas(BaseModel):
    rpt1:  str
    rpt2:  str
    rpt3:  str