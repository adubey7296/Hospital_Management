# Hospital Management System
A Hospital Management using Django Framework  

## Installation

- Clone this repo. `git clone <repo-url>`
- Create a virtualenv. `python3 -m venv <name>`
- Install requirements. `pip install Django==3.1.1`
- Install Sqlparse. ` pip install sqlparse`
- Install Pillow. `pip install Pillow`
- Install widget_tweaks. `pip install django-widget-tweaks`
- Make migrations. `python manage.py makemigrations`
- Apply migrations. `python manage.py migrate`
- Create a super user. `python manage.py createsuperuser`
- Run the server. `python manage.py runserver`

#### Important Things to do:
###### To enable widget_tweaks in your project you need to add it to INSTALLED_APPS in your projects settings.py file:(like this)
`INSTALLED_APPS = [
    ...'app_name',
    'widget_tweaks',
    ...
]`
#### Changes you have to do:
###### (provide your mail so that you will get mails)
`EMAIL_HOST_USER = 'xyz@gmail.com'`
`EMAIL_HOST_PASSWORD = 'xyz123'`
`EMAIL_RECEIVING_USER = 'xyz@mail.com'`
