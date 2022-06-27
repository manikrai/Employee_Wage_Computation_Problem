import random


class monthly_wages:
    def calculate_monthly_wages(self):
        self.day_per_month = 20
        self.wage_per_hour = 20
        self.emphrs = 0
        self.empwage = 0
        self.monthly_wage = 0
        self.is_full_time = 2
        self.is_part_time = 1

        empcheck = random.randint(0, 2)
        if empcheck == self.is_full_time:
            print("Employee Is Working As Full-Time  \n")
            self.emphrs = 8
            self.empwage = self.emphrs * self.wage_per_hour
            self.monthly_wage = self.empwage * self.day_per_month
            print("Monthly Wage Of Permanent Employee Is :", self.monthly_wage)
        else:
            print("Employee Is Working As Part-Time \n")
            self.emphrs = 4
            self.empwage = self.emphrs * self.wage_per_hour
            self.monthly_wage = self.empwage * self.day_per_month
            print("Monthly Wage Of Non Permanent Employee Is :", self.monthly_wage)


emp1 = monthly_wages()
emp1.calculate_monthly_wages()