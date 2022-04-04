FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENV SECRET_KEY 988f1a680636d521d845768dc62a32f4b87b8155244c0eded1e493dbb88abdb9
ENV REDIS_URL redis://localhost:6379
ENV HOST 0.0.0.0
ENV LOG_LEVEL info

COPY ./app /code/app
COPY ./main.py /code

EXPOSE 8000

CMD ["python", "main.py"]