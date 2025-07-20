import random

class ScheduleGenerator:
    def __init__(self, employees, workdays, shifts):
        self.employees = employees
        self.workdays = workdays
        self.shifts = {shift.name: shift for shift in shifts}  # dict за лесен достъп
        self.schedule = {}  # дата -> {смяна: [служители]}

    def generate_schedule(self):
        for day in self.workdays:
            self.schedule[day.date] = {}
            available_employees = self.get_available_employees_for_day(day)

            print(f"\n--- {day.date} ---")
            print("Налични служители:")
            for emp in available_employees:
                print(f"{emp.name} – възможни смени: {emp.possible_shifts}, предпочита: {emp.preferred_shifts}")

            for shift_name, shift in self.shifts.items():
                min_required = 5  # по подразбиране
                max_required = 10  # например

                # Проверка за override (например при офанзива)
                if shift_name in day.shift_overrides:
                    override = day.shift_overrides[shift_name]
                    min_required = override.get("min", min_required)
                    max_required = override.get("max", max_required)

                # Подбор на служители за тази смяна
                assigned = []
                candidates = [emp for emp in available_employees if shift_name in emp.possible_shifts]

                # Debug печат
                print(f"\nСмяна: {shift_name} — кандидати: {[e.name for e in candidates]}")

                random.shuffle(candidates)  # За разнообразие

                for emp in candidates:
                    if len(assigned) >= max_required:
                        break
                    if emp.schedule.get(day.date):
                        continue  # вече е на смяна днес
                    assigned.append(emp)
                    emp.schedule[day.date] = shift_name
                    emp.total_hours += shift.calculate_duration()

                self.schedule[day.date][shift_name] = [e.name for e in assigned]

                print(f"Назначени: {[e.name for e in assigned]} (нужно: {min_required}-{max_required})")

    def get_available_employees_for_day(self, day):
        available = []
        for emp in self.employees:
            if day.date in emp.days_off or day.date in emp.vacation_days:
                continue
            available.append(emp)
        return available

    def print_schedule(self):
        print("\n=== График ===")
        for date, shifts in self.schedule.items():
            print(f"\nДата: {date}")
            for shift_name, employee_names in shifts.items():
                print(f"  {shift_name}: {', '.join(employee_names)}")

    def print_employee_summary(self):
        print("\n=== Обобщение на служители ===")
        for emp in self.employees:
            print(f"{emp.name} — общо часове: {emp.total_hours}")
