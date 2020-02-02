FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/
COPY ./manage.py /code/
COPY ./docker/site /code/site
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000
ENV PORT 8000

ENV PYTHONUNBUFFERED 1
ENV PROCESSES 2
CMD ["/code/site/gunicorn_start"]
