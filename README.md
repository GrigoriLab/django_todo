#TodoList

#commands for DB
CREATE DATABASE ToDolist;
SHOW DATABASES;
use ToDoList;
show tables;

#commands for django
python manage.py migrate
python manage.py makemigrations todos #before this we should add todos in setting.py->installed_apps
python manage.py sqlmigrate todos 0001
python manage.py migrate
python manage.py createsuperuser --username=name --email=e@mail.com

