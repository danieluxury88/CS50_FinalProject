ADD ABOUT & CONTACT
FIX CYCLE BUTTON ON OTHER PAGES
ADD EVENT TYPE REGISTER
REMOVE REPORTS APP

# 99 Hours - Personal Management Project

Organize and measure your daily life. Create cycles of time, define objectives and rules, and compare your growth.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)

## Project Description

Personal (as Project) Management Django Web Project.
To know if you are going on the right direction you need to measure yourself, your achievements, your habits and your advance.
Whenever you are ready to commit 99 hours of work (approx 4 days and 3 hours), start a cycle. If you have a clock that has chronometer that runs until 99 hours 59 minutes and 59 seconds start its count. In all the pages, a togglable timer in the navigation bar, and a bar will let you know how much time you have left.
Define your current projects, milestones and tasks; set if dues milestones are due today or not. Also you can create independent tasks for chores outside your big goals.
On main view (Today) you will see how is the day advancing. Any day is lost until is over. Also you will see how is current cycle (99 hours) advancing. If you toggle any of them, you can switch between elapsed/remaining time.
It is important to have a reminder what are you currently supposed to be doing, so if you a IN PROGRESS task, you will see it on the main page.

Your life is like a game, but you set your missions, your goals. On the MISSIONS page you can add your projects, its milestones and their tasks. You can edit them, and see its DUE DATE. On the TODAY view, you will see the milestones you have set DUE for TODAY, and its tasks.

You are measuring yourself, not need to lie. When you are ready to start a work session, click on the green START WORK SESSION button, but don't forget to click it back when you leave the desk.

But life is not only working, if you try to do it like you wont resist a long period of time. Maybe adding small habits like Meditation or Exercise, and control your pleasures as Videogames, and register your addictions ... will help you start. Maybe you believe something about yourself that your are not. You wont know until you measure it.

If you see how much can you do in 4 days, you will want to start a new Cycle again. Go to the REPORT views, where you will see how much have you done TODAY.

## Technologies Used

Django web framework
Python
JavaScript

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

## Distinctiveness and Complexity

Use class based views.
Use native css.
Use django-rest-framework
Create 3 apps to split logic.

## Source file explanation

## Usage

Explain how to use the project. Provide examples, screenshots, or links to live demos if applicable.
