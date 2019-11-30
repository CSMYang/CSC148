class Event:
    def __init__(self, day, month, year, desc):
        self.day = day
        self.month = month
        self. year = year
        self.description = desc

    def change_date(self, new_day, new_month, new_year):
        self.day = new_day
        self.month = new_month
        self.year = new_year

    def conflicts_with(self, other) -> bool:
        return self.day == other.day and self.day == other.day and \
                self.year == other.year
