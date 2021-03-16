"""
Case Study (Python Implementation) in Structured Programming Languages
Submitted to Hadji P. Tejuco (Course Adviser)
FEU Tech
Authors:
    Rom Braveheart P. Leuterio (Dauntless Dev)
    Hezekiah John V. Rizan (Hezzz)
    Chrys Uoie A. Salazar (Memewtoo)
"""

import sys
from scheduler import Scheduler
# from project import Project

def main():
    """Main driver of the program."""
    menu()


def menu():
    print(30 * "-", "MENU", 30 * "-")

    print("""
    a. Input Project Details
    b. View Project
    c. Schedule Projects
    d. Get a Project
    e. Exit
    """)
    print(66 * "-")

    choice = input("Please enter your choice: ").lower()
    
    if choice == "a":
        # input_project()
        pass
    elif choice == "b":
        menu_view_project()
    elif choice == "c":
        menu_schedule_project()
    elif choice == "d":
        # get_project()
        pass
    elif choice == "e":
        print("\nYou have exited.....")
        sys.exit()
    else:
        print("\nPlease select letter in the choices only.")
        print("Try again.")
        menu()


def menu_view_project():
    print(26 * "-", "VIEW PROJECT", 26 * "-")
    print("""
    a. One Project
    b. Completed
    c. All Projects
    d. Back
    """)
    print(66 * "-")

    choice = input("Please enter your choice: ").lower()

    if choice == "a":
        pass
    elif choice == "b":
        pass
    elif choice == "c":
        pass
    elif choice == "d":
        menu()
    else:
        print("\nPlease select letter in the choices only.")
        print("Try again.")
        menu_view_project()


def menu_schedule_project():
    print(24 * "-", "SCHEDULE PROJECT", 24 * "-")
    print("""
    a. Create Schedule
    b. View Updated Schedule
    c. Back
    """)
    print(66 * "-")

    choice = input("Please enter your choice: ").lower()

    if choice == "a":
        print(66*"-")
        if scheduler.create_schedule():
            print("A schedule has been created.")
        else:
            print("Required file `project.txt` does not exist!")
        menu_schedule_project()
    elif choice == "b":
        print(28 * "-", "SCHEDULE", 28 * "-")
        if not scheduler.view_updated_schedule():
            print("Please create a schedule first.")
        menu_schedule_project()
    elif choice == "c":
        menu()
    else:
        print("\nPlease select letter in the choices only.")
        print("Try again.")
        menu_schedule_project()


scheduler = Scheduler()
main()
