# Overview

* This web project is make it to record a list of things we need to do every day. When the user run the server, the first page they will see is the list of task the user have record and saved in the database. On the top, there is a input form so the user type the task and then user can click on submit to record it and save in the database. The task will be show down the form as a list. 

* The propuse of this project is to work on my abilities coding a web page in Django. Also, this project is helpful on my daily life since I can use it to keep track of the things I need to do every day. 


[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

This web app has two pages:

* ***The first page*** shows to the users the list of tasks and they are also prompted to type a new task. On the top of the first page, the user is prompted to type the new task, and below that there is a button to submit it. When the users click on that the task is recorded and saved in the database. There are some columns that users can not see but they also are recorded such as the time they submit it and a boolean value if the task is complete or not.

* The second part of the web app has a list of tasks. There are some columns on this list. The first column has the task to do, the second column has the date-time when the users created or when the task has been modified, then the third, fourth, and fifth columns have buttons such as update, delete and complete a task. When users click on the update button, they are sent to another web page, which I will describe here later. Th delete button, delete the task from the list, and delete the record of the database. The complete button strikes the task text and also turns the text color to red. 
![First Page](/images/3.png)
<p>&nbsp;</p>

* ***The second page*** is the update page. On this page, the user will see the task they want to change and they can type or make changes in the input form. Then the users do click in submit and the change will be saved and shown in the list. 
![Second Page](/images/4.png)

# Development Environment


## Backend
* Used a virtual enviroment to create the Django project. 
* Django: Django is a Python-based free and open-source web framework that allow us to create web pages, and work with database 
* Used the sqlite database that comes with django project. 
## Frontend 
* Integrated and made some changes into the settings file to be able to use HTML and Css in the Django file
##### HTML integration
![Templates](/images/1.png)
##### CSS integration
![Static files](/images/2.png)
## Libraries 
* virtualenv : pip install virtualenv
* Django: pip install django
* To make changes in the database: python manage.py migrate
* To cerate the tables: python manage.py migrations [FILE NAME]
* To create and have access to the django admin page: python manage.py create superuser


# Useful Websites

* [Install First Django Project](https://www.geeksforgeeks.org/django-introduction-and-installation/?ref=lbp)
* [Setting Up a Django Project with SQlite](https://realpython.com/django-migrations-a-primer/)
* [Creat a Django project Video](https://www.youtube.com/watch?v=0CAXhbn0jA0&list=LL&index=32&ab_channel=CoolITHelp)


# Future Work

* Users will be able to record task by day and have acces to it
* User will have their account to get access
* Improve the Designb of the page . Use a check mark icon instead of a button