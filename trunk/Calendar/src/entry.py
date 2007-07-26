class entry:
    "A basic to-do entry"
    def __init__(self, name):
        self.name = name
        self.isComplete = 0
        self.title = ''
        self.date = ''

class task(entry):
    "A basic entry w/no location or date"

class errand(entry):
    location = ''
    def __init__(self, loc):
        self.location = loc

class event(entry):
    time = ''
    location = ''

