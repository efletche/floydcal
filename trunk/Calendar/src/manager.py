#!/usr/bin/python

class manager:
    "Class that manages the calendar"
    listHead = []
    def __init__(self):
        print 'new manager class instantiated'
    def addEntry(self, date, title):
        """adds the entry to the daylist"""
        newEntry = entry(title)
        newEntry.date = date
        if newEntry.title == '':
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'Nonexistant entry found :', e.value 
        else:
            print 'entry added'
            print newEntry.title
            self.listHead = [newEntry]
    def addEntry(self, newEntry):
        print newEntry.title
    def editEntry(entry, title, location, time, duration):
        """edits specified entry in the list"""
        pEntry = entry(title)
        if pEntry == '':
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'Nonexistant entry found :', e.value 
        else:
            #edit entry
            print 'entry changed'
            pass
    def removeEntry(entry):
        print 'entry deleted'
    def sort(date):
        print 'list re-sorted'
    def complete(entry):
        print 'task completed'
    def exportEntry(entry):
        print 'entry saved'
    print 'done'
