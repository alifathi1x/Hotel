import re

room1 = "vip"
room2 = "normal"

def room_type_validator(room_type):
    if room_type == room1:
        return room1
    elif room_type == room2:
        return room2
