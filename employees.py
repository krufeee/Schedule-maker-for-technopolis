from shifts import all_shifts, first_shifts, second_shifts


class Employee:

    def __init__(self, name:str, position:str, possible_shifts:list, preferred_shifts:list, full_time=True, days_off=None, vacation_days=None, egn= 1):
        self.name = name
        self.egn = egn
        self.position = position
        self.full_time = full_time
        self.days_off = set(days_off) if days_off else set()  #обекти
        self.vacation_days = set(vacation_days) if vacation_days else set() #обекти
        self.possible_shifts = possible_shifts      #обекти
        self.preferred_shifts = preferred_shifts    #обекти
        self.schedule = {}  # дата -> име на смяна
        self.total_hours = 0


    def __str__(self):
        contract = 8
        if not self.full_time:
            contract = 4
        return (
            f"""
Служител :{self.name}
На позиция {self.position}
Договор на {contract} часа
Смени на работа {[i.name for i in self.possible_shifts]}
Предпочитания за смяна {[i.name for i in self.preferred_shifts]}
Желани почивни дни - {self.days_off if  self.days_off else 'Няма'}
Отпуска  - {self.vacation_days if self.vacation_days else 'Няма'}
"""
                )


Martin = Employee("Мартин","Employee", all_shifts, first_shifts)
Trifon = Employee("Трифон","Employee", all_shifts, all_shifts)
Filip = Employee("Филип","Employee", all_shifts, all_shifts)
Jivko = Employee("Живко","Employee", all_shifts, all_shifts)
Evgeni = Employee("Евгени","Employee", all_shifts, all_shifts)
Nikolay = Employee("Николай","Employee", all_shifts, second_shifts)
ivajlo = Employee("Ивайло","Employee", all_shifts, all_shifts)
Aleks = Employee("Алекс","Employee", all_shifts, all_shifts)

employee_list = [Martin,Trifon,Filip,Jivko,Evgeni,Nikolay,ivajlo, Aleks]