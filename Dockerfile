FROM python:3.12

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chmod=755 src /app

CMD [ "python", "/app/docker-app-complex.py" ]