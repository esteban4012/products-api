FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /project

COPY . .

RUN python -m pip install --upgrade pip setuptools

RUN pip install asgiref Django djangorestframework psycopg2-binary sqlparse

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



