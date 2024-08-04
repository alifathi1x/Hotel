
class GuestNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Guest not found")

class BookingNotFoundError(Exception):
    def __init__(self,*args):
        super().__init__("Booking not found")