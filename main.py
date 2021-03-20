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
    print(42 * "-", "MENU", 42 * "-")

    print("""
    a. Input Project Details
    b. View Project
    c. Schedule Projects
    d. Get a Project
    e. Exit
    """)
    print(90 * "-")

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
    print(38 * "-", "VIEW PROJECT", 38 * "-")
    print("""
    a. One Project
    b. Completed
    c. All Projects
    d. Back
    """)
    print(90 * "-")

    choice = input("Please enter your choice: ").lower()

    if choice == "a":
        try:
            id_number = int(input("Enter the ID Number: "))
            print(40 * "-", "PROJECT", 41 * "-")
            project_manager.view_one(id_number)
        except TypeError:
            print("Invalid input. Please input a valid (int) ID.")
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
    print(36 * "-", "SCHEDULE PROJECT", 36 * "-")
    print("""
    a. Create Schedule
    b. View Updated Schedule
    c. Back
    """)
    print(90 * "-")

    choice = input("Please enter your choice: ").lower()

    if choice == "a":
        print(90 * "-")
        if not project_manager.is_projects_empty():
            project_manager.create_schedule()
        else:
            print("Input projects first.")
        menu_schedule_project()
    elif choice == "b":
        if project_manager.is_schedule_empty():
            print(90 * "-")
            print("Please create a schedule first.")
        else:
            print(40 * "-", "SCHEDULE", 40 * "-")
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
