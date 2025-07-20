

class WorkDay:
    def __init__(self, date_obj, is_holiday=False, early_close=False, expected_rush=False):
        self.date = date_obj                      # datetime.date
        self.is_weekend = date_obj.weekday() >= 5 # проверява дали е събота или неделя True or False
        self.is_holiday = is_holiday             # ръчно маркирани официални празници
        self.early_close = early_close           # затваряме по-рано
        self.expected_rush = expected_rush       # офанзива – нужни повече хора
        self.shift_overrides = {}  # dict по име на смяна -> мин/макс хора

    def set_shift_override(self, shift_name, min_employees=None, max_employees=None):
        self.shift_overrides[shift_name] = {
            "min": min_employees,
            "max": max_employees
        }


