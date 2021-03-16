import csv
from project import Project
class Scheduler:
    schedule = []

    def __init__(self):
      self.schedule = []

        
    def createSchedule(self):
        schedule = self.schedule
        
        file = open('projects.txt','r',encoding='utf-8-sig')
        table = csv.DictReader(file)
        line_count = 0

        for row in table:
          if line_count == 0:
            schedule.append(Project(row['id'],row['title'],row['size'],row['priority']))
        schedule.sort(key=lambda x: (x.get_priority(), x.get_size()))
        with open('schedule.txt', 'w') as f:
          for project in schedule:
              f.write("%s\n" % (project.get_id()+'          '+project.get_title()+'          '+project.get_size()+'          '+project.get_priority()))
        
        file.close()

    
    def viewUpdatedSchedule(self):
        try:
            with open('schedule.txt', 'r') as schedule:
                print("ID          TITLE          SIZE        PRIO")
                for project in schedule:
                    print(project)
        except:
            print("Please create a schedule first.")
