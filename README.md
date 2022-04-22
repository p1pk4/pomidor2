# Example 2

pip install -r requirements.txt

- **Django==4.0.4**
- **psycopg2==2.9.3**
- **djangorestframework==3.13.1**
- **coverage==6.3.2**
- **django-filter==21.1**
- **social-auth-app-django==5.0.0**

**Add script for checks update dependencies in reqirements.txt:**
   > **python upgrade_pip.py**
>
**✔view:**
API endpoint для формирования данных на сервер, передача их клиенту и отрисовка этих данных на клиенте.
> queryset = объекты =  AllUsers.objects.all() # Cписок/срез объектов которые выводятся в запросе. В данном случае из AllUsers модели.
> serializer_class = поля этих объектов =  AllUsersSerializer # Из каких полей сформируется питон словарь, а потом уже json объект.
1. models.py (создаются миграции)
2. serializers.py (передаются поля для формирования питон словаря)
3. views.py (создаются ViewSets для каждой модели. Фильтры, сортировки, права доступа)
4. urls.py:
	- **для сервера** - во view.py пишется метод с render и именем html файла. - backend
	- **для клиента** - регистриуется router и указывается viewset. ```router.register('api/all_users', AllUsersViewSet)``` - frontend
	
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

**✔Filters:**
 * https://www.django-rest-framework.org/api-guide/filtering/
 * Модель из store.views.py:
   ``` 
   from django_filters.rest_framework import DjangoFilterBackend
   from rest_framework.viewsets import ModelViewSet

   from store.models import Book
   from store.serializers import BooksSerializer


   class BookViewSet(ModelViewSet):
      queryset = Book.objects.all()
      serializer_class = BooksSerializer
      filter_backends = [DjangoFilterBackend]
      filter_fields = ['price']
   ```
   **В settings.py утсанавливаем дефолтный формат выдачи данных у Django Rest Framework:**
   ```
   REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': (
         'rest_framework.renderers.JSONRenderer',
      ),
      'DEFAULT_PARSER_CLASSES': (
         'rest_framework.parsers.JSONParser',
      )
   }
   ```

   **Фильтрация и поиск:**
      + Если ищем по одному полю, то фильтра достаточно:
         - filter_fields = ['price']
      + Если ищем по двум полям тогда используем поиск(Например ищем значение 500 в поле "цена" и в поле "скидка":
         * search_fields = ['name', 'author_name']
      + Если нужна сортировка:
         - ordering_fields = ['price', 'author_name']

**✔Oauth:**
   * Как устроен oauth - https://www.digitalocean.com/community/tutorials/oauth-2-ru
   * https://python-social-auth.readthedocs.io/en/latest/configuration/django.html   
      +  добавил в settings.py настройки авторизации через социальные сети(в данном случае через Гитхаб)
      +  добавил функцию во view для отдачи html страницы
      +  добавил url для view в urls.py
         - Авторизованный пользователь отображается в админке Django 
         - 
 **✔Update:**
   + Add view for blog.html.  
   + Add path('blog/', blog) in urls.py
   + Add blog.html with GitHub authorization button with css

 **✔Update:**
   + Add ManyToMany model UserBookRelation 
   + Add serializer UserBookRelationSerializer with fields: like, in_bookmarks, rate
   + Add view UserBookRelationView **with lookup_field = 'book'**
   + Add url router.register(r'book_relation', UserBookRelationView)
