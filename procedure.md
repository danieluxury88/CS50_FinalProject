1. Create virtual environment
```
python -m venv env
```
2. Add gitignore file (from toptal https://www.toptal.com/developers/gitignore/api/react,django,python)
3. Create and fill requirements.txt
4. Create repository
5. Activate virtual environment **(.\env\Scripts\activate)**
6. Run requirements.txt to install django **(pip install -r requirements.txt)**
7. Create django project **(django-admin startproject core .)**
8. Run django migrations **(python manage.py makemigrations & python manage.py migrate)**
9. Create superuser **(python manage.py createsuperuser)**
10. Test server **(python manage.py check & python manage.py runserver)**
11. Move keys to a separate file (to prevent uploading in repository)
    a. Create a .env file inside core folder
    b. Modify settings.py to use .env keys.
    c. Reorder settings.py
12. Add static folder with favicon.icon and add url route

13. Define apps & models.
