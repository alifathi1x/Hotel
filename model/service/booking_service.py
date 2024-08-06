from controller.exeptions import BookingNotFoundError
from model.da.da import DataAccess
from model.entity.booking_information import BookingInformation
from model.tools.decorator import *

class BookingService:
    @classmethod
    def save(cls,booking):
        booking_da = DataAccess(BookingInformation)
        booking_da.save(booking)
        return booking

    @classmethod
    def edit(cls,booking):
        booking_da = DataAccess(BookingInformation)
        if booking_da.find_by_id(booking.id):
            booking_da.edit(booking)
            return booking
        else:
            raise BookingNotFoundError()

    @classmethod
    def remove(cls,booking):
        booking_da = DataAccess(BookingInformation)
        if booking_da.find_by_id(booking.id):
            booking_da.remove(booking)
            return booking
        else:
            raise BookingNotFoundError()

    @classmethod
    def find_all(cls):
        booking_da = DataAccess(BookingInformation)
        return booking_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        booking_da = DataAccess(BookingInformation)
        return booking_da.find_by_id(id)

    @classmethod
    def find_by_booking_number(cls,booking_number):
        booking_da = DataAccess(BookingInformation)
        return booking_da.find_by(booking_number)


