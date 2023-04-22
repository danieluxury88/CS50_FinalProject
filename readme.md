# 99 Hours - Personal Management Project

Organize and measure your daily life. Create cycles of time, define objectives and rules, and compare your growth.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)

## Project Description

**Personal (as Project) Management Django Web Project.**<br><br>
To know if you are going on the right direction you need to measure yourself, your achievements, your habits and your advance.<br><br>
Whenever you are ready to commit 99 hours of work (approx 4 days and 3 hours), start a cycle. If you have a clock that has chronometer that runs until 99 hours 59 minutes and 59 seconds start its count.<br><br>
In all the pages, a togglable timer in the navigation bar, and a bar will let you know how much time you have left.<br>
Define your current projects, milestones and tasks; set if dues milestones are due today or not. Also you can create independent tasks for chores outside your big goals.<br><br>
On main view (Today) you will see how is the day advancing. Any day is lost until is over. Also you will see how is current cycle (99 hours) advancing. If you toggle any of them, you can switch between elapsed/remaining time.
It is important to have a reminder what are you currently supposed to be doing, so if you a IN PROGRESS task, you will see it on the main page.

Your life is like a game, but you set your missions, your goals. On the MISSIONS page you can add your projects, its milestones and their tasks. You can edit them, and see its DUE DATE. On the TODAY view, you will see the milestones you have set DUE for TODAY, and its tasks.

You are measuring yourself, not need to lie. When you are ready to start a work session, click on the green START WORK SESSION button, but don't forget to click it back when you leave the desk.

But life is not only working, if you try to do it like you wont resist a long period of time. Maybe adding small habits like Meditation or Exercise, and control your pleasures and addictions as Videogames, register them ... will help you know where and how you are. Perhaps you believe something about yourself that your are not. You wont know until you measure it.

If you see how much can you do in 4 days, you will want to start a new Cycle again. Go to the REPORT views, where you will see how much have you done TODAY.

## Technologies Used

- Django web framework:
   - functions and classed based views.
   - forms
   - admin personalization
   - models (including abstract model)
   - template tags
- Python
   - virtual environment
   - 
- JavaScript
- Bootstrap
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
The complexity of the project is on getting together multiple concepts with different layers as Projects-Milestones-Task, Habits and Addictions, and more abstract concepts related to time as Cycles and Work Sessions.

Use class based views.
Use native css.
Use django-rest-framework
Create 3 apps to split logic.

## Source file explanation

Project is composed of 3 apps:
1. Home
2. Personal
3. Tasks

### Home

## Usage

1. Enter admin site and create EventTypes (here you will register your habits as Meditation, Exercise or addictions as VideoGames, Drugs, etc), and set them as regultar.
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
