class entry:
    "A basic to-do entry"
    isComplete = 0
    title = ''
    date = ''

class task(entry):
    "A basic entry w/no location or date"

class errand(entry):
    location = ''
    def __init__(self, loc):
        self.location = loc

class event(entry):
    time = ''
    location = ''

