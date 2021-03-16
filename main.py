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
import scheduler
import project


def main():
    """Main driver of the program."""

    print (30*"-","MENU",30*"-")

    print("""
    a. Input Project Details
    b. View Project
    c. Schedule Projects
    d. Get a Project
    e. Exit
    """)
    print(67*"-")                  
    choice = input("""Please enter your choice: """).lower()
    
    if choice == "a":
        #input_project()
        pass
    elif choice == "b":
        #view_project()
        pass
    elif choice == "c":
        scheduler = Scheduler()
        scheduler.createSchedule()
    elif choice == "d":
        scheduler = Scheduler()
        scheduler.viewUpdatedSchedule()
    elif choice == "e":
        #getproject()
        pass
    elif choice == "f":
        print("\nYou have exited.....")
        sys.exit
    else:
        print("\nPlease select letter in the choices only.")
        print("Try again.")
        menu()


main()
