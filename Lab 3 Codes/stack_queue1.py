# parking_and_ticket_easy.py
class Stack:
    def __init__(self):
        self.table = []
        self.content = 0

    def push(self, x):
        self.table.append(x)
        self.content += 1

    def pop(self):
        if self.content == 0:
            return None
        self.content -= 1
        return self.table.pop()

    def peek(self):
        if self.content == 0:
            return None
        return self.table[-1]

    def isEmpty(self):
        return self.content == 0

    def size(self):
        return self.content

    def show(self):
        return list(self.table)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)           # back

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)       # front

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def show(self):
        return list(self.items)

# ============================================================
# A) PARKING LOT — STACK 
# ============================================================
# Rules 
# - arrive(plate): push to stack (top is closest to exit)
# - depart():pop from stack (the car at the top leaves)
# - top_car(): peek (who’s next to exit)
# - lot_size(): current count
# No middle-car extraction here—keep it pure, obvious LIFO.

class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cars = Stack()

    def arrive(self, plate: str):
        if self.cars.size() == self.capacity:
            return "Lot full"
        self.cars.push(plate)
        return self.cars.show()

    def depart(self):
        p = self.cars.pop()
        return p if p is not None else "Lot empty"

    def top_car(self):
        return self.cars.peek()

    def lot_size(self):
        return self.cars.size()

    def snapshot(self):
        return self.cars.show()

# ============================================================
# B) TICKET COUNTER — QUEUE 
# ============================================================
# Rules (simplified):
# - join(name): enqueue to back
# - serve(): dequeue from front
# - next_up(): peek at front
# - line_size(): count

class TicketCounter:
    def __init__(self):
        self.line = Queue()

    def join(self, name: str):
        self.line.enqueue(name)
        return self.line.show()

    def serve(self):
        x = self.line.dequeue()
        return x if x is not None else "No one to serve"

    def next_up(self):
        return self.line.peek()
        
    def line_size(self):
        return self.line.size()
    
    def snapshot(self):
        return self.line.show()

# ============================================================
# DEMO / SAMPLE RUNS 
# ============================================================

def print_section(title):
    print("\n" + "=" * 10, title, "=" * 10)

def demo_scenarios():
    # ----- STACK: PARKING LOT -----
    print_section("PARKING LOT (STACK)")
    lot = ParkingLot(capacity=3)

    print("Start:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())
    print("> arrived           →", lot.arrive("AAA-111"))
    print("> arrived           →", lot.arrive("BBB-222"))
    print("> arrived           →", lot.arrive("CCC-333"))
    print("> arrived           →", lot.arrive("DDD-444"))   # Lot full
    print("Now:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())

    print("> depart()          →", lot.depart())            # CCC-333
    print("Now:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())
    print("> depart()          →", lot.depart())            # BBB-222
    print("> depart()          →", lot.depart())            # AAA-111
    print("> depart()          →", lot.depart())            # Lot empty
    print("End:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())

    # ----- QUEUE: TICKET COUNTER -----
    print_section("TICKET COUNTER (QUEUE)")
    tc = TicketCounter()

    print("Start:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())
    print("> join             →", tc.join("Irene"))
    print("> join             →", tc.join("Jasper"))
    print("> join             →", tc.join("Kyla"))
    print("Now:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())

    print("> serve()           →", tc.serve())               # Irene
    print("Snapshot            →", tc.snapshot())
    print("> serve()           →", tc.serve())               # Jasper
    print("> serve()           →", tc.serve())               # Kyla
    print("> serve()           →", tc.serve())               # No one to serve
    print("End:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())


if __name__ == "__main__":
    demo_scenarios()
