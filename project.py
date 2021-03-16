class Project:
    """Project Class"""

    def __init__(self, project_id, title, size, priority):
        self.__project_id = project_id
        self.__title = title
        self.__size = size
        self.__priority = priority

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
        """Returns the project priority"""
        return self.__priority
