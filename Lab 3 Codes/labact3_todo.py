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
    
    #TO DO
    def depart_specific(self, plate: str):
        if self.cars.isEmpty():
            return "Lot empty"

        temp_stack = Stack()
        found_plate = "Not found"

        while not self.cars.isEmpty():
            current_car = self.cars.pop()
            if current_car == plate:
                found_plate = current_car
                break
            temp_stack.push(current_car)

        while not temp_stack.isEmpty():
            self.cars.push(temp_stack.pop())
        return found_plate

    def top_car(self):
        return self.cars.peek()

    def lot_size(self):
        return self.cars.size()

    def snapshot(self):
        return self.cars.show()
    
# ============================================================
# B) TICKET COUNTER — QUEUE 
# ============================================================

class TicketCounter:
    def __init__(self):
        self.line = Queue()

    def join(self, name: str):
        self.line.enqueue(name)
        return self.line.show()

    def serve(self):
        x = self.line.dequeue()
        return x if x is not None else "No one to serve"
    
    #TO DO
    def move_to_front(self, name: str):
        if self.line.isEmpty():
            return "No one to move"

        size = self.line.size()
        found_name = False

        for i in range(size):
            current_person = self.line.dequeue()
            if current_person == name and not found_name:
                found_name = True
                break
            else:
                self.line.enqueue(current_person)
            
        if found_name == False:
            return "Not found"
        else:
            self.line.enqueue(name)

        for i in range(size - 1):
            self.line.enqueue(self.line.dequeue())

        return self.snapshot()
        
        """
        Move the first occurrence of 'name' to the FRONT using ONLY dequeue/enqueue.
        Return:
          - a list snapshot if moved
          - "Not found" if absent
          - "No one to move" if empty
        """
        # NOTE: DO NOT use indexing or list .index(). Use only queue ops.
        

    #TO DO
    def rotate(self, k: int):
        """
        Rotate the line left by k:
          Repeat k times: dequeue front → enqueue to back.
        Return the list snapshot of the line.
        """

        if self.line.isEmpty():
            return self.snapshot()
        
        actual_k = k % self.line.size()

        for _ in range(actual_k):
            self.line.enqueue(self.line.dequeue())

        return self.snapshot()
    
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
    print("> arrived           ->", lot.arrive("AAA-111"))
    print("> arrived           ->", lot.arrive("BBB-222"))
    print("> arrived           ->", lot.arrive("CCC-333"))
    print("> arrived           ->", lot.arrive("DDD-444"))   # Lot full
    print("Now:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())

    print("> depart()          ->", lot.depart())            # CCC-333
    print("Now:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())
    print("> depart()          ->", lot.depart())            # BBB-222
    print("> depart()          ->", lot.depart())            # AAA-111
    print("> depart()          ->", lot.depart())            # Lot empty
    print("End:", lot.snapshot(), "| Top:", lot.top_car(), "| Size:", lot.lot_size())

    # ----- QUEUE: TICKET COUNTER -----
    print_section("TICKET COUNTER (QUEUE)")
    tc = TicketCounter()

    print("Start:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())
    print("> join             ->", tc.join("Irene"))
    print("> join             ->", tc.join("Jasper"))
    print("> join             ->", tc.join("Kyla"))
    print("Now:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())

    print("> serve()           ->", tc.serve())               # Irene
    print("Snapshot            ->", tc.snapshot())
    print("> serve()           ->", tc.serve())               # Jasper
    print("> serve()           ->", tc.serve())               # Kyla
    print("> serve()           ->", tc.serve())               # No one to serve
    print("End:", tc.snapshot(), "| Next:", tc.next_up(), "| Size:", tc.line_size())

    #TO DO TEST RUNS
    print("\n--- EXTRA TESTS: depart_specific / move_to_front / rotate ---")

    # ParkingLot: depart_specific
    lot2 = ParkingLot(capacity=5)
    for p in ["AAA-111", "BBB-222", "CCC-333", "DDD-444"]:
        print("> arrive", p, "->", lot2.arrive(p))
    print("Snapshot:", lot2.snapshot())
    print("depart_specific('CCC-333') ->", lot2.depart_specific("CCC-333"))  # should remove CCC-333
    print("After:", lot2.snapshot())
    print("depart_specific('ZZZ-999') ->", lot2.depart_specific("ZZZ-999"))  # Not found
    print("After:", lot2.snapshot())

    # TicketCounter: move_to_front + rotate
    print()
    tc2 = TicketCounter()
    for n in ["Irene", "Jasper", "Kyla", "Luis"]:
        print("> join", n, "->", tc2.join(n))
    print("Snapshot:", tc2.snapshot())
    print("move_to_front('Kyla') ->", tc2.move_to_front("Kyla"))  # Kyla should become front
    print("After:", tc2.snapshot())                              # ['Kyla', 'Irene', 'Jasper', 'Luis']
    print("rotate(2) ->", tc2.rotate(2))                          # two rotations
    print("After:", tc2.snapshot())                              # ['Jasper', 'Luis', 'Kyla', 'Irene']
    print("move_to_front('Zed') ->", tc2.move_to_front("Zed"))    # Not found
    print("After:", tc2.snapshot())

if __name__ == "__main__":
    demo_scenarios()
