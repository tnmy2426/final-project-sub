WebsiteName: Event Management System for SUB Computing Club.
Developed by: Abdullah Al Nahdi, MD Didar Masud.

Commands used:

Virtual enviroment:
$ python -m venv env

Virtual enviroment activate:
$ .\env\Scripts\activate

Installation on local device:

-  Download & Install Python3.8 or later.
-  Download Project from GitHub.
-  From root directory create a virtual environment for our app.
-  Activate the virtual enviroment.
-  Then run this command:
   $ pip install -r requirements.txt

After runnig that command, all of our app depedencies will be installed in our virtual enviromnet.

Now, we have to create a database to connect with our application.

-  Download & Install PotgreSQL database.
-  Open pgAdmin and create a database.
-  In our main app(Directory name:EventManagement) will have a settings.py file, in that file we have to configure our database we just created.
-  After configuring database we have to run these command:
   $ python manage.py makemigrations
   $ python manage.py migrate

-  Now, we can create a superuser & run our app on our local server.
-  To create superuser run this command and give signup credentials.
   $ python manage.py createsuperuser

-  After creating superuser we can run our app on our locan server using this command:
   $ python manage.py runserver

   If we can complete these steps without any error, then our project will run on our local server.
