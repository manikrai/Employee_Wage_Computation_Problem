import random


class Employee_Total_Wages:
    def __init__(self):
        self.wage_per_hour = 20

    def working_hours_or_days(self):
        attendance = []
        category = []
        daily_wages = []
        hours_worked = 0
        days = 0
        total_wage = 0
        while True:
            days += 1
            if random.randint(0, 2) == 0:
                attendance.append('Absent')
            else:
                attendance.append('Present')
                if random.randint(0, 2) == 0:
                    category.append("Permanent")
                    total_daily_hours = 8
                    hours_worked += total_daily_hours
                    daily_wages.append(8 * self.wage_per_hour)
                    total_wage = total_wage + (self.wage_per_hour * total_daily_hours)

                else:
                    category.append("PartTime")
                    total_daily_hours = 4
                    hours_worked += total_daily_hours
                    daily_wages.append(4 * self.wage_per_hour)
                    total_wage = total_wage + (self.wage_per_hour * total_daily_hours)

            if days == 20 or hours_worked == 100:
                print("Month Completed")
                return attendance, category, days, hours_worked, daily_wages, total_wage, attendance.count("Present")

    def show_output(self):

        attendance, category, working_days, hours_worked, daily_wages, total_wages, present_days = self.working_hours_or_days()
        print("Wages For {} days = {}".format(present_days, total_wages))
        print("Employee was Present for {} out of {} working days for {} hours.".format(present_days, working_days,
                                                                                        hours_worked))
        print("Daily Wages : ", daily_wages)


emp1 = Employee_Total_Wages()
emp1.show_output()