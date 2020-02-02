FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
COPY manage.py /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD ['gunicorn --bind 0.0.0.0:37803 rewiza_services.wsgi']
