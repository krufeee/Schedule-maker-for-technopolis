import calendar
from datetime import date, timedelta
from datetime import datetime
from workdays import WorkDay

# ------------------------- days generator by year and month -------------------------------------------------------

def generate_workdays(year, month, holidays=None, early_closings=None, rush_days=None):
    if rush_days is None:
        rush_days = []
    if early_closings is None:
        early_closings = []
    if holidays is None:
        holidays = []
    _, num_days = calendar.monthrange(year, month)
    days = []
    for day in range(1, num_days + 1):
        d = date(year, month, day)
        wd = WorkDay(
            date_obj=d,
            is_holiday=d in holidays,
            early_close=d in early_closings,
            expected_rush=d in rush_days
        )
        days.append(wd)
    return days


#----------------------------------------calculate duration of shift-------------------------------------------


def calculate_duration(start_time, end_time):
    today = datetime.today().date()
    start_dt = datetime.combine(today, start_time)
    end_dt = datetime.combine(today, end_time)
    return end_dt - start_dt


#-------------------------------------time from string to time format timedelta-----------------------------------
def parse_duration(time_str):
    hours, minutes = map(int, time_str.split(":"))
    return timedelta(hours=hours, minutes=minutes)


#-------------------------------string to datetime.date ------------------------------------

def string_to_datetime(date_str):
      date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
      return date_obj