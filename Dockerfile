FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN alembic init alembic

COPY ./alembic /code/alembic
COPY ./app /code/app
COPY ./main.py /code

EXPOSE 8000

CMD ["python", "main.py"]