import random


class EmployeeWage_Problem:
    def __init__(self):
        self.num_of_working_days = 20
        self.is_full_time = 2
        self.is_part_time = 1
        self.emp_rate_per_hour = 20
        self.max_hrs_in_month = 100

    def total_working_hours(self):
        totalemphrs = 0
        totalworkingdays = 0
        while totalemphrs < self.max_hrs_in_month and totalworkingdays < self.num_of_working_days:
            totalworkingdays = totalworkingdays + 1
            empcheck = random.randint(0, 2)
            if empcheck == self.is_full_time:
                emphrs = 8
            elif empcheck == self.is_part_time:
                emphrs = 4
            else:
                emphrs = 0

            totalemphrs += emphrs
            print("Days :", totalworkingdays)
            print("EmpHrs: ", emphrs)

        totalempwage = totalemphrs * self.emp_rate_per_hour
        print("TotalEmployeeWage: ", totalempwage)
        print("TotalWorkingDays :", totalworkingdays)
        print("TotalEmpHrs: ", totalemphrs)


emp1 = EmployeeWage_Problem()
emp1.total_working_hours()