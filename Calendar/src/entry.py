
from datetime import date
from datetime import time

class entry(object):
    "A basic to-do entry"
    title = None
    date = None
    location = None
    time = None
    isComplete = None
    duration = None
    def __init__(self, initTitle, initDate):
        self.title = initTitle
        self.date = initDate
        self.isComplete = False

    #defines the greater-than relationship between any two entries
    #   entries with no time or location (tasks) are the greatest, all tasks are equal
    #   entries with time (events) are the least, events are comparable by time
    #   entries with location and no time (errands) fall between, all errands are equal
    def __gt__(self, other):
        value = None
        if type(other) is not entry:
            print "ERROR! The second value is not an entry"
        else:
            if ((self.time is None) and (other.time is not None)) or ((self.location is None) and (other.location is not None)) or (((self.time is not None) and (other.time is not None)) and (self.time > other.time)):
                value = True
            else: value = False
        return value


class entryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
