import random

#---------------------------------------------declaring initial information--------------------------------

employees = ['Martin', 'Trifon', 'Filip', 'Ivailo', 'Evgeni', 'Jivko', 'Nikolay', 'Alex']
month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
shifts = ['1', '2']

# schedule = {'1': {'Martin':'1'}}

# for day in schedule.keys():         # въртим дните
#     print(day)                      # достъпваме датата от месеца
#     print(schedule[day])            # достъпваме служителите и смените за датата
#     for emp in schedule[day]:       # въртим служителите и смените
#         print(emp)                  # достъпваме служителя
#         print(schedule[day][emp])   # достъпваме смяната
#


# schedule.update({'1':{'Martin':'1'}})  # добавяме към речника

#--------------------------------------------declaring initial number---------------------------------------

working_days_in_month = 22
number_of_employees = len(employees)
off_days_in_month_for_employees = 10

#------------------------------------------calculating initial numbers -------------------------------------

max_number_of_employees_per_day =round((number_of_employees * (working_days_in_month - off_days_in_month_for_employees))
                                       / working_days_in_month)
max_number_of_type_of_shift_per_day = round(max_number_of_employees_per_day / 2)
max_number_of_type_of_shift_per_mont = round(working_days_in_month / len(shifts))
max_number_of_consecutive_work_days = round(working_days_in_month / 4)


# random_employee = random.choice(employees)

#--------------------------------------declaring dictionaries-------------------------------------------------

schedule = {}
consecutive_shifts = {}     # {'Martin': 0, 'Trifon': 0, 'Filip': 0, 'Ivailo': 0, 'Evgeni': 0, 'Jivko': 0, 'Nikolay': 0, 'Alex': 0}
employee_possible_shifts_for_month = {} # {'Martin': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2'],
working_days_in_month_for_employees = {} #{'Martin': 22, 'Trifon': 22, 'Filip': 22, 'Ivailo': 22, 'Evgeni': 22, 'Jivko': 22, 'Nikolay': 22, 'Alex': 22}


# ------------------------------------filling employees shifts for month------------------------------------------
def filling_employees_shift_for_month(employees_list):
    for employee in employees_list:
        consecutive_shifts.update({employee:0})
        working_days_in_month_for_employees.update({employee:22})
        employee_shifts = []
        employee_shifts.extend(11*'1')
        employee_shifts.extend(11*'2')
        employee_possible_shifts_for_month.update({employee:employee_shifts})
    return


#--------------------------------------calling function that fill days of month --------------------------------

filling_employees_shift_for_month(employees)


# schedule = {'1': {'Martin':'1'}}

#-------------------------------------------------filling schedule-----------------------------------------------

for date in month:
    shifts_for_day =['1','1','2','2']
    employees_left = [e for e in employees]
    schedule[date] = {}

    for _ in range(max_number_of_employees_per_day):
        random_employee = random.choice(employees_left)
        random_shift = random.choice(shifts_for_day)
        shifts_for_day.remove(random_shift)
        current_date = schedule[date]
        current_date.update({random_employee:random_shift})
        employees_left.remove(random_employee)


#--------------------------------------printing schedule-----------------------------------
for key in schedule.keys():
    print(schedule[key])








