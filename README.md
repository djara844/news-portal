# NEWS PORTAL

### Test for T&T Interactiva

Create news system.

## Previous requirements

Python (recommended version Python 3.9.10)

Virtualenv (recommended version virtualenv 20.14.1)

## Quick installation with sqlite db

1 Clone repo https://github.com/djara844/news-portal.git

```bash
git clone https://github.com/djara844/news-portal.git
```
2 Inside the news-portal folder create virtual environment

```bash
virtualenv ven
```

3 Activate virtual environment

```bash
source ./ven/bin/activate
```

4 Install libraries from the file requirements.txt

```bash
pip install -r requirements.txt
```

5 Inside the folder newsportal run migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## Installation with postgresql

1 Comment out the following lines in the settings.py file:

    DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
        }
    }

2 Uncomment the following lines in the settings.py file:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "newsportal",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
        }
    }

3 Create in postgres the database with the name:
    
    newsportal

4 In settings.py customize the fields, according to your configuration

    "USER": "Your user",

    "PASSWORD": "Your password",


5 Inside the newsportal folder run migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```


## Usage

6 Run the project

```bash
python manage.py runserver
```

7 Enter the link


`<link>` : <http://127.0.0.1:8000/>

8 To create, edit or delete news create user for django admin (run command in newsportal folder) and fill in the data

```bash
python manage.py createsuperuser
```

9 Login to django admin

`<link>` : <http://127.0.0.1:8000/admin/>