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

    def is_schedule_empty(self):
        """Checks if the schedule is empty."""

        return not self.__schedule

    # Project related functions
    def input_project(self):
        """
        Inputs project details and creates a `projects.csv` file if does not exist.
        Appends new project details to that file.

        :exception: TypeError
        """

        try:
            # Input project details
            id_num = int(input("ID Number: "))
            title = input("Title: ")
            size = int(input("Size: "))
            priority = int(input("Priority: "))
            project = Project(project_id=id_num, title=title, size=size, priority=priority)

            self.__overwrite_projects_file(file_name='projects.csv', project=project)
            print("Project has been added.")

        except TypeError:
            print("Wrong input, try again.")

    def view_one(self, project_id):

        print(28 * "-", "PROJECT", 29 * "-")
        
        file = open('projects.csv','r',encoding='utf-8-sig')
        table = csv.DictReader(file)

        line_count = 0
        for row in table:
            if project_id in row['id']:
                print("{:<15}{:^10}{:>17}{:>21}".format("ID", "TITLE", "SIZE", "PRIORITY"))
                print("{:<15}{:^10}{:>15}{:>20}".format(row['id'],row['title'],row['size'],row['priority']))
                line_count+=1
                break

        if line_count == 0:
            print("Project does not exist. Please try again")
        
        file.close()

    def view_completed(self):
        """Prints all the completed projects read from the `completed_projects.csv` file."""

        error_message = "Required file `completed_projects.csv` does not exist! Complete a project first."
        self.view_file('completed_projects.csv', error_message)

    def view_all(self):
        """Prints all the projects received read from the `projects.csv` file."""

        error_message = "Required file `projects.csv` does not exist! Input project details first."
        self.view_file('projects.csv', error_message)

    def get_project(self):
        """
        Gets the topmost project from the queue of scheduled projects.
        Adds that project to the list of completed projects then
        overwrites the schedule to the updated one.
        """

        # Print schedule then pop the topmost project.
        self.view_updated_schedule()
        project = self.__schedule.pop(0)

        # Print confirmation, add to the completed list.
        print("Project", project.get_title(), " has been removed from the schedule...")
        self.__overwrite_projects_file(file_name='completed_projects.csv', project=project)
        print("Project", project.get_title(), " added to completed list...")

        # Overwrite the schedule and print the updated list.
        self.__overwrite_schedule()
        self.view_updated_schedule()

    # Scheduling related functions
    def create_schedule(self):
        """
        Creates a schedule of projects read from the `projects.csv` file.

        :exception: IOError
        """

        try:
            file = open('projects.csv', 'r', encoding='utf-8-sig')
            table = csv.DictReader(file)
            line_count = 0

            for row in table:
                if line_count != 0:
                    self.__schedule.append(Project(row['id'], row['title'], row['size'], row['priority']))
                line_count += 1

            self.__schedule.sort(key=lambda x: (x.get_priority(), x.get_size()))
            self.__overwrite_schedule()
            file.close()
        except IOError:
            print("Required file `project.csv` does not exist! Input project details first.")
        else:
            print("A schedule has been created.")

    def view_updated_schedule(self):
        """Prints the updated schedule of projects read from the `schedule.csv` file."""

        error_message = "Required file `project.csv` does not exist! Please create a schedule first."
        self.view_file('schedule.csv', error_message)

    # File handling reusable methods
    def __overwrite_schedule(self):
        """
        Creates and overwrites the `schedule.csv` file.
        Used when creating a schedule or getting a project from
        a schedule.
        """
        with open('schedule.csv', 'w', newline='') as schedule_file:
            csv_writer = csv.writer(schedule_file)
            csv_writer.writerow(["id", "title", "size", "priority"])
            for project in self.__schedule:
                csv_writer.writerow([project.get_id(),
                                     project.get_title(),
                                     project.get_size(),
                                     project.get_priority()]
                                    )

    @staticmethod
    def __overwrite_projects_file(file_name, project):
        """
        Overwrites a specified project-related file if it exists;
        otherwise, creates a new one.

        :param file_name: Project-related file
        :param project: `Project` object containing the details
        """

        # Field/Column names
        field_names = ["id", "title", "size", "priority"]

        # Check if projects.csv exist; if not then create a `project.csv`
        if not path.exists(file_name):
            create_file = open(file_name, 'w', newline='')
            csv_writer = csv.writer(create_file)
            csv_writer.writerow(field_names)
            create_file.close()

        # Open project.csv and append inputted project details
        with open(file_name, 'a+', newline='') as project_file:
            csv_writer = csv.DictWriter(project_file, fieldnames=field_names)
            csv_writer.writerow({"id": project.get_id(),
                                 "title": project.get_title(),
                                 "size": project.get_size(),
                                 "priority": project.get_priority()}
                                )

    @staticmethod
    def view_file(filename, error_message):
        """
        Reads a given file name and prints the formatted output.

        :exception: IOError
        """
        try:
            with open(filename, 'r') as row:
                print("{:<15}{:^10}{:>17}{:>21}".format("ID", "TITLE", "SIZE", "PRIORITY"))
                next(row)
                for col in row:
                    col = col.split(',')
                    print("{:<15}{:^10}{:>15}{:>20}".format(col[0],col[1],col[2],col[3]))
        except IOError:
            print(error_message)
