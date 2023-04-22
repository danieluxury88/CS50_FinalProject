# 99 Hours - Personal Management Project

Organize and measure your daily life. Create cycles of time, define objectives and rules, and compare your growth.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Distinctiveness and Complexity](#distinctiveness-and-complexity)
- [Source file explanation](#source-file-explanation)
- [Usage](#usage)

## Project Description

**Personal (as Project) Management Django Web Project.**<br><br>
To know if you are going on the right direction you need to measure yourself, your achievements, your habits and your advance.<br>
Whenever you are ready to commit 99 hours of work (approx 4 days and 3 hours), start a cycle. If you have a clock that has chronometer that runs until 99 hours 59 minutes and 59 seconds start its count.<br><br>
In all the pages, a togglable timer in the navigation bar, and a bar will let you know how much time you have left.<br>
Define your current projects, milestones and tasks; set if dues milestones are due today or not. Also you can create independent tasks for chores outside your big goals.<br><br>
On main view (Today) you will see how is the day advancing. Any day is lost until is over. Also you will see how is current cycle (99 hours) advancing. If you toggle any of them, you can switch between elapsed/remaining time.
It is important to have a reminder what are you currently supposed to be doing, so if you a IN PROGRESS task, you will see it on the main page.

Your life is like a game, but you set your missions, your goals. On the MISSIONS page you can add your projects, its milestones and their tasks. You can edit them, and see its DUE DATE. On the TODAY view, you will see the milestones you have set DUE for TODAY, and its tasks.

You are measuring yourself, not need to lie. When you are ready to start a work session, click on the green START WORK SESSION button, but don't forget to click it back when you leave the desk.

But life is not only working, if you try to do it like you wont resist a long period of time. Maybe adding small habits like Meditation or Exercise, and control your pleasures and addictions as Videogames, register them ... will help you know where and how you are. Perhaps you believe something about yourself that your are not. You wont know until you measure it.

If you see how much can you do in 4 days, you will want to start a new Cycle again. Go to the REPORT views, where you will see how much have you done TODAY, YESTERDAY and on the CYCLE.<br><br>

## Technologies Used

- Django web framework:
   - functions and classed based views.
   - forms.
   - admin personalization.
   - models (including abstract model).
   - template tags.
   - template inheritance.
- Python
   - virtual environment.
- JavaScript
   - DOM Manipulation.
   - Fetch functions.
   - Async Functions.
- Bootstrap
   - Accordions.
   - Cards.
   - Icons.
   - Badges.
   - Navigation.
   - Responsive containers.
- Css

## Installation Instructions

- create virtual env **python -m venv env**
- activate virtual env **(.\env\Scripts\activate)**
- download packages **(pip install -r requirements.txt)**
- Run django migrations **(python manage.py makemigrations & python manage.py migrate)**
- change fake_env.txt to .env and fill SECRET_KEY, obtaining key from **python manage.py shell** and execute:

```
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

- create superuser **python manage.py createsuperuser**
- enter admin site and create EventTypes, and set them as regular (as Meditation, Exercise, Videogames, **etc**)

## Distinctiveness and Complexity

I created a project that I always wanted for myself; most Project Management platforms are mainly focused on Projects within Teams, but not on Personal Measurement. As this projects has emerged from my own needs, which I understand they may be also others in the same situation needs, I consider it is distinctive enough. Working as a freelancer or at home may be complex, since one can believe that it is not working enough. Impostor syndrome, procrastination, distractions, etc are the main enemies when working by oneself.<br>
The complexity of the project is on getting together multiple concepts of django frameworks and Pythona as using models with different layers as Projects-Milestones-Task, Habits and Addictions, and more abstract concepts related to time as Cycles and Work Sessions.
Some model queries where created on the models file, and others on the views; it was necessary to prefetch some additional data to obtain number of events of an event type.<br>
To create a the html, django template inheritance was used; **base.html** add some partials sections as **nav.html** and **footer.html**. Above base.html all pages are constructed, allowing to not duplicate html code.
Also on the html side, multiple template tags from django have been used, including creating custom format tags to convert how information is displayed, using crispy forms and timezone.<br>
On footer.html (djangoCycleData) and index.html (djangoData), some structure to pass some variables from django to javascript were created; this technique facilitate handling front side creation.<br>
On the javaScript side, functions to query backend data and update the DOM were used. Also some functions to update timers, create model objects and update object attributes.<br>

Bootstrap 5 was used to create the views. I used different components to display the information, ensuring all views are responsive.<br><br>
I built an MVP of a project I have done several times, but its the first time I do it using Web Development techniques. I had constructed similar systems like on paper, using Excel (sheets), Notion, but is the first time I obtain a good continue working above. Any existing Project Management platform I have used provided me features I needed for my context, and despite I consider there is plenty of features and functionalities to be added (I described some of them on the **About** view) I consider the project is more complex than the ones made during the course.



## Source file explanation

Project configuration is on **core** folder:
- settings.py: Project configuration. <br>
Used environ library to allow changing some configurations through external file (.env)<br>
Splitted INSTALLED_APPS intro three lists: DJANGO_APPS,THIRD_PARTY_APPS and PROJECT_APPS   <br>

- urls.py: project urls <br>
Included apps urls and favicon direction

- fake_env.txt: environmental file template<br>
Provided file to be used as template, that should be renamed to .env, replacing SECRET_KEY as explained on [Installation Instructions](#installation-instructions) section. <br><br>


Project is composed of 3 apps:
1. [Home](#home)
2. [Personal](#personal)
3. [Task](#tasks)

### Home
Application to obtain and display Tasks and Personal models data, and show it on 3 views: **TODAY**, **MISSIONS** and **REPORTS**

- Static folder: Contains JavaScript files to handle front view and request operations to backend, basic style.css and images as icons and favicon.

   - cycle-timer.js: file that control button to start a cycle, update bar and navigation timer, toggle bar and timer.<br>
   DOMContentLoaded: call functions to initiate view. <br>
   manageCycleElements: check if current cycle exists to display Start Cycle Button or Progress Bar.<br>
   updatePeriodicData: sets periodic functions interval; clock timer on nav bar is updated each 500ms and Cycle Bar each minute.<br>
   updateInternalVariables: sets internal variables: it is called on DOMLoaded and when a New Cycle creation response is received.<br>
   toggleCycleBar: allows changing from elapsed to remaining cycle time and viceversa.<br>
   updateNavCycleTimer: update cycle navigation clock.<br>
   calculateCycleProgressBarPercentage: calculates the percentage of cycle elapsed.<br>
   updateCycleProgressBar: updates cycle progress bar.<br>
   StartCycle: function to request server to create a new Cycle.<br>

   - day-timer.js: file that controls day timer. A day starts at 6 AM and ends at 10 PM.<br>
   DOMContentLoaded: call functions to initiate view, and add handlers <br>
   updateNavClock: updates Navigation bar clock.
   toggleDayInverted: allows changing from elapsed to remaining day time and viceversa.<br>
   calculateDayProgressBarPercentage: calculates the percentage of cycle elapsed.<br>

   - utils-update-time-components-functions: file that holds common function used by cycle-timer.js, day-timer.js and personal/work_cycle.js<br>
   updateProgressBar: gets the html elements ids and the data to update Day and Cycle bars<br>
   updateTimer: gets the html id to update cycle and day navigation clocks<br>
   startChronometer: function to display timer of work session clock.<br>


- Templates folder: contains html files, including base.html which includes partials (nav.html and footer.html)<br>

   - partials/footer.html: Includes footer html elements and calls to include javaScript files. Also passes django data to javaScript functions.<br>
   - partials/nav.html: Includes navigation bar and Day and Cycle bars.<br>
   - partials/messages.html: Includes support to display messages.<br>
   - about.html: Includes information of project, incoming features and contact.<br>
   - index.html: Home view. Includes In Progress Task, Goals, Work Sessions and Events Sections. Also on footer sends additional data to javaScript functions.<br>
   - missions.html: Missions view. Page to create new Projects, Milestones and Tasks. Also includes reference to All Tasks view.<br>
   - report.html: Template for Today, Yesterday and Cycle reports view.<br>
   - base.html: Template for all views, including the ones created on Task app. Joins navigation, body and footer sections.<br><br>

- Templatetags folder: contains format_data_tags.py file<br>
   - format_data_tags.py: file to present Enumeration attributes with their string representations. <br><br>

- urls.py: file to include all home views: index (TODAY), missions, today-report, yesterday-report, cycle-report and about<br>
- views.py: file to declare functions and class based views.<br>
   - index: function to render Home view. Sends current cycle, current work session, milestones which due date is TODAY, and Independent Tasks (tasks without a milestone) for today. Also includes the events for fast register.<br>
   - MissionView: class to log all Projects and all Independent Tasks. Also send Current cycle information.<br>
   - ReportView: class to create Today and Yesterday Report. Allows overriding which day will be required.<br>
   - TodayReportView: inherits from ReportView setting day to today.<br>
   - YesterdayReportView: inherits from ReportView setting day to yesterday.<br>
   - CycleReportView: class to query tasks, work sessions and events within current cycle.<br>
   - MyDefaultView: generic class view to pass current cycle information.<br>
   - AboutView: inherits from MyDefaultView to render about.html<br><br><br>


### Personal
Application to manage time (Cycle/Work Session) and event related (Event Type and Event) models<br>
- Static folder: Contains JavaScript file to handle Work Cycles and register Events.<br>

   - work-cycle.js: file that holds the logic to start/stop a work session by requesting operations on the server, and change Button appearance<br>
   DOMContentLoaded: register events and changes button appearance according if active work session exists.<br>
   StartWorkSession: request to create a WorkSession object, changing button appearance when receiving server response, and starting chronometer.<br>
   StopWorkSession: request to update WorkSession object by setting the end_time, changing button appearance when receiving server response and stopping chronometer.<br>

   - events.js: file that holds the register an event<br>
   RegisterEvent: request user to create a event according event type, and when response is received adds new element on list and increase counter.<br><br>

- models.py: file where Cycle, EventType, Event and WorkSession models are defined. <br><br><br>


### Tasks
Application to manage tasks (Project/Milestone/Task) models, and their views for creating, updating, deleting<br>
- Static folder: Contains JavaScript file to handle Tasks Milestones and Projects.<br>

   - task_handling.js:  file to sort, filter and update models.<br>
   filterListByTitle: allows filtering tasks according text input<br>
   sortListByDuration: allows sorting tasks according by duration<br>
   sortListByStatus: allows sorting tasks according by status<br>
   sortListByPriority: allows sorting tasks according by priority<br>
   filterListByStatus: allows filtering tasks according by status checkboxes<br>
   updateStatus: function to update task status from buttons<br>
   updateTaskDueDate: function to update task due date from list<br>
   updateMilestoneDueDate: function to update milestone due date from list<br><br>

- Templates folder: contains html files, including project, milestone and task views<br>
   - project_confirm_delete.html/milestone_confirm_delete.html/project_confirm_delete.html: files to ask user confirmation before deleting element.<br>
   - project_form.html: html file to create and update project. It list associated milestones.<br>
   - milestone_form.html: html file to create and update milestone. It list associated tasks.<br>
   - task_form.html: html file to create and update task.<br>
   - task_list.html: html to view all tasks within projects, and independent tasks. Allows filtering and sorting.<br><br>


- admin.py: Task admin view personalization.<br>
- models.py: File that contains one abstract model (WorkItem) and Project, Milestone and Task models which implement WorkItem abstract model.<br>
- urls.py: File that contains views and operations addresses. urlpatterns is splitted on multiple lists<br><br>
- view.py: File that contains classed base views for creating/updating Project/Milestone/Task models, and functions to alter models attributes.<br>
   - CurrentCycleMixin: generic class based view to pass current cycle information in other views<br>
   - ProjectCreateView: inherits from CurrentCycleMixin and CreateView, allows creating new Project.<br>
   - ProjectUpdateView: inherits from CurrentCycleMixin and UpdateView, allows modifying selected. Passes all associated milestones<br>
   - ProjectDeleteView: inherits from CurrentCycleMixin and DeleteView, ask for user confirmation to delete Project.<br>
   - MilestoneCreateView: allows creating new milestone.<br>
   - MilestoneUpdateView: allows modifying selected.<br>
   - MilestoneDeleteView: Ask for user confirmation to delete milestone.<br>
   - TaskCreateView: allows creating new task. Does not inherit from CurrentCycleMixin (for demonstration purposes)<br>
   - TaskUpdateView: allows modifying selected.<br>
   - TaskDeleteView: Ask for user confirmation to delete milestone.<br>
   - TaskListView: Inherits from ListView to list all tasks.<br>
   - update_task_status: receives request to update task status.<br>
   - update_task_due_date: receives request to update task due date.<br>
   - update_milestone_due_date: receives request to update milestone due date.<br><br><br>
   

### Scripts
   Folder to add scripts to be run django_extensions command for development.<br>
   - test.py: Python file to execute development tests. Run **python manage.py runscript test**<br><br>


- procedure.md: file that indicate the initial steps to create a Django project.


## Usage

1. Enter admin site and create EventTypes (here you will register your habits as Meditation, Exercise or addictions as VideoGames, Drugs, etc), and set them as regular.
2. On every view you will see at the top the navigation bar and two percentages bars.
   - Navigation bar clocks: A clock with current time, and current remaining/elapsed cycle time. If you a cycle is active you can toggle the cycle timer from elapsed to remaining.
   - The **DAY BAR** starts at 6 AM and ends at 10 PM.
   - The **CYCLE BAR** represents the 99 hours.
   - Navigation bar options: Today, Missions and Reports (Today, Yesterday, Cycle).<br><br>
3. The default view is the **Today** view, but maybe its a good idea to start on the **Missions** page.

   - Start by creating a Project (as CS50-Final Project).
   - Split the project in Milestones (as Create Use Cases, Define MVP, Create draft wireframe, etc).
   - Get the first milestone as set is DUE TODAY; split it again in multiple tasks.
   - Take the first task and set is status as IN PROGRESS; now this task will be the first thing you see on the TODAY view.
   - Every Milestone set as DUE TODAY will appear in the TODAY view.
   - If you want to see all tasks across multiples projects, including independent tasks you can click on the **VIEW ALL TASKS** option.<br><br>

4. Additionally, if you have some other relevant task outside your projects, you can add them on the MISSIONS view on the **INDEPENDENT TASKS** sections.
5. Organizing your tasks is already working, so may have prefer to have started a **WORK SESSION** on the **TODAY** view. But dont forget to stop it when you leave the desk.
6. You can register your **HABITS** on the TODAY view.
7. Finally you can take a look on your progress on the **REPORTS** views: **TODAY**, **YESTERDAY** and **CYCLE**; there you can check the **Milestones, Tasks, Work Sessions and Events** you have fulfill in those periods of time.

If you have any comment or suggestion, you can visit the **ABOUT** page on the footer, where you can see the upcoming plans and my GitHub profile, where you can contact me!
