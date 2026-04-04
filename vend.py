"""
vend.py
by Team Purple: Paul Renaud, Andrii Saveliev, Gueswende Kafando
For Ivy Tech class SDEV 265
Spring 2026

Simulates a vending machine, but mostly just the internal logic of accepting cash, vending, and giving change.

April 3, 2026
Paul: started writing code. Made basic main menu, and placeholder functions. Added color to some text.

"""

# name ANSI colors for colored output
A_RED =     "\033[31m"
A_GREEN =   "\033[32m"
A_YELLOW =  "\033[33m"
A_BLUE =    "\033[34m"
A_MAGENTA = "\033[35m"
A_CYAN =    "\033[36m"
A_WHITE =   "\033[37m"
A_END =     "\033[0m"


def startup():
    print("Starting up...")
    print("Get location and price list.")
    print("Get coin quantities available.")
    print("Ready.")

def pause():
    input("Press Enter")

def deposit_menu():
    print("Cash deposit feature will go here.")
    pause()

def coin_return():
    print("Coin return feature goes here.")
    pause()

def select_item():
    print("Item selection feature goes here.")
    print("Display price. Vend if enough cash entered, and return change.")
    pause()

def admin_options():
    print("Admin option menu goes here.")
    pause()

startup()
while True:
    print(A_GREEN)
    print("  Vending Machine")
    print("  ---------------")
    print("  0. Exit")
    print("  1. Deposit Cash")
    print("  2. Coin Return")
    print("  3. Select item")
    print("  4. Admin Options" + A_END)
    choice = input(A_YELLOW + "Enter action:")
    print(A_END)  # return color to normal
    if choice == "0":
        break
    elif choice == "1":
        deposit_menu()
    elif choice == "2":
        coin_return()
    elif choice == "3":
        select_item()
    elif choice == "4":
        admin_options()
    else:
        print(A_RED + "Invalid option" + A_END)

print("Goodbye.")
