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
    
    def display(self):
        return "{0}-{1}-{2}".format(self.month, self.day, self.year)

    
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def millenium(day, month):
        return Data(day, month, 2000)
    
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

class DateTime(Data):
    def display(self):
        return "{0}-{1}-{2}-00:00:00PM".format(self.month, self.day, self.year)
    


if __name__ == "__main__":
    date = Data.from_string('06-01-2017')
    is_date = Data.is_date_valid('06-01-2017')
    new_year = Data(1,1,2017)
    millenium_new_year = Data.millenium(1,1)
    string_new = Data.from_string('06-01-2017')

    print new_year.display()
    print millenium_new_year.display() 
    print string_new.display()
    print isinstance(new_year, Data)
    print isinstance(millenium_new_year, Data)
    print isinstance(string_new, Data)
    #查看硬编码的坏处

    print "The Difference ..........."
    new_year_DateTime = DateTime(1,1,2017)
    millenium_new_year_DateTime = DateTime.millenium(1,1)
    string_DateTime = DateTime.from_string('06-01-2017')

    print new_year_DateTime.display()
    print millenium_new_year_DateTime.display() 
    print string_DateTime.display()
    print isinstance(new_year_DateTime, DateTime)
    print isinstance(millenium_new_year_DateTime, DateTime)
    print isinstance(string_DateTime, DateTime)
