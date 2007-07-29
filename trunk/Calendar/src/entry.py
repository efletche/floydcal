
from datetime import date
from datetime import time

class entry:
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
        self.isComplete = 0


class entryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
