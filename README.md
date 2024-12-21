# Django CRUD App

## Introduction

a simple CRM(Customer Relationship Management) app using python django, css bootstap, sqlite for database
![CRM-DEMO](./assets/Screenshot%202024-12-21%20at%2008-55-50%20Django-CRM.png)

## Key Features:

- Authentication & Authorization:
Users can register and log in using Django's built-in UserCreationForm and AuthenticationForm classes.
- The @login_required decorator ensures that non-authenticated users can only access the Home, 
Register, and Login pages.
- Authenticated users gain access to the Dashboard as well as View, Add, Update, and Delete pages.
- For authenticated users, the default landing page is the Dashboard.
- CRUD Operations:
Perform Create, Read, Update, and Delete operations on records.
- Simple UI:
Built with HTML and Bootstrap CSS for an intuitive and clean interface, without using additional frontend frameworks.
- Database:
The application uses Django ORM to create databases and tables without requiring direct SQL queries.


# Getting Started

First clone the repository from Github and switch to the new directory:

```sh
$ git https://github.com/Youssef-Chibane/Django-CRM
$ cd Django-CRM
```

Create And Activate virualenv:

```sh
$ python -m venv venv
$ source venv/bin/activate
```  
    
Install project dependencies:

```sh
$ pip install -r requirements/local.txt
```  
    
Then simply apply the migrations:

```sh
$ python manage.py migrate
```   

You can now run the development server:

```sh
$ python manage.py runserver
```
