import csv
from os import path
from project import Project


class ProjectManager:
    """
    Project Manager Class

    Handles project and scheduling function (e.g. creating and retrieving).
    """

    def __init__(self):
        self.__schedule = []

    # Project related functions
    @staticmethod
    def input_project():
        """
        Inputs project details and creates a `projects.csv` file if does not exist.
        Appends new project details to that file.

        :exception: TypeError
        """

        # Input Project Details
        try:
            id_num = int(input("ID Number: "))
            title = input("Title: ")
            size = int(input("Size: "))
            priority = int(input("Priority: "))

            # Check if projects.csv exist; if not then create a project.csv
            if path.exists('projects.csv'):
                create_file = open('projects.csv', 'w')
                writer = csv.writer(create_file)
                writer.writerow(["id", "title", "size", "priority"])
                create_file.close()

            # Field/Column names in project.csv
            field_names = ["id", "title", "size", "priority"]

            # Open project.csv and append inputted project details
            with open('projects.csv', 'a+', newline='') as project_file:
                writer = csv.DictWriter(project_file, fieldnames=field_names)
                writer.writerow({"id": id_num, "title": title, "size": size, "priority": priority})
                print("Project has been added.")

        except TypeError:
            print("Wrong input, try again.")

    def view_one(self, project_id):
        pass

    def view_completed(self):
        pass

    def view_all(self):
        pass

    def get_project(self):
        pass

    # Scheduling related functions
    def create_schedule(self):
        try:
            file = open('projects.csv', 'r', encoding='utf-8-sig')
            table = csv.DictReader(file)
            line_count = 0

            for row in table:
                if line_count != 0:
                    self.__schedule.append(Project(row['id'], row['title'], row['size'], row['priority']))
                line_count += 1

            self.__schedule.sort(key=lambda x: (x.get_priority(), x.get_size()))
            with open('schedule.csv', 'w', newline='') as f:
                csv_writer = csv.writer(f)
                for project in self.__schedule:
                    csv_writer.writerow([project.get_id(), project.get_title(), project.get_size(),
                                         project.get_priority()])
            file.close()

        except IOError:
            return False
        else:
            return True

    @staticmethod
    def view_updated_schedule():
        try:
            with open('schedule.csv', 'r') as schedules:
                print("ID          TITLE          SIZE        PRIORITY")
                for project in schedules:
                    print(project.replace(",", "          "))
        except IOError:
            return False
        else:
            return True
