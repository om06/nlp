# Audio Transcriber

The project is intended to convert audio to text.

**Technology used** 

 - Django 3
 - Celery
 - RabbitMQ
 - SQLite
 - HTML
 - CSS
 - Jqyery
 - JS

**Prequisites**
 - python3+
 - pip3
 - virtualenv
 - ubuntu16+
 - rabbitmq with a valid user, password and vhost

**Installation**

 - Clone the project using command 
 `[https://github.com/om06/nlp](https://github.com/om06/nlp)`
 
 - Add the rabbitmq user details in project's settings.py
 - Create a virtualenv using command 
  `virtualenv -p python3 env`
  
 - Activate virtualenv using command
  `source env/bin/activate`
  
 - Install requirements
  `pip install requirements/base.txt`
  
 - Migrate the database
 `python manage.py makemigrations`
  `python manage.py migrate`
 - Runserver
 - python manage.py runserver

