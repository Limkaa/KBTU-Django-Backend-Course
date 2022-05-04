# KBTU-Django-Backend-Course

# Courses platform application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Limkaa/KBTU-Django-Backend-Course.git
$ cd KBTU-Django-Backend-Course
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip3 install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip3` has finished downloading the dependencies:

```sh
(env)$ cd project
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

At that stage, your django project is ready for launch

### Let's fill database with some random data

It is more interesting, when we already have some info to work with.
Actually, you can find in project directory, folder with name `mock_data`.
It is a test data to work with, there are also some images for future use.

So, for now, we need to generate data in database. For that purpose there are special custom command, which will start the process of creating information. To use that command:

```sh
(env)$ python manage.py fill_db_with_mock_data
```

```diff
+ Users number to generate (1-100):
  50 <- type your own number, it is just for example
+ Users successfully created
+ Categories successfully created

+ Course number to generate (1-100):
  35 <- type your own number, it is just for example
+ Courses successfully created
+ Memberships successfully created
+ Lessons successfully created
+ Lessons tasks successfully created
+ Reviews successfully created
+ Comments successfully created
+ News successfully created
```

So, finally, your database filled with mock data!

### Let's make easier testing API

For that purpose project root directory has `courses_platform.postman_collection.json`.
It is a file with all necessary API methods and other settings, which can be imported to your Postman. Just you for that 'import' option in Postman menu. After you successfully did this, we can go to next and final step!

### Let's run project

Type this in terminal:

```sh
(env)$ cd project
(env)$ python manage.py runserver
```

Then go to Postman and try to make your first API request for this project using Postman
Have fun :)
