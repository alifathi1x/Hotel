from datetime import date
from sqlalchemy import Column, Integer, String, Date
from model.entity.base import Base
from model.tools.validator import *

class GuestInformation(Base):
    __tablename__ = "guest_information_tbl"
    _id = Column("id",Integer,primary_key=True,autoincrement=True)
    _name = Column("name",String(20),nullable=False)
    _family = Column("family",String(20),nullable=False)
    _birth_date = Column("birth_date",Date,nullable=False)
    _address = Column("address",String(30),nullable=False,unique=True)
    _phone = Column("phone",Integer,nullable=False,unique=True)
    _email = Column("email",String(50),nullable=False,unique=True)

    def __init__(self,id,name,family,birth_date,address,phone,email):
        self._id = None
        self._name = name
        self._family = family
        self._birth_date = birth_date
        self._address = address
        self._phone = phone
        self._email = email

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_name(self):
        return self._name
    def set_name(self,name):
        if name_validator(name):
            self._name = name
        else:
            raise ValueError("Invalid Name")

    def get_family(self):
        return self._family
    def set_family(self,family):
        if name_validator(family):
            self._family = family
        else:
            raise ValueError("Invalid Family")

    def get_birth_date(self):
        return self._birth_date
    def set_birth_date(self,birth_date):
        if isinstance(birth_date,date):
            self._birth_date = birth_date
        else:
            raise ValueError("Invalid Birth Date")

    def get_address(self):
        return self._address
    def set_address(self, address):
        if address_validator(address):
            self._address = address
        else:
            raise ValueError("Invalid Address")

    def get_phone(self):
        return self._phone
    def set_phone(self,phone):
        if isinstance(phone,int):
            self._phone = phone
        else:
            raise ValueError("Invalid Phone Number")

    def get_email(self):
        return self._email
    def set_email(self,email):
        if email_validator(email):
            self._email = email
        else:
            raise ValueError("Invalid Email")

    id = property(get_id,set_id)
    name = property(get_name,set_name)
    family = property(get_family,set_family)
    birth_date = property(get_birth_date,set_birth_date)
    address = property(get_address,set_address)
    phone = property(get_phone,set_phone)
    email = property(get_email,set_email)
