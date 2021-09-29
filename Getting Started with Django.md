### Prerequisite

- Python 3
- Django

### Create a django admin project

```bash
django-admin startproject <project_name>
```

### Create a new app

```bash
python3 manage.py startapp <appname>
```

### Start the server

```bash
python3 manage.py runserver
```

### Creating a url path

#### Index path:

- Create your paths using the URL in your appname/urls.py and include it in the adminapp/urls.py so that it will be accessible when the server is run.

On the urls.py

```py
urlpatterns = [
  path('', views.index, name='index'),
]
```

On the views.py

```py
def index(request):
  return HttpResponse("This is my first url")
```

#### Specific path:

- Add in the path in the appname/urls.py and views.py

On the urls.py

```py
urlpatterns = [
  path('specific', views.specific, name='specific')
]
```

On the views.py

```py
def specific(request):
  return HttpResponse("This is the specific url")
```

### Get an dynamic value (id) and render HTML file:

- Add in th path on urls.py, views.py, settings.py and index.html

On the urls.py

```py
urlpatterns = [
  path('article/<int:article_id>', views.article, name='article')
]
```

On the views.py

```py
def article(request, article_id):
  return render(request, 'blog/index.html', {'article_id': article_id})
```

- Create an index.html file under appname/templates/appname/(file.html)

On the settings.py, add this in to see the render of file:

```py
INSTALLED_APPS = [
    'blog.apps.BlogConfig',
]
```
