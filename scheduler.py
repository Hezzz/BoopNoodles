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

        
        file.close()

    
    def viewUpdatedSchedule(self):
      schedule = self.schedule
      if not schedule:
        print("Please create a schedule first.")
      else:
        print("ID          TITLE          SIZE        PRIO")
        for project in schedule:
          print((project.get_id()+'          '+project.get_title()+'          '+project.get_size()+'          '+project.get_priority()))

          