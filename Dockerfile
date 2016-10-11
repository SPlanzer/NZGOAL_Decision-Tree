FROM django
ADD . /my-django-app
WORKDIR /my-django-app
RUN pip install --proxy=127.0.0.1:3128 -r requirements.txt
CMD [ "python", "./manage.py runserver 127.0.0.1:8000" ]