import re

room1 = "vip"
room2 = "normal"
def room_price_validator(room_price):
    if room_price == room1:
        return 1000
    elif room_price == room2:
        return 500

def room_type_validator(room_type):
    if room_type == room1:
        return room1
    elif room_type == room2:
        return room2

def name_validator(name):
    return re.match(r"^[a-zA-Z]{2,40}$",name)
def email_validator(email):
    return re.match(r"^[\w.]{2,20}@(gmail|yahoo)\.com$",email)
def address_validator(address):
    return re.match(r"^[a-zA-Z]{1,80}$",address)
