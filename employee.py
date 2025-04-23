class Employee:
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_wage(self):
        return self.hourly_rate * self.hours_worked
