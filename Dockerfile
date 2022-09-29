FROM python:3.9
USER root

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install db-sqlite3 requests pytelegrambotapi schedule

COPY ./project /project
WORKDIR project

CMD ["python3", "/project/main.py"]
