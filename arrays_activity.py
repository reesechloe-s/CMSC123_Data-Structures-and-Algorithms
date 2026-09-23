# REESE CHLOE SANTIAGO
# CMSC 123 LAB 1A
# SEPTEMBER 23, 2026

def create_waitlist():
    return []

def add_to_waitlist(waitlist, name, position):
    waitlist.insert(position, name)
    print(f"Adding {name}...")

def remove_from_waitlist(waitlist, name):
    waitlist.remove(name)
    print(f"Removing '{name}...")


def search_waitlist(waitlist, name):
    print(f"Searching for '{name}'...")
    for i in range(len(waitlist)):
        if waitlist[i] == name:
            print(f"Found '{name}' at index {i}")
            return
    print(f"{name} is not in the waitlist")

def traverse_waitlist(waitlist):
    print("[", end="")
    for i in range(len(waitlist)):
        print(f"'{waitlist[i]}'", end="")
        if i < len(waitlist) - 1:
            print(", ", end="")
    print("]")

def create_chart(rows, cols):
    chart = []
    for i in range(rows):
        row_list = [None] * cols
        chart.append(row_list)
    return chart

def assign_chart(chart, row, col, name):
    chart[row][col] = name
    print(f"Row {row}, Col {col} -> {name}")

def clear_seat(chart, row, col):
    chart[row][col] = None
    print(f"Clearing seat ({row}, {col})...")

def traverse_chart(chart):
    print("Updated seating chart...")
    for i in range(len(chart)):
        print(f"Row {i}: {chart[i]}")

def main():
    print("=== CINEMA WAITLIST ===")
    cinema_waitlist = create_waitlist()
    print(f"Initial waitlist: {cinema_waitlist}")
    add_to_waitlist(cinema_waitlist, 'Ana', 0)
    add_to_waitlist(cinema_waitlist, 'Ben', 1)
    add_to_waitlist(cinema_waitlist, 'Cara', 2)
    add_to_waitlist(cinema_waitlist, 'Dan', 3)
    add_to_waitlist(cinema_waitlist, 'Eli', 4)
    print(f"Current waitlist: {cinema_waitlist}")

    print()
    remove_from_waitlist(cinema_waitlist, 'Cara')
    print(f"Waitlist after removal: {cinema_waitlist}")

    print()
    search_waitlist(cinema_waitlist, 'Ben')

    print("\nFinal Waitlist: ", end="")
    traverse_waitlist(cinema_waitlist)

    print("\n=== SEATING CHART ===")
    seating_chart = create_chart(3, 4)
    print("Assigning seats...")
    assign_chart(seating_chart, 0, 1, 'Ana')
    assign_chart(seating_chart, 1, 2, 'Ben')
    assign_chart(seating_chart, 2, 3, 'Dan')

    print()
    clear_seat(seating_chart, 1, 2)
    traverse_chart(seating_chart)
    
main()

# === Reflection Questions ===
# [1] How do .insert() and .remove() change the array automatically?
## Inserting and removing items causes shifting of items. Because an array is stored in contiguous blocks of memory, inserting an item in between the items shifts every subsequent items one spot to the right to make room. 
## The .remove() will shift all the remaining items on the right side of the array to shift to the left to close the empty gap of memory.

# [2] Why is traversal using loops still important even with built-in functions?
## For loop allows me to traverse each item carefully and format it better (in the case of charts, row by row). 
## Loops let me inspect, format, or manipulate data exactly how I want it when built-in functions fail due to some pre-formatting they have.

# [3] How would you modify this program if the cinema had 10 rows
## I will just change the function call from create_chart(3, 4) to create_chart(10, 4) because I used variables for rows and columns in the function instead of hardcoding the values in the loops

## ADDITIONAL: This isn't really an answer to the question, but I would like to modify my code to have two parameters inside the traverse_waitlist. I kind of want it to be 

# def traverse_waitlist(message, waitlist):
#     print(f"{message}: {waitlist}")

# then just call traverse_waitlist on the printing of current waitlist, waitlist after removal, and final waitlist.
# I think this follows the principle of DRY (Don't Repeat Yourself)
