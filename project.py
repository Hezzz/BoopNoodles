class Project:
    """Project Class"""

    def __init__(self, project_id, title, size, priority, status="INC"):
        self.__project_id = project_id
        self.__title = title
        self.__size = size
        self.__priority = priority
        self.__status = status

    def get_id(self):
        """Returns the project id."""
        return self.__project_id

    def get_title(self):
        """Returns the project title."""
        return self.__title

    def get_size(self):
        """Returns the project size."""
        return self.__size

    def get_priority(self):
        """Returns the project priority."""
        return self.__priority

    def get_status(self):
        """Returns the project's status."""
        return self.__status

    def change_status(self, status="DONE"):
        """Set the status of the project."""
        self.__status = status
