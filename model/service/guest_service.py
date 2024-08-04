from controller.exeptions import GuestNotFoundError
from model.da.da import DataAccess
from model.entity.guest_information import GuestInformation
from model.tools.decorator import *

class GuestService:
    @classmethod
    def save(cls,guest):
        guest_da = DataAccess(GuestInformation)
        guest_da.save(guest)
        return guest

    @classmethod
    def edit(cls,guest):
        guest_da = DataAccess(GuestInformation)
        if guest_da.find_by_id(guest.id):
            guest_da.edit(guest)
            return guest
        else:
            raise GuestNotFoundError()

    @classmethod
    def remove(cls,guest):
        guest_da = DataAccess(GuestInformation)
        if guest_da.find_by_id(guest.id):
            return guest_da.remove(guest)
        else:
            raise GuestNotFoundError()

    @classmethod
    def find_all(cls):
        guest_da = DataAccess(GuestInformation)
        return guest_da.find_all()

    @classmethod
    def find_by_id(cls,id):
        guest_da = DataAccess(GuestInformation)
        return guest_da.find_by_id(id)

    @classmethod
    def find_by_family(cls,family,guest):
        guest_da = DataAccess(GuestInformation)
        return guest_da.find_by(guest.family == family)

    @classmethod
    def find_by_name(cls,name,guest):
        guest_da = DataAccess(GuestInformation)
        return guest_da.find_by(guest.name == name)