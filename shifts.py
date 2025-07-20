from datetime import datetime, timedelta


class Shift:
    def __init__(self, name,start_hour, end_hour, off_time, duration_hours = None):
        self.name = name
        self.start_hour = datetime.strptime(start_hour, "%H:%M").time()
        self.end_hour = datetime.strptime(end_hour, "%H:%M").time()
        self.off_time = off_time
        self.hours = duration_hours if duration_hours else self.calculate_duration()

    def calculate_duration(self):
        today = datetime.today().date()
        start_dt = datetime.combine(today, self.start_hour)
        end_dt = datetime.combine(today, self.end_hour)
        if end_dt < start_dt:
            end_dt += timedelta(days=1)
        return (end_dt - start_dt).total_seconds() / 3600


    def working_hours(self):
        return self.calculate_duration() - self.break_duration()

    def break_duration(self):
        h, m = map(int, self.off_time.split(":"))
        return h + m / 60

    def __str__(self):
        return (
            f'{self.name}: {self.start_hour.strftime("%H:%M")} - {self.end_hour.strftime("%H:%M")}, '
            f'работни часове: {self.calculate_duration():.2f}, почивка: {self.off_time}'
        )



first_shift = Shift("4", "9:30", "19:30", "1:30")
first_shift_short_1 = Shift("5", "9:30", "18:00", "1:00")
first_shift_short_2 = Shift("26", "9:30", "18:30", "1:00")
second_shift = Shift("18", "10:30", "20:30", "1:30")
full_shift = Shift("20", "9:30", "20:30", "1:30")
holiday_shift = Shift("69", "10:30", "18:30", "1:00")

all_shifts = [first_shift_short_1, first_shift_short_2, first_shift, second_shift, full_shift]
first_shifts = [first_shift_short_2,first_shift_short_1,first_shift]
second_shifts = [second_shift,full_shift]
holiday_shifts = [holiday_shift]


# print(first_shift.name)
# print(first_shift.start_hour)
# print(first_shift.end_hour)
# print(first_shift.off_time)
# print(first_shift.calculate_duration())
# print(first_shift.working_hours())
# print(first_shift.break_duration())
