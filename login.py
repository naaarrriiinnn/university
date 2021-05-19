import pandas as pd
import json
import datetime

def log_event(text):
    with open('log.txt', 'a') as fp:
        fp.write(f"[{datetime.datetime.now()}] {text}\n")


class User:
    admin_db  = pd.read_csv('account1.csv')
    student_db  = pd.read_csv('student1.csv')

    def __init__(self, role, username, password):
        self.username = username
        self.password = password
        self.role = role

    def login(self):
        if self.role == 'admin':
            print('>>>  admin login')
            if self.username in User.admin_db ['username'].values:
                r = User.admin_db [User.admin_db['username'] == self.username]['password'].tolist()[0]
                if str(r) == self.password:
                    print(f"'{self.username}' admin Logged in sucsessfully")
                    log_event(f"'{self.username}' admin Logged in sucsessfully")
                    return True
                else:
                    
                    log_event('wrong password')
                    print('wrong password')
                    return False
            else:
                log_event('wrong user name input')
                print('wrong user name input')
                return False

        elif self.role == 'student':
            print('>>>  student login')
            
            if self.username in User.student_db ['full_name'].values:
                r  = User.student_db [User.student_db['full_name'] == self.username]['stu_num'] == int(self.password)
                if r.bool():
                    print(f"'{self.username}' Logged in sucsessfully")
                    log_event(f"'{self.username}' Logged in sucsessfully")
                    return True
                else:
                    log_event('wrong password')
                    print('wrong password')
                    return False
            else:
                log_event('wrong user name input')
                print('wrong user name input')
                return False
        else:
            log_event("wrong role input")
            print('wrong role input')
            return False

    def logout(self):
        log_event(f"{self.username} Logged out")
        


    def stu_major(self):
        return User.student_db [User.student_db['full_name'] == self.username]['major'].tolist()[0]

    @staticmethod
    def stu_list():
        print(*User.student_db['full_name'].tolist(), sep='\n')


