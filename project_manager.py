import csv
from project import Project


class ProjectManager:

    def __init__(self):
        self.__schedule = []

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
                    csv_writer.writerow([project.get_id(),project.get_title(),project.get_size(),project.get_priority()])
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
                    print(project.replace(",", "         "))
        except IOError:
            return False
        else:
            return True