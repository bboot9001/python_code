#/usr/bin/dev python
#-*-coding:utf-8-*-
class Data(object):
    day   = 0
    month = 0
    year  = 0
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year  = year

    
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1
    
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


if __name__ == "__main__":
    date = Data.from_string('06-01-2017')
    is_date = Data.is_date_valid('06-01-2017')