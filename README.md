# pomidor2

pip install -r requirements.txt

- **Django==4.0.4**
- **psycopg2==2.9.3**


**✔Config:**
  > settings.py: 
    > > PostgreSQL:
    > > > https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04
   ``` 
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'fooks_db',
          'USER': 'books_user',
          'PASSWORD': '123',
          'HOST': 'localhost',
          'PORT': '',
      }
    } 
