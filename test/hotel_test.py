from model.da.da import DataAccess
from model.entity.guest_information import *
from datetime import datetime

my_date = datetime.now()

guest = GuestInformation(407,"ali","abolfathi",my_date,"hfurhurhefurhfhfuwuruh",222874722,"www.aliifathi@yahoo.com")
guest_da = DataAccess(GuestInformation)
guest_da.save(guest)
print(guest)