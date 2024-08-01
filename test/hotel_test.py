from model.da.da import DataAccess
from model.entity.guest_information import *
from datetime import datetime

my_date = datetime.now()

guest = GuestInformation(400,"ali","abolfathi",my_date,"hfurhurhfurhfhfuuruh","09213703837","www.alifathi@yahoo.com")
guest_da = DataAccess(GuestInformation)
guest_da.save(guest)
print(guest)