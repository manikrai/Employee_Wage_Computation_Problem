import random


class Daily_Wage:
    def calculate_wage(self):
        self.wage_per_hour = 20
        self.is_full_time = 2
        self.is_part_time = 1
        self.emphrs = 0
        self.empwage = 0

        empcheck = random.randint(0, 2)
        if empcheck == self.is_full_time:
            print("Employee Is Working As Full-Time \n")
            self.emphrs = 8
            self.empwage = self.emphrs * self.wage_per_hour
            print("Employee Daily Wage Is :", self.empwage)
        else:
            print("Employee Is Working As Part-Time \n")
            self.emphrs = 4
            self.empwage = self.emphrs * self.wage_per_hour
            print("Employee Daily Wage Is :", self.empwage)


emp1 = Daily_Wage()
emp1.calculate_wage()