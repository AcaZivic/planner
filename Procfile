release: python manage.py makemigrations 
release: python manage.py migrate 
config: set DISABLE_COLLECTSTATIC=1
web: gunicorn planner.wsgi
