# DiplomaQ
Diploma management.

##Requirements
* Python 3

##Start django test server
1. Enter the project directory:
    ~~~
    $ cd DiplomaQ
    ~~~
2. Create virtual environment:
    ~~~
    $ python3 -m venv venv
    ~~~
3. Activate environment with:
    ~~~
    $ source venv/bin/activate
    ~~~
4. Install requirements:
    ~~~
    $ pip install -r requirements.txt
    ~~~
5. Create DB:
    ~~~
    $ python manage.py migrate
    ~~~
6. Populate users with command:
    ~~~
    $ python manage.py populate
    ~~~
    To see available options and command description:
    ~~~
    $ python manage.py populate -- help
    ~~~
7. Start django server with:
    ~~~
    $ python manage.py runserver 8000
    ~~~
8. Web app is available at http://127.0.0.1:8000/
9. At the end deactivate virtual environment:
    ~~~
    $ deactivate
    ~~~