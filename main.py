import datetime

from logic import generate_workdays
from employees import employee_list, Employee
from schedule import ScheduleGenerator
from shifts import all_shifts, Shift

date_format = "2025-07-12"

# formats in generator for working days
holidays_format= datetime.date(2025,7,1)
rush_format = datetime.date(2025,7,2)
early_close_format = datetime.date(2025,7,3)

employees = employee_list
work_days = generate_workdays(2025,7)
shifts = all_shifts

print(employee_list[0])
