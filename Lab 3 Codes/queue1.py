# printing_queue.py

class Queue:
    def __init__(self):
        self.items = []                       # internal list to store queue elements

    def createQueue(self):
        self.items = []                       # initialize empty queue

    def enqueue(self, value):
        self.items.append(value)               # add element to the end (rear)

    def dequeue(self):
        if self.isEmpty():                     # cannot dequeue if queue is empty
            return None
        return self.items.pop(0)               # remove and return the front element

    def peek(self):
        if self.isEmpty():                     # check if queue is empty before peeking
            return None
        return self.items[0]                   # return the element at the front

    def isEmpty(self):
        return len(self.items) == 0            # True if no elements

    def deleteQueue(self):
        self.items = []                        # remove all elements (clear queue)

    def show(self):
        return self.items                      # return all current items in queue


# ---------- MAIN PROGRAM ----------
# Simulation: Printing Queue System
if __name__ == "__main__":
    q = Queue()
    q.createQueue()
    job_counter = 1                            # keeps track of job numbers

    while True:
        print("\n=== PRINTING QUEUE SYSTEM ===")
        print("1. Add print job")
        print("2. Process (print) next job")
        print("3. View next job to print")
        print("4. Show all pending print jobs")
        print("5. Clear all print jobs")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            doc_name = input("Enter document name: ")
            job = f"Job#{job_counter}: {doc_name}"
            q.enqueue(job)
            print(f"{job} added to the printing queue.")
            job_counter += 1

        elif choice == "2":
            next_job = q.dequeue()
            if next_job is None:
                print("No print jobs to process.")
            else:
                print(f"Printing... {next_job} — Completed ✅")

        elif choice == "3":
            upcoming = q.peek()
            if upcoming is None:
                print("No pending print jobs.")
            else:
                print(f"Next job to print: {upcoming}")

        elif choice == "4":
            if q.isEmpty():
                print("Printing queue is empty.")
            else:
                print("Pending print jobs:")
                for job in q.show():
                    print(" •", job)

        elif choice == "5":
            q.deleteQueue()
            print("All print jobs have been cleared.")

        elif choice == "0":
            print("Exiting printing queue system... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
