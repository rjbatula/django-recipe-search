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

### Create a model-view-controller

1. Create your paths using the URL in your <appname>/urls.py and include it in the <adminapp>/urls.py so that it will be accessible when the server is run.
