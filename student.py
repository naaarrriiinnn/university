from login import User, log_event
from course import Course
import json
import os


class student(User):
    def __init__(self, username, password):
        super(). __init__("student", username, password)
        self.name = username
        self.stu_id = password
        self.major = self.stu_major()
        self.__total_units = 0
        self.total_units_status = False # must be 10< and <20
        self.taken_course = self.get_taken_courses() 
    
    @property
    def total_units(self):
        return self.__total_units

    @total_units.setter
    def total_units(self, value):
        self.__total_units = value
        self.limitation_course()
        with open(f"stu_taken_course\{self.name}.json", 'w+') as json_file:
                json.dump(self.taken_course, json_file)
    
    def limitation_course(self):
        if 10 <= self.total_units <= 20:
            self.total_units_status = True
            return
        self.total_units_status = False

    def get_taken_courses(self):
        if os.path.exists(f'stu_taken_course\{self.name+".json"}'):
            with open(f"stu_taken_course\{self.name}.json", 'r') as jp:
                d = json.load(jp)
            return d
        else:
            return {"nothing to show "}
    def choose_course(self, course_title):
        if course_title in self.taken_course.values():
            print(f">>> {course_title} is choosed recently")
        elif Course.any_capacity(course_title):
            res, unit = Course.choose_course(course_title)
            if res:
                self.taken_course[course_title] = "not Checked"
                self.total_units += int(unit)
                log_event(f"{course_title} course Selected by {self.name}")
                Course.save_db()
                return f">>> {course_title} course Selected Sucsesfully"
        else:
            return "No capacity"

    def display_course(self):
        print('_______ courses _______')
        print(*Course.display_courses(self.major), sep='\n')
        
    
    def display_taken_course(self):
        print('_____Taken courses_____')
        for c, s in self.taken_course.items():
            print(f"{c} | {s}")

        print('-------> total unit : ', self.total_units)
    
    def __str__(self):
        print('_____ student info _____')
        return f"name : {self.name}\nstudent number : {self.stu_id}\nmajor : {self.major}\ntotal units: {self.total_units}" \


    

