
from os import name
from  login import User
from student import student
from admin import admin

class App:
    def __init__(self):
        self.user = None

    @staticmethod
    def first_page():
        print('[1] Login\n[q] Quit')
        return input('>>> please Select a choise :')

    
    def login_page(self):
        # role = {'1':'admin', '2':'student'}
        print("____Login____")
        print('  |  [1] admin\n  |  [2] student')
        r = input('  |__please select a role  : ')
        user_name = input('  |__please enter your user name : ')
        password = input('  |__please enter your password : ')
        
        if r == '1':
            self.user = admin('admin', user_name, password)
        elif r == '2':
            self.user = student(user_name, password)
        else:
            print('wrong role selected')
            return        
        return self.user.login()

    def admin_page(self):
        while True:
            print("________ Admin ________")
            print('  | [1] add course')
            print('  | [2] students List')
            print('  | [3] select student')
            print("  | [q] log out")
            user_input = input('  |__please select a choise  : ')
            if user_input == 'q':
                self.user.logout()
                break
            elif user_input == '1':
                title = input('title : ')
                professor = input('professor : ')
                unit = input('unit : ')
                capacity= input('capacity : ')
                major= input('major : ')
                self.user.define_course(title,professor,unit,capacity,major)
            elif user_input == '2':
                self.user.stu_list()
            elif user_input == '3':
                name = input('  |__please enter studdent name : ')
                r = self.user.select_student(name)
                if r:
                    print("___")
                    print('  |_[1] accept units')
                    print('  |_[2] Not-accept units')
                    print('  |_[3] back')
                    user_input = input('  |__please select a choise  : ')
                if user_input == '1':
                    self.user.check_stu_units(name, accept=True)
                elif user_input == '2':
                    self.user.check_stu_units(name, accept=False)

    def student_page(self):
        while True:
            print("________ student ________")
            print('  | [1] display courses')
            print('  | [2] choose course')
            print('  | [3] display taken courses')
            print("  | [q] log out")
            user_input = input('  |__please select a choise  : ')
            if user_input == 'q':
                self.user.logout()
                break
            elif user_input == '1':
                self.user.display_course()
            elif user_input == '2':
                course_title = input('Enter course title :')
                self.user.choose_course(course_title)
            elif user_input == '3':
                self.user.display_taken_course()
            

break_flag = True
while break_flag:
    user_input = App.first_page()
    if  user_input == 'q':
        break_flag = False
    elif user_input == '1':
        app = App()
        if app.login_page():
            if app.user.role == 'admin':
                app.admin_page()
            elif app.user.role == 'student':
                app.student_page()
        