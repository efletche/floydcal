#!/usr/bin/python
from datetime import date
from datetime import time
import os

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
        return tEntry


    def removeEntry(self, rmEntry):
        """Removes Entry"""
        if type(rmEntry) is not entry:
            #throw error
            try:
                raise entryException()
            except entryException, e:
                print 'ERROR, must pass an entry instance'
        else:
            for i in range(len(self.dateList)):
                if self.dateList[i][0] == rmEntry.date:
                    for j in range(len(self.dateList[i][1])):
                        if self.dateList[i][1][j] == rmEntry:
                            self.dateList[i][1].remove(rmEntry)
                            if len(self.dateList[i][1]) == 0:
                                self.dateList.remove(self.dateList[i])
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

    def export(self, target):
        mkTrunk = True
        for f in os.listdir('/'):
            if f == 'floydcal':
                mkTrunk = False
        if mkTrunk:
            os.mkdir('floydcal')

        targetDate = None
        if type(target) is entry:
            targetDate = target.date
        elif type(target) is date:
            targetDate = target
        else: print "ERROR, wrong datatype passed"

        yearString = str(targetDate.year)
        monthString = str(targetDate.month)
        dayString = str(targetDate.day)
        mkYear = True
        mkMonth = True
        mkDay = True
        for f in os.listdir('/floydcal'):
            if f == yearString:
                mkYear = False
                for g in os.listdir('/floydcal/'+yearString):
                    if g == monthString:
                        mkMonth = False
                        for h in os.listdir('/floydcal/'+yearString+'/'+monthString):
                            if h == dayString:
                                mkDay = False
                                break
                        break
                break
        if mkYear:
            os.mkdir('/floydcal/'+yearString)
        if mkMonth:
            os.mkdir('/floydcal/'+yearString+'/'+monthString)
        if mkDay:
            os.mkdir('/floydcal/'+yearString+'/'+monthString+'/'+dayString)


        path = '/floydcal/'+yearString+'/'+monthString+'/'+dayString

        if type(target) is entry:
            self.exportEntry(target, path)
        elif type(target) is date:
            for x in self.dateList:
                if x[0] == target:
                    for y in x[1]:
                        self.exportEntry(y, path)
                    break

        print 'entry saved'


    def exportEntry(self, entry, path):
        apNum = ''
        num = 0
        for i in os.listdir(path):
            if (entry.title+apNum+'.ics') == i:
                num+=1
                apNum = str(num)

        beginDateString = str(entry.date.year)+str(entry.date.month)+str(entry.date.day)
        endDateString = beginDateString
        if entry.time is not None:
            beginDateString = beginDateString+"T"+str(entry.time.hour)+str(entry.time.minute)+'00'

        if entry.duration is not None:
            hour = entry.time.hour
            min = entry.time.minute
            deltaHrs = entry.duration/60
            deltaMin = entry.duration - (deltaHrs*60)
            hour += deltaHrs
            min += deltaMin
            endDateString = endDateString +"T"+str(hour)+str(min)+'00'


        k = file(path+'/'+entry.title+apNum+'.ics', 'w')
        k.write("BEGIN:VCALENDAR\n")
        k.write("BEGIN:VTIMEZONE\n")
        k.write("TZID:Pacific/Honolulu\n")
        k.write("BEGIN:STANDARD\n")
        k.write("TZNAME:HST\n")
        k.write("END:STANDARD\n")
        k.write("END:VTIMEZONE\n")
        k.write("BEGIN:VEVENT\n")
        k.write("DTSTART:"+beginDateString+"\n") #begin date/time
        k.write("DTEND:"+endDateString+"\n") #end
        if entry.title is not None: k.write("SUMMARY:"+entry.title+"\n")
        if entry.location is not None: k.write("LOCATION:"+entry.location+"\n")
        k.write("END:VEVENT\n")
        k.write("END:VCALENDAR")
        k.close()
