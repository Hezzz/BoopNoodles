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
from project_manager import ProjectManager


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
        project_manager.input_project()
        menu()
    elif choice == "b":
        menu_view_project()
    elif choice == "c":
        menu_schedule_project()
    elif choice == "d":
        if project_manager.is_schedule_empty():
            print("Please create a schedule first.")
        else:
            project_manager.get_project()
        menu()
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
        id_number = input("Enter the ID Number: ")
        print(28 * "-", "PROJECT", 29 * "-")
        project_manager.view_one(id_number)
        menu_view_project()
    elif choice == "b":
        project_manager.view_completed()
        menu_view_project()
    elif choice == "c":
        project_manager.view_all()
        menu_view_project()
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
        print(66 * "-")
        if not project_manager.is_schedule_empty():
            print("Schedule already exists. Please finish first before creating a new one.")
        else:
            project_manager.create_schedule()
        menu_schedule_project()
    elif choice == "b":
        if project_manager.is_schedule_empty():
            print(66 * "-")
            print("Please create a schedule first.")
        else:
            print(28 * "-", "SCHEDULE", 28 * "-")
            project_manager.view_updated_schedule()
        menu_schedule_project()
    elif choice == "c":
        menu()
    else:
        print("\nPlease select letter in the choices only.")
        print("Try again.")
        menu_schedule_project()


project_manager = ProjectManager()
main()
