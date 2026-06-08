FROM python:3.12-alpine

COPY ./requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY --chmod=755 ./src /app

CMD [ "python", "/app/docker-app-complex.py" ]