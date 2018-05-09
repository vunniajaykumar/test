Problem statement
=========
 It's year 1945 and the Soviet forces need a network for co-ordinating on the
war effort. We are tasked with creating an app which can aid the Sovient
forces to oust the Axis power from their motherland.
You are the Lead engineer selected to design and develop this application.

Requirements
======

1. Python
2. Mysql
3. Django Framework


Installing
------

#### 1. Python 

Python can be obtained from [Here](https://www.python.org).
    
#### 2. Mysql

Mysql can be obtained as a pakage from Apache friends [here](https://www.apachefriends.org/download.html).
    
#### 3. Django Framework
	
Django can be installed after installing Python in __SHELL__ using below command
    
```
	pip install django
```

Setup
---

#### 1. Creating project

After completing installation please create a new django project using below command in __SHELL__ at your desired folder

```
	django-admin startproject projectname
```

#### 2. Copying files

Once you created your project open project folder and copy the folders named home,login,signup to your project folder.

#### 3. Editing setting.py

###### 1. Installing Apps

Open setting.py located in projectname/projectname/settings.py folder and add below lines in __INSTALLED_APPS__ .

```
	'home',
    'login',
    'signup',
```

###### 2. Adding Database

Create database and user in phpmyadmin and replace the below code in __DATABASE__ section

```
	'ENGINE': 'django.db.backends.mysql',
    'NAME': 'databsename',
    'USER': 'username',
    'PASSWORD': 'password',
    'HOST': '127.0.0.1',
```

replace the databasename,username,password with your databasename,username,password

###### 3. Making migrations

Making migrations basically means creating all of the required tables in databse it can be performed using below command in __SHELL__

```
	python manage.py makemigrations
    python manage.py migrate
```

###### 4. Creating Superuser

Create Superuser Using Bellow Command

```
	python manage.py createsuperuser
```

And follow the instructions


Runnin Server
--------

There is a in-biult development server in Django which can be run using below command

```
	python manage.py runserver
```

and go to [127.0.0.1:8000](127.0.0.1:8000) to view our website.
