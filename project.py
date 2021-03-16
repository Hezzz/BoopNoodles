class Project:
    """Project Class"""

    def __init__(self, project_id, title, size, priority):
        self.project_id = project_id
        self.title = title
        self.size = size
        self.priority = priority

    def get_id(self):
        """Returns the project id."""
        return self.project_id

    def get_title(self):
        """Returns the project title."""
        return self.title

    def get_size(self):
        """Returns the project size."""
        return self.size

    def get_priority(self):
        """Returns the project priority"""
        return self.priority
