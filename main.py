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
import csv
from os import path
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
        input_project()
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
            print("Required file `project.csv` does not exist!")
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

def input_project():

    #Input Project Details
    id_num = int(input("ID Number: "))
    title = input("Title: ")
    size = int(input("Size: "))
    priority = int(input("Priority: "))

    #Check if projects.csv exist; if not then create a project.csv
    if (path.exists('projects.csv') == False):
        create_file = open('projects.csv','w')
        writer = csv.writer(create_file)
        writer.writerow(["id","title","size","priority"])

        create_file.close()

    #Field/Column names in project.csv
    field_names = ["id","title","size","priority"]

    #Open project.csv and append inputted project details
    file = open('projects.csv','a+',newline='')
    writer = csv.DictWriter(file,fieldnames = field_names)

    writer.writerow({"id":id_num,"title":title,"size":size,"priority":priority})
    print("Project has been added.")

    file.close()
    menu()



scheduler = Scheduler()
main()
