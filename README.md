# pomidor2

pip install -r requirements.txt

- **Django==4.0.4**
- **psycopg2==2.9.3**
- **djangorestframework==3.13.1**



**✔Config:** 
   + PostgreSQL:
     * https://coderlessons.com/tutorials/bazy-dannykh/uchebnik-postgresql/7-sozdat-izmenit-dobavit-udalit-polzovatelia
     * https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04
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
```

**✔Serialize:**
   + в serializers.py есть модель BooksSerializer которая наследуется от класса Serializer из rest_framework.
   ```
   class BooksSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
   ```
      * Превращает поля в ключи словаря:
      > * [{"id":1,"name":"Number one","price":"1254.04"},{"id":2,"name":"Alladin","price":"123.32"}]

**✔Unittests:**
> SQL Shell (psql) - консоль PostgreSQL
> > -Подключаемся к БД которая указана в settings.py и в конcоли выдаем права пользователю: 
> > > ``` ALTER USER books_user CREATEDB; ```
   + Пользователем создается специальная БД для тестов. Обычно она после каждого тестирования удаляется.
   + Регрессионное тестирование.
   + python .\manage.py test store.tests
   - **Coverage.** Проверка покрытия кода тестами.
      > ``` coverage run --source='.' ./manage.py test . ```
      > > coverage report
      > > > coverage html - Визуальное отображение покрытия кода тестами (в корне проекта создается папка "htmlcov")
