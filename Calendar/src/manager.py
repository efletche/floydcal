#!/usr/bin/python
from datetime import date


class manager(object):
    """Class that manages the calendar"""
    #dateList essentially is the calendar
    #takes on the form of:
    #[[date(2007, 7, 20), [1, 2, 3]], [date(2007, 7, 21), [1, 2, 3, 4]], [date(2007, 7, 22), [1, 2]]]
    #   where the lists of numbers([1, 2, 3]) represent lists of to-do items for the corresponding day
    dateList = []
    def __init__(self):
        print 'new manager class instantiated'
    def __add__(self, other):
        if type(other) is not entry:
            print "ERROR, cannot add anything but an entry to a manager"
        else:
            temp = self.addEntry(other.title, other.date)
            self.editEntry(temp, other.title, other.location, other.time, other.duration)

    def addEntry(self, title, date):                     #Adds a new entry to a Calendar list
        """Adds the entry to the daylist"""
        newEntry = entry(title, date)
        if newEntry.title == None:
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'Invalid entry: must have title'
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
        return newEntry

    def editEntry(self, tEntry, newTitle, newLocation, newTime, newDuration):
        """edits specified entry in the list"""
        for i in range(len(self.dateList)):
            if self.dateList[i][0] == tEntry.date:
                for j in range(len(self.dateList[i][1])):
                    if self.dateList[i][1][j] == tEntry:
                        #edit entry if entry not null(none)
                        if newTitle is not None:      tEntry.title = newTitle
                        if newLocation is not None:   tEntry.location = newLocation
                        if newTime is not None:       tEntry.time = newTime
                        if newDuration is not None:   tEntry.duration = newDuration
                        print 'entry', tEntry.title, 'edited'
                        break
            elif i == (len(self.dateList)-1):
                print 'entry', tEntry.title, 'not found'
                break
        self.sort(tEntry.date)
    def removeEntry(self, rmEntry):
        """Removes Entry"""
        if rmEntry is none:
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'Null entry :', e.value
        else:
            for i in range(len(self.dateList)):
            #remove entry
                self.dateList[i][1][j].remove(rmEntry)
                print 'entry deleted'
    def sort(self, date):
        for x in self.dateList:
            if x[0] == date:
                if len(x[1]) is 1:
                    break
                for y in range(1, len(x[1])):
                    for i in range(len(x[1])-y):
                        j = i + 1
            #if ((x[1][i].time is None) and (x[1][j].time is not None))
            #or ((x[1][i].location is None) and (x[1][j].location is not None))
            #or (((x[1][i].time and x[1][j].time) is not None)
                #and (x[1][i].time > x[1][j].time)):
                        if x[1][i] > x[1][j]:
                            temp = x[1][j]
                            x[1][j] = x[1][i]
                            x[1][i] = temp
                break
        print 'list re-sorted'
    def complete(self, entry):
        for i in range(len(self.dateList)):
            if self.dateList[i][0] is entry.date:
                for j in range(len(self.dateList[i][1])):
                    if self.dateList[i][1][j] is entry:
                        self.dateList[i][1][j].isComplete = True
                        break
                break
        print 'task completed'
    def exportEntry(self, entry):
        print 'entry saved'