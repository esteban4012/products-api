FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /project
COPY requeriments.txt .
RUN pip install -r requeriments.txt
COPY ./api .
COPY docker-compose.yml .
COPY Dockerfile .
COPY manage.py .
# RUN python manage.py makemigrations
# RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
