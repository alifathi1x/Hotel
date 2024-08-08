from model.entity.booking_information import BookingInformation
from model.service.booking_service import BookingService
from model.tools.decorator import exception_handling

class BookingController:
    @classmethod
    @exception_handling
    def save(cls,room_number,checkin_date,checkout_date,room_type):
        booking = BookingInformation(room_number,checkin_date,checkout_date,room_type)
        return True, BookingService.save(booking)

    @classmethod
    @exception_handling
    def edit(cls,room_number,checkin_date,checkout_date,room_type):
        booking = BookingInformation(room_number,checkin_date,checkout_date,room_type)
        booking.id = id
        return True, BookingService.edit(booking)

    @classmethod
    @exception_handling
    def remove(cls,room_number,checkin_date,checkout_date,room_type):
        booking = BookingInformation(room_number,checkin_date,checkout_date,room_type)
        return True, BookingService.remove(booking)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, BookingService.find_all()


    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        return True, BookingService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_booking_number(cls,booking_number):
        return True, BookingService.find_by_booking_number(booking_number)
