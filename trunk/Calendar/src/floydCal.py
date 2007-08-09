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
        # Date Selection                                    @DateBlock
        self.previous = wx.Button(self, -1, "Previous")
        self.dateData = wx.StaticText(self, -1, "8/01/2007", style=wx.ALIGN_CENTRE)
        self.button_1 = wx.Button(self, -1, "Next")
        # ListCtrl Cal_ControlList - The date's tasks       @sizer_2
        listID = wx.NewId()
        self.Cal_ControlList = wx.ListCtrl(self, listID, style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|wx.SUNKEN_BORDER)
        # Edit(Add) Entry Panel                             @EntryData
        #Check box to complete an event
        self.isComplete = wx.CheckBox(self, -1, "")
        #Entry box for Title of event
        self.title = wx.TextCtrl(self, -1, "")
        #location label "takes place at":
        self.at = wx.StaticText(self, -1, "       at ")
        #Entry box for the location
        self.location = wx.TextCtrl(self, -1, "")

        #--Block for determining the time of an event--
        #Label with extra spaces preceeding to buffer between text and location box:
        self.Time = wx.StaticText(self, -1, "      Time:", style=wx.ALIGN_CENTRE)
        #Hours 0-23; 24-hour clock:
        self.hour = wx.SpinCtrl(self, -1, "", min=0, max=23)
        #Minutes 0-59:
        self.min = wx.SpinCtrl(self, -1, "", min=0, max=59)
        #Durations available in 15 minutes intervals:
        self.duration = wx.ComboBox(self, -1, choices=["", "15", "30", "45", "60", "75", "90", "105", "120", "135", "150", "165", "180", "195", "210", "225", "240", "255", "270", "285", "300"], style=wx.CB_DROPDOWN)
        #duration label (so the user knows what the box is for)
        #w/extra @ the end to make space for the submit button:
        self.inMinutes = wx.StaticText(self, -1, "minutes long   ")
        self.submit = wx.Button(self,wx.NewId(),"Submit")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        #intialize list control columns
        self.Cal_ControlList.InsertColumn(0,"Complete?",)
        self.Cal_ControlList.InsertColumn(1,"Title")
        self.Cal_ControlList.InsertColumn(2,"Location")
        self.Cal_ControlList.InsertColumn(3,"Time")
        self.Cal_ControlList.InsertColumn(4,"Duration")
        # event - list control on click / double-click
        self.currentItem = 0
        wx.EVT_LIST_ITEM_SELECTED(self, listID, self.onItemSelected)
        wx.EVT_LEFT_DCLICK(self.Cal_ControlList, self.onDoubleClick)
        # event - submitting an entry to the listctrl Cal_ControlList
        wx.EVT_BUTTON(self,self.submit.GetId(), self.pushSubmit)
        # event - selecting an entry to show on the Entry Panel
        # event - changing a date
        # event - menu events : export, exit, howto, about
        #wx.EVT_MENU(self, ID_EXPORT, self.exitCal) #TODO:export function
        wx.EVT_MENU(self, ID_EXIT, self.exitCal)
        #wx.EVT_MENU(self, ID_HOWTO, self.exitCal)  #TODO:Help Function?
        wx.EVT_MENU(self, ID_ABOUT, self.onAbout)
        wx.EVT_MENU(self, ID_EXPORT, self.onExport)


        ###SETUP DATA STRUCTURE###
        self.m = manager()

        #update view on listctrl at the end.("garbage collection")
        self.updateView()

    def __set_properties(self):
        # begin wxGlade: toDoList.__set_properties
        self.SetTitle("Floyd")
        self.SetSize((800, 450))
        self.isComplete.SetMinSize((30, 30))
        self.title.SetMinSize((120, 24))
        self.location.SetMinSize((120, 24))
        self.hour.SetMinSize((55, 25))
        self.min.SetMinSize((55, 25))
        self.duration.SetMinSize((60, 21))
        self.duration.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: toDoList.__do_layout
        listFrame = wx.BoxSizer(wx.VERTICAL)
        #Intializing Boxsizers
        entryData = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        dateBlock = wx.BoxSizer(wx.HORIZONTAL)
        #Placing GUI objects @dateBlock - The top section
        dateBlock.Add((0, 0), 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 60)
        dateBlock.Add(self.previous, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        dateBlock.Add(self.dateData, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        dateBlock.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
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
        entryData.Add(self.submit, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        listFrame.Add(entryData, 0, wx.EXPAND, 0)
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
        hr = self.hour.GetValue()
        mn = self.min.GetValue()
        thisTime = time(hr, mn)
        try:
            thisDur = int(self.duration.GetValue())
        except ValueError:
            thisDur = 0

        print "isComplete = " + str(thisComp)
        print "Title = " + thisTitle
        print "Location = " + thisLoc
        #print "hours = " + str(hr)
        #print "minutes = " + str(mn)
        print "Time = " + thisTime.isoformat()
        print "Duration = " + str(thisDur)

        #Create entry
        e = entry(thisTitle, date.today())
        e.location = thisLoc
        e.time = thisTime
        e.duration = thisDur
        e.isComplete = thisComp

        #Add to manager
        self.m + e      #'+' is overloaded to add an entry to a mangager
        self.updateView()

        print "GHAAAA!"

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

    def onExport(self, event):
        #!!!NEEDS TO BE CHANGED TO THE DATE SELECTED!!!
        self.m.export(date.today())

    def onItemSelected(self, event):
        #When user clicks on the entry on the list control, it should send the entry data to the entryplane
        self.currentItem = event.m_itemIndex
        pass

    def onDoubleClick(self, event):
        pass

    def updateView(self):
        self.Cal_ControlList.DeleteAllItems()
        if len(self.m.dateList) is not 0:
            for i in range(len(self.m.dateList[0][1])):
                dCom = self.m.dateList[0][1][i].isComplete
                dTitle = self.m.dateList[0][1][i].title
                dLoc = self.m.dateList[0][1][i].location
                dTime = self.m.dateList[0][1][i].time.isoformat()
                dDur = str(self.m.dateList[0][1][i].duration)
                #self.Cal_ControlList.InsertStringItem(i, "Title", dTitle)#[dCom, dTitle, dLoc, dTime, dDur])
                #Now fill the list
                self.Cal_ControlList.InsertStringItem(i, str(dCom))
                self.Cal_ControlList.SetStringItem(i, 1, dTitle)
                self.Cal_ControlList.SetStringItem(i, 2, dLoc)
                self.Cal_ControlList.SetStringItem(i, 3, dTime)
                self.Cal_ControlList.SetStringItem(i, 4, dDur)
                print "Printing entry :" , dCom, dTitle, dLoc, dTime, dDur

# end of class toDoList


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    toDoList = toDoList(None, -1, "")
    app.SetTopWindow(toDoList)
    toDoList.Show()
    app.MainLoop()
