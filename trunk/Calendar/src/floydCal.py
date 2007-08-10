#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.5 on Mon Aug 06 15:38:58 2007 from C:\Documents and Settings\Owner\My Documents\School\ICS 413\413-Project\Calendar\src\gui\prototype2.wxg

import wx
from wxPython.wx import *
from manager import *
from datetime import date
from datetime import time


# Define ID's for event handling
ID_EXPORT = 200
ID_EXIT   = 201
ID_HOWTO  = 202
ID_ABOUT  = 203

class toDoList(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: toDoList.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        # Menu Bar
        self.toDoList_menubar = wx.MenuBar()
        self.SetMenuBar(self.toDoList_menubar)
        self.CreateStatusBar()
        menuBar = wx.Menu()
        menuBar.Append(ID_EXPORT, "Export", "Save file", wx.ITEM_NORMAL)
        menuBar.Append(ID_EXIT, "Exit", "Toodles (^_^)y", wx.ITEM_NORMAL)
        self.toDoList_menubar.Append(menuBar, "File")
        menuBar = wx.Menu()
        menuBar.Append(ID_HOWTO, "How To", "Instructions on how to use the task list", wx.ITEM_NORMAL)
        menuBar.Append(ID_ABOUT, "About", "Credits", wx.ITEM_NORMAL)
        self.toDoList_menubar.Append(menuBar, "Help")
        # Menu Bar end
        # -- DateBlock --- Date Selection
        self.previous = wx.Button(self, -1, "Previous")
        self.datepicker = wx.DatePickerCtrl(self, -1, style=wx.DP_DROPDOWN)
        self.next = wx.Button(self, -1, "Next")
        # -- sizer_2 -- ListCtrl Cal_ControlList - The date's tasks
        listID = wx.NewId()
        self.Cal_ControlList = wx.ListCtrl(self, listID, style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|wx.SUNKEN_BORDER)
        # -- EntryData -- Edit(Add) Entry Panel
        #Check box to complete an event
        self.isComplete = wx.CheckBox(self, -1, "")
        #Entry box for Title of event
        self.title = wx.TextCtrl(self, -1, "")
        #location label "takes place at":
        self.at = wx.StaticText(self, -1, "     at ")
        #Entry box for the location
        self.location = wx.TextCtrl(self, -1, "")

        #--Block for determining the time of an event--
        #Label with extra spaces preceeding to buffer between text and location box:
        self.Time = wx.StaticText(self, -1, "      Time:", style=wx.ALIGN_CENTRE)
        #Hours 0-23; 24-hour clock:
        self.hour = wx.SpinCtrl(self, -1, "", min=-1, max=23)
        self.hour.SetValue(-1)
        #Minutes 0-59:
        self.min = wx.SpinCtrl(self, -1, "", min=-1, max=59)
        self.min.SetValue(-1)
        #Durations available in 15 minutes intervals:
        self.duration = wx.ComboBox(self, -1, choices=["", "15", "30", "45", "60", "75", "90", "105", "120", "135", "150", "165", "180", "195", "210", "225", "240", "255", "270", "285", "300"], style=wx.CB_DROPDOWN)
        #duration label (so the user knows what the box is for)
        #w/extra @ the end to make space for the submit button:
        self.inMinutes = wx.StaticText(self, -1, "minutes long   ")
        self.submit = wx.Button(self,wx.NewId(),"Submit")
        self.edit = wx.Button(self,wx.NewId(),"Edit")
        self.remove = wx.Button(self,wx.NewId(),"Remove")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        #intialize list control columns
        self.Cal_ControlList.InsertColumn(0,"Complete?",)
        self.Cal_ControlList.InsertColumn(1,"Title")
        self.Cal_ControlList.InsertColumn(2,"Location")
        self.Cal_ControlList.InsertColumn(3,"Time")
        self.Cal_ControlList.InsertColumn(4,"Duration")
        # event - selecting (or deselecting) an entry to show on EntryData sizer on click
        self.currentItem = 0
        wx.EVT_LIST_ITEM_SELECTED(self, listID, self.onItemSelected)
        wx.EVT_LIST_ITEM_DESELECTED(self, listID, self.onItemDeselected)
        wx.EVT_LEFT_DCLICK(self.Cal_ControlList, self.onDoubleClick)
        # event - submitting an entry to the listctrl Cal_ControlList
        wx.EVT_BUTTON(self,self.submit.GetId(), self.pushSubmit)
        wx.EVT_BUTTON(self,self.edit.GetId(),self.pushEdit)
        wx.EVT_BUTTON(self,self.remove.GetId(),self.pushRemove)
        # event - changing a date
        wx.EVT_BUTTON(self,self.previous.GetId(),self.pushPrev)
        wx.EVT_BUTTON(self,self.next.GetId(),self.pushNext)
        wx.EVT_DATE_CHANGED(self, self.datepicker.GetId(),self.dateChanged)
        # event - menu events : export, exit, howto, about
        wx.EVT_MENU(self, ID_EXIT, self.exitCal)
        wx.EVT_MENU(self, ID_HOWTO, self.onHowTo)
        wx.EVT_MENU(self, ID_ABOUT, self.onAbout)
        wx.EVT_MENU(self, ID_EXPORT, self.onExport)


        ###SETUP DATA STRUCTURE###
        self.m = manager()

        #update view on listctrl at the end.("garbage collection")
        self.updateView()

    def __set_properties(self):
        # begin wxGlade: toDoList.__set_properties
        self.SetTitle("Floyd")
        self.SetSize((700, 450))
        self.datepicker.SetMinSize((150, 25))
        self.isComplete.SetMinSize((30, 30))
        self.title.SetMinSize((120, 24))
        self.location.SetMinSize((120, 24))
        self.hour.SetMinSize((55, 25))
        self.min.SetMinSize((55, 25))
        self.duration.SetMinSize((60, 21))
        self.duration.SetSelection(-1)
        self.remove.Enable(False)
        self.edit.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: toDoList.__do_layout
        listFrame = wx.BoxSizer(wx.VERTICAL)
        #Intializing Boxsizers
        entryData = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        dateBlock = wx.BoxSizer(wx.HORIZONTAL)
        buttons = wx.BoxSizer(wx.HORIZONTAL)
        #Placing GUI objects @dateBlock - The top section
        dateBlock.Add((0, 0), 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 60)
        dateBlock.Add(self.previous, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        dateBlock.Add(self.datepicker, 0, wx.LEFT|wx.RIGHT, 60)
        dateBlock.Add(self.next, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        dateBlock.Add((0, 0), 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 60)
        listFrame.Add(dateBlock, 0, wx.EXPAND, 0)
        #Placing GUI objects @sizer_2 - The middle
        sizer_2.Add(self.Cal_ControlList, 1, wx.EXPAND, 0)
        listFrame.Add(sizer_2, 1, wx.EXPAND, 0)
        #Placing GUI objects @entryData - The bottom section
        entryData.Add(self.isComplete, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        entryData.Add(self.title, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        entryData.Add(self.at, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        entryData.Add(self.location, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        entryData.Add(self.Time, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        entryData.Add(self.hour, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        entryData.Add(self.min, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        entryData.Add((0, 0), 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 25)
        entryData.Add(self.duration, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        entryData.Add(self.inMinutes, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0)
        buttons.Add(self.submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        buttons.Add(self.edit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        buttons.Add(self.remove, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        listFrame.Add(entryData, 0, wx.EXPAND, 0)
        listFrame.Add(buttons, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        # Layout Setup
        self.SetSizer(listFrame)
        self.Layout()
        self.Centre()
        # end wxGlade

    def pushSubmit(self, event):
        #event that submits the entry panel contents to listCtrl
        #self.Cal_ControlList.InsertStringItem(row, self.title) #TODO: replace row with variable
        #Initialize Variables
        thisComp = self.isComplete.GetValue()
        thisTitle = str(self.title.GetLineText(0))
        thisLoc = str(self.location.GetLineText(0))
        if thisLoc is '':
            thisLoc = None
        hr = self.hour.GetValue()
        mn = self.min.GetValue()
        if (hr or mn) is -1:
            thisTime = None
        else:
            thisTime = time(hr, mn)
        try:
            thisDur = int(self.duration.GetValue())
        except ValueError:
            thisDur = None
        thisDate = self.currentDate()

        print "isComplete = " + str(thisComp)
        print "Title = " + thisTitle
        print "Location = " + str(thisLoc)
        #print "hours = " + str(hr)
        #print "minutes = " + str(mn)
        if thisTime is not None: print "Time = " + thisTime.isoformat()
        print "Duration = " + str(thisDur)
        print "Date =" + thisDate.isoformat()

        #Create entry
        e = entry(thisTitle, thisDate)
        e.location = thisLoc
        e.time = thisTime
        e.duration = thisDur
        e.isComplete = thisComp

        #Add to manager
        self.m + e      #'+' is overloaded to add an entry to a mangager
        #thisEntry = self.m.addEntry(thisTitle, thisDate)
        #self.m.editEntry(thisEntry, None, thisLoc, thisTime, thisDur)
        #if thisComp is True:
        #    self.m.complete(thisEntry)

        self.updateView()

        self.clearValues()

        print "GHAAAA!"

    def pushEdit(self, event):
        index = self.Cal_ControlList.GetFocusedItem()
        thisComp = self.isComplete.GetValue()
        thisTitle = str(self.title.GetLineText(0))
        thisLoc = str(self.location.GetLineText(0))
        hr = self.hour.GetValue()
        mn = self.min.GetValue()
        if (hr or mn) is -1:
            thisTime = None
        else:
            thisTime = time(hr, mn)
        try:
            thisDur = int(self.duration.GetValue())
        except ValueError:
            thisDur = None
        thisDate = self.currentDate()

        for x in self.m.dateList:
            if x[0] == self.currentDate():
                print "ee",thisTitle,thisLoc
                self.m.editEntry(x[1][index], thisTitle, thisLoc, thisTime, thisDur)
                if thisComp is True:
                    self.m.complete(x[1][index])
                break

        self.submit.Enable(True)
        self.edit.Enable(False)
        self.updateView()
        self.clearValues()

    def pushRemove(self, event):
        """Removes the selected entry"""
        index = self.Cal_ControlList.GetFocusedItem()
        for x in self.m.dateList:
            if x[0] == self.currentDate():
                self.m.removeEntry(x[1][index])
                break
        self.submit.Enable(True)
        self.edit.Enable(False)
        self.remove.Enable(False)
        self.updateView()
        self.clearValues()
        pass

    #Goes back one day
    def pushPrev(self, event):
        #This is way overcomplicated, needs to be looked over for synergy with datepicker methods
        temp = self.currentDate()
        newDate = temp + datetime.timedelta(-1)
        dt = self.datepicker.GetValue()
        dt.SetMonth(newDate.month - 1)
        dt.SetDay(newDate.day)
        self.datepicker.SetValue(dt)
        self.updateView()

    #Advanced date forward 1 day
    def pushNext(self, event):
        #This is way overcomplicated, needs to be looked over for synergy with datepicker methods
        temp = self.currentDate()
        newDate = temp + datetime.timedelta(1)
        dt = self.datepicker.GetValue()
        dt.SetMonth(newDate.month - 1)
        dt.SetDay(newDate.day)
        self.datepicker.SetValue(dt)
        self.updateView()

    def exitCal(self, event):
        #Quits The program
        print "exit"
        self.Close(True)

    def onAbout(self, event):
        #Shows the "About" dialog box
        dlg = wx.MessageDialog(self, "Schleduling Program for ICS 413\n"
                              "2007 Eric Fletcher & Nathan Britton\n"
                              "Woot.",
                              "About FloydCal", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def onHowTo(self, event):
        dlg = wx.MessageDialog(self,
            "Fill the data fields on the bottom with the details of\n"
            "your event. The checkbox indicates whether the event has\n"
            "been completed, and the first data field is the name\n"
            "of the event.\n"
            "Click on an entry to edit or delete it.  ", "",
            wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def onExport(self, event):
        self.m.export(self.currentDate())

    def onItemDeselected(self, event):
        self.submit.Enable(True)
        self.edit.Enable(False)
        self.remove.Enable(False)

    def onItemSelected(self, event):
        #Grab text fields and assign them to variables
        index = self.Cal_ControlList.GetFocusedItem()
        sCom = self.Cal_ControlList.GetItem(index, 0).GetText()
        sTitle = self.Cal_ControlList.GetItem(index, 1).GetText()
        sLoc = self.Cal_ControlList.GetItem(index, 2).GetText()
        sTime = self.Cal_ControlList.GetItem(index, 3).GetText()
        sDur = self.Cal_ControlList.GetItem(index, 4).GetText()
        if sTime != '':
            #Taking the first two values from the isoformat string
            sHr = int(sTime[:2])
            #Taking the 3rd and 4th values for minutes
            sMn = int(sTime[3:5])

        #Display the data in the fields available
        if sCom == "True": self.isComplete.SetValue(True)
        else: self.isComplete.SetValue(False)
        self.title.SetValue(sTitle)
        self.location.SetValue(sLoc)
        if sTime != '':
            self.hour.SetValue(sHr)
            self.min.SetValue(sMn)
        self.duration.SetValue(sDur)

        #identify the entry that is selected

        self.submit.Enable(False)
        self.edit.Enable(True)
        self.remove.Enable(True)

    def onDoubleClick(self, event):
        pass

    def dateChanged(self, event):
        self.updateView()

    def updateView(self):
        self.Cal_ControlList.DeleteAllItems()
        if len(self.m.dateList) is not 0:
            for x in self.m.dateList:
                if x[0] == self.currentDate():
                    for i in range(len(x[1])):
                        dCom = x[1][i].isComplete
                        dTitle = x[1][i].title
                        dLoc = x[1][i].location
                        if dLoc is None:
                            dLoc = ''
                        dTime = x[1][i].time
                        if dTime is not None:
                            dTime = dTime.isoformat()
                        else:
                            dTime = ''
                        dDur = str(x[1][i].duration)
                        if dDur == "None":
                            dDur = ''
                        #Now fill the list
                        self.Cal_ControlList.InsertStringItem(i, str(dCom))
                        self.Cal_ControlList.SetStringItem(i, 1, dTitle)
                        self.Cal_ControlList.SetStringItem(i, 2, dLoc)
                        self.Cal_ControlList.SetStringItem(i, 3, dTime)
                        self.Cal_ControlList.SetStringItem(i, 4, dDur)
                        #print "Printing entry :" , dCom, dTitle, dLoc, dTime, dDur

    def clearValues(self):
        self.isComplete.SetValue(False)
        self.title.SetValue('')
        self.location.SetValue('')
        self.hour.SetValue(-1)
        self.min.SetValue(-1)
        self.duration.SetValue('')

    def currentDate(self):
        return date(self.datepicker.GetValue().GetYear(), (self.datepicker.GetValue().GetMonth() +1),self.datepicker.GetValue().GetDay())
# end of class toDoList


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    toDoList = toDoList(None, -1, "")
    app.SetTopWindow(toDoList)
    toDoList.Show()
    app.MainLoop()