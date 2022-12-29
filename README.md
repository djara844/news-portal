# NEWS PORTAL

#### Test for T&T Interactiva

Create news system

## Requerimientos previos

Python
Virtualenv

## Instalación

1 Clonar repo https://github.com/djara844/news-portal.git

git clone https://github.com/djara844/news-portal.git

2 Dentro de la carpeta news-portal crear envorno virtual

virtualenv ven

3 Activar entorno vrtual

source ./ven/bin/activate

4 Instalar librerias del archivo requirements.tx

pip install -r requirements.txt

5 Dentro de la carpeta newsportal ejecutal migraciones

python manage.py makemigrations

python manage.py migrate

## Instalación with postgresql

Comentar en el archivo settings.py 

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3",
    }
}

Descomentar en el archivo settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "newsportal",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
    }
}

Crear en postgress la base de datos newsportal

Dentro de la carpeta newsportal ejecutal migraciones

python manage.py makemigrations

python manage.py migrate



### Usage

6 Correr el proyecto

python manage.py runserver

7 Ingresar en el link http://127.0.0.1:8000/

8 Para crear, editar o eliminar news crear usuario para admin de django (ejecutar comando en la carpeta newsportal)

python manage.py createsuperuser

Ingresar al admin de django http://127.0.0.1:8000/admin/
