import random


class checking_attendance:
    def attendance(self):
        empcheck = random.randint(0, 1)
        if empcheck == 1:
            print("Employee Is Present")
        else:
            print("Employee Is Absent")


emp1 = checking_attendance()
emp1.attendance()
