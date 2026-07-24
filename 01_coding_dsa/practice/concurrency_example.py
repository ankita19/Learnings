# book seat -Ticket system

#issues Correctness: shared sate gets corrupted because two thread access it at the same time
# Issue : another thread can change the state of the seat between the check and the act, leading to incorrect behavior.
# concurrency problems : correctness , coordination, Scarcity


import threading

class BookingService:
    def __init__(self):
        self.seats:dict[str,Seat] = {}
        self.lock = threading.Lock()

    def book_seat(self, seat_id:str, visitor_id: str) -> bool:
        seat = self.seats[seat_id]
        # correctness - check-then-act
        with self.lock:
            if seat.is_available():
                seat.set_occupant(visitor_id)
                return True
            return False
    
class Seat:
    def __init__(self, seat_id:str):
        self.seat_id = seat_id
        self.occupant = None

    def is_available(self) -> bool:
        return self.occupant is None

    def set_occupant(self, visitor_id: str):
        self.occupant = visitor_id

# correctness  : read - modify - write
count = 0
def increment():
    global count
    with threading.Lock():
        count += 1

 #Coordination - when useer sign up let say we need send email. while is email is in prgress signup should not be blocked -> use Queue or Asych 
 # use blocking queue

 # scarcity - limited resources - use semaphore to limit the number of concurrent access to a resource total request 100 and only 10 can be processed at a time
 
permits = threading.Semaphore(10)

def download_file(file_id):
    permits.acquire()
    try:
        # simulate file download
        print(f"Downloading file {file_id}...")
    finally:
        permits.release()   

