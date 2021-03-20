import csv
from os import path
from project import Project


class ProjectManager:
    """
    Project Manager Class

    Handles project and scheduling function (e.g. creating and retrieving).
    """

    def __init__(self):
        # Schedule queue and Project dictionary, used for caching
        self.__schedule = []
        self.__projects = {}

        self._read_projects()
        self._read_schedule()

    def is_schedule_empty(self):
        """Checks if the schedule is empty."""

        return not self.__schedule

    def is_projects_empty(self):
        """Checks if there are any projects."""

        return not self.__projects

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

            if self.__projects.get(id_num):
                print("Project with the same ID already exists.")
            else:
                self.__projects[id_num] = project
                self.__overwrite_append(file_name='projects.csv', project=project)
                print("Project has been added.")
        except TypeError:
            print("Please input valid project details, try again.")

    def view_one(self, project_id):
        """
        Print the project details given an ID number.

        :exception: KeyError
        """

        try:
            project = self.__projects[project_id]
            print("{:<15}{:^10}{:>17}{:>21}{:>23}".format("ID", "TITLE", "SIZE", "PRIORITY", "STATUS"))
            print("{:<15}{:^10}{:>15}{:>20}{:>25}".format(project.get_id(),
                                                          project.get_title(),
                                                          project.get_size(),
                                                          project.get_priority(),
                                                          project.get_status(),
                                                          ))
        except KeyError:
            print("Project does not exist. Please try again")

    def view_completed(self):
        """Prints all the completed projects read from the `completed_projects.csv` file."""

        error_message = "Required file `completed_projects.csv` does not exist! Complete a project first."
        self.__view_file('completed_projects.csv', error_message)

    def view_all(self):
        """Prints all the projects received read from the `projects.csv` file."""

        error_message = "Required file `projects.csv` does not exist! Input project details first."
        self.__view_file('projects.csv', error_message)

    def get_project(self):
        """
        Gets the topmost project from the queue of scheduled projects.
        Adds that project to the list of completed projects then
        overwrites the schedule to the updated one.
        """

        # Print schedule then pop the topmost project.
        self.view_updated_schedule()
        project = self.__schedule.pop(0)
        project.change_status()

        # Print confirmation, add to the completed list.
        print("Project", project.get_title(), " has been removed from the schedule...")
        self.__overwrite_append(file_name='completed_projects.csv', project=project)
        self.__overwrite(file_name='projects.csv', project_list=self.__projects.values())
        print("Project", project.get_title(), " added to completed list...\n")

        # Overwrite the schedule and print the updated list.
        self.__overwrite(file_name='schedule.csv', project_list=self.__schedule)
        self.view_updated_schedule()

    def _read_projects(self):
        """
        Reads the `projects.csv` file and caches it in a dictionary for easy retrieval.

        :exception: IOError
        """
        try:
            print("Reading file, `projects.csv`...")
            with open('projects.csv', 'r', encoding='utf-8-sig') as file:
                table = csv.DictReader(file)
                for row in table:
                    self.__projects[int(row['id'])] = Project(int(row['id']), row['title'],
                                                              int(row['size']), int(row['priority']),
                                                              row['status'])
        except IOError:
            print("File `projects.csv` does not exist, no projects available yet.")
        else:
            print("Successfully read...")

    # Scheduling related functions
    def _read_schedule(self):
        """
        Get the old schedule read from the `schedule.csv` file.

        :exception: IOError
        """

        try:
            print("Reading file, `schedule.csv`...")
            file = open('schedule.csv', 'r', encoding='utf-8-sig')
            table = csv.DictReader(file)
            for row in table:
                self.__schedule.append(Project(int(row['id']), row['title'], int(row['size']),
                                               int(row['priority']), row['status']))
        except IOError:
            print("File `schedule.csv` does not exist, no schedule set yet.")
        else:
            print("Successfully read...")
            file.close()

    def create_schedule(self):
        """Creates a schedule of projects."""

        self.__schedule.clear()
        for project in self.__projects.values():
            if project.get_status() != 'DONE':
                self.__schedule.append(project)

        if not self.is_schedule_empty():
            self.__schedule.sort(key=lambda x: (x.get_priority(), x.get_size()))
            self.__overwrite(file_name='schedule.csv', project_list=self.__schedule)
            print("A schedule has been created.")

    def view_updated_schedule(self):
        """Prints the updated schedule of projects read from the `schedule.csv` file."""

        error_message = "Required file `project.csv` does not exist! Please create a schedule first."
        self.__view_file('schedule.csv', error_message)

    # File handling reusable methods
    @staticmethod
    def __overwrite(file_name, project_list):
        """
        Creates and overwrites the `schedule.csv` file.
        Used when creating a schedule or getting a project from
        a schedule.
        """
        with open(file_name, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(["id", "title", "size", "priority", "status"])
            for project in project_list:
                csv_writer.writerow([project.get_id(),
                                     project.get_title(),
                                     project.get_size(),
                                     project.get_priority(),
                                     project.get_status()]
                                    )

    @staticmethod
    def __overwrite_append(file_name, project):
        """
        Overwrites a specified project-related file if it exists;
        otherwise, creates a new one.

        :param file_name: Project-related file
        :param project: `Project` object containing the details
        """

        # Field/Column names
        field_names = ["id", "title", "size", "priority", "status"]

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
                                 "priority": project.get_priority(),
                                 "status": project.get_status()}
                                )

    @staticmethod
    def __view_file(filename, error_message):
        """
        Reads a given file name and prints the formatted output.

        :exception: IOError
        """
        try:
            with open(filename, 'r') as row:
                print("{:<15}{:^10}{:>17}{:>21}{:>23}".format("ID", "TITLE", "SIZE", "PRIORITY", "STATUS"))
                next(row)
                for col in row:
                    col = col.split(',')
                    print("{:<15}{:^10}{:>15}{:>20}{:>25}".format(col[0], col[1], col[2], col[3], col[4]))
        except IOError:
            print(error_message)
