from datetime import date
from sqlalchemy import Integer, DateTime, Column, Boolean
from model.entity.base import Base
from model.tools.validator import *

class BookingInformation(Base):
    __tablename__ = "booking_information_tbl"
    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _room_number = Column("room_number",Integer,nullable=False,unique=True)
    _checkin_date = Column("checkin_date",DateTime,nullable=False)
    _checkout_date = Column("checkout_date",DateTime,nullable=False)
    _room_type = Column("room_type",Boolean,nullable=False)

    def __init__(self,id,room_number,checkin_date,checkout_date,room_type):
        self._id = None
        self._room_number = room_number
        self._checkin_date = checkin_date
        self._checkout_date = checkout_date
        self._room_type = room_type

    def get_id(self):
        return self._id
    def set_id(self,id):
        self._id = id

    def get_room_number(self):
        return self._room_number
    def set_room_number(self,room_number):
        if isinstance(room_number,int):
            self._room_number = room_number
        else:
            raise ValueError("Invalid Room Number")
    def get_checkin_date(self):
        return self._checkin_date
    def set_checkin_date(self,checkin_date):
        if isinstance(checkin_date,date):
            self._checkin_date = checkin_date
        else:
            raise ValueError("Invalid Checkin Date")

    def get_room_type(self):
        return self._room_type
    def set_room_type(self,room_type):
        if room_type == room_type_validator and room_price_validator:
            self._room_type = room_type
        else:
            raise ValueError("Invalid Room")


    id = property(get_id,set_id)
    room_number = property(get_room_number,set_room_number)
    checkin_date = property(get_checkin_date,set_checkin_date)
    checkout_date = property(get_checkin_date,set_checkin_date)
    room_type = property(get_room_type,set_room_type)