from model.entity.guest_information import GuestInformation
from model.service.guest_service import GuestService
from model.tools.decorator import exception_handling

class GuestController:
    @classmethod
    @exception_handling
    def save(cls,name,family,birth_date,address,phone,email):
        guest = GuestInformation(name,family,birth_date,address,phone,email)
        return True, GuestService.save(guest)

    @classmethod
    @exception_handling
    def edit(cls,name,family,birth_date,address,phone,email):
        guest = GuestInformation(name,family,birth_date,address,phone,email)
        guest.id = id
        return True, GuestService.edit(guest)

    @classmethod
    @exception_handling
    def remove(cls,name,family,birth_date,address,phone,email):
        guest = GuestInformation(name, family, birth_date,address,phone,email)
        return True, GuestService.remove(guest)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, GuestService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        return True, GuestService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_family(cls,family):
        return True, GuestService.find_by_family(family)

    @classmethod
    @exception_handling
    def find_by_name(cls,name):
        return True, GuestService.find_by_name(name)

