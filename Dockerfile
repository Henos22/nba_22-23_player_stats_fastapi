FROM python:3.10
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./season_stats.csv /code/season_stats.csv

RUN pip install -r requirements.txt

COPY ./app /code/app

CMD ["uvicorn","app.main:app", "--host", "0.0.0.0", "--port", "80"]