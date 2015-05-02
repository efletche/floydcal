# Introduction #

Add your content here.


## Details ##
Revision Control:

-subversion repository hosted by Google Code


**Division of Work:**

Nathan: Interface design, GUI implementation

Eric: Event database management, task sorting


**iCal Progress:**

None as of yet


**Architecture:**

2 wyPython GUI windows:

Calendar window displays the days of the month. Days with events are marked, current date is highlighted.


Event window displays a checklist of tasks for the day. There wil be an option to save the event(s) of the day in an iCal format.

(Calendar GUI and iCal system low priority)


Calendar Class

variables

-currentDate

-Linked list of Date objects


Date Class

variables

-isActive

-hasEvent

-Linked list of Entry objects

functions

-sort()


Task Class

variables

-title

-isComplete

-date <-redundant data to allow an entry to be saved independent from it's list

functions

-complete()


Errand Class is-a Task

variables

-location


Event Class is-a Task

variables

startTime

duration

timeLeft

isExpired



&lt;optional&gt;



-location



**Explanation:**

The calendar system maintains a minimalist to-do list for every day. Tasks are arranged in order of importance with time sensitive tasks, or "events" at the top of the list (in temporal order), location sensitive "errands" with second priority and flexible tasks (that can be done anytime, anywhere) at the bottom of the list. Lists can be edited dynamically, and are sorted dynamically.


Each task has a title and the option to add a time, duration, and location. The interface makes it easy to add the information the user cares about without requiring erroneous data. The events are intrinsically linked to the associated date. All 5 minimum requirements are accounted for.