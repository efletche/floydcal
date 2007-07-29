#!/usr/bin/python
from datetime import date


class manager:
    """Class that manages the calendar"""
    #dateList essentially is the calendar
    #takes on the form of:
    #[[date(2007, 7, 20), [1, 2, 3]], [date(2007, 7, 21), [1, 2, 3, 4]], [date(2007, 7, 22), [1, 2]]]
    dateList = []
    def __init__(self):
        print 'new manager class instantiated'

    def addEntry(self, title, date):                     #Adds a new entry to a Calendar list
        """Adds the entry to the daylist"""
        newEntry = entry(title, date)
        if newEntry.title == '':
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'Nonexistant entry found :', e.value
        else:
            if len(self.dateList) == 0:                         #If there is nothing in the calendar yet
                    subList = [newEntry.date, [newEntry]]           #Add the first date and it's first entry
                    self.dateList.append(subList)
            else:
                for i in range(len(self.dateList)):                      #i indexes each date
                    #print self.dateList[i][0], "<-->", newEntry.date
                    if self.dateList[i][0] == newEntry.date:                 #If the new entry is of an indexed date
                        self.dateList[i][1].append(newEntry)                     #Add the entry to the end of the list for that day
                        break
                    elif self.dateList[i][0] > newEntry.date:                #If the new entry comes before an indexed date
                        subList = [newEntry.date, [newEntry]]               #Insert the new day and it's 1st entry
                        self.dateList.insert(i, subList)
                        break
                    elif i == (len(self.dateList)-1):                        #If the new entry comes after all indexed dates
                        subList = [newEntry.date, [newEntry]]               #Add the new day and it's 1st entry to the end
                        self.dateList.append(subList)
                        break
            print 'entry', newEntry.title, 'added'

    def editEntry(self, tEntry, title, location, time, duration):
        """edits specified entry in the list"""
        if tEntry == '':
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'Nonexistant entry found :', e.value
        else:
            for i in range(len(self.dateList)):    #i indexes each date
                    #print self.dateList[i][0], "<-->", newEntry.date
                    #If the new entry is of an indexed date
                    if self.dateList[i][0] == tEntry.date:    
                        for j in range(len(self.dateList[i][1])):
                            if dateList[i][0][j] == tEntry:
                                #edit entry if entry not null(none)
                                if title is not None:      tEntry.title = title 
                                if location is not None:   tEntry.location = location
                                if time is not None:       tEntry.time = time
                                if duration is not None:   tEntry.duration = duration
                                print 'entry ', tEntry.title, ' edited'
                                break
                            else:
                                print 'entry ', tEntry.title, ' not found'
                                break
                    #If the entry is at the end of the list
                    elif i == (len(self.dateList)-1):           
                        #subList = [newEntry.date, [newEntry]]               #Add the new day and it's 1st entry to the end
                        #self.dateList.append(subList)
                        print 'entry ', tEntry.title, ' not found'
                        break

            print 'entry changed'

    def removeEntry(self, entry):
        print 'entry deleted'

    def sort(self, date):
        for x in self.dateList:
            if x[0] == date:
                #sort x[1]
                print x[1]
        print 'list re-sorted'

    def complete(self, entry):
        print 'task completed'

    def exportEntry(self, entry):
        print 'entry saved'


