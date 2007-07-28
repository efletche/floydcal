
from datetime import date

class entry:
    "A basic to-do entry"
    title = ''
    isComplete = 0
    date = date(2007, 1, 1)

    def __init__(self, initTitle, initDate):
        self.title = initTitle
        self.date = initDate
        self.isComplete = 0

    def setDate(self, newDate):
        self.date = newDate

    def setTitle(self, newTitle):
        self.title = newTitle

class task(entry):
    "A basic entry w/no location or date"
    def __init__(self):
        if self.title == '':
            print 'ERROR, no name'

class errand(entry):
    location = ''
    def __init__(self, inputLocation):
        self.location = inputLocation

class event(entry):
    time = ''
    location = ''
    def __init__(self, inputTime):
        self.time = inputTime

class entryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
