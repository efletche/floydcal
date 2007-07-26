#!/usr/bin/python


class manager:
    "Class that manages the calendar"
    listHead = 'null'
    def __init__(self):
        print 'new manager class instantiated'

    def addEntry(self, date, title):
        newEntry = entry(title)
        newEntry.date = date
        print 'entry added'
        print newEntry.title
        self.listHead = [newEntry]

    def addEntry(entry):
        print 'entry added'

    def editEntry(entry, title, location, time, duration):
        print 'entry changed'

    def removeEntry(entry):
        print 'entry deleted'

    def sort(date):
        print 'list re-sorted'

    def complete(entry):
        print 'task completed'

    def exportEntry(entry):
        print 'entry saved'

    print 'done'
