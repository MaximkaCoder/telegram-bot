FROM python:3.9
USER root

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install sqlite3 requests

COPY ./project /project
WORKDIR project

CMD ["python3", "/project/main.py"]
