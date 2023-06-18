FROM python:3.9.16-bullseye
WORKDIR /app
COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip==23.0.1
RUN pip install --root-user-action=ignore requests
RUN pip install --no-cache-dir -r requirements.txt



CMD ["python3", "/app/main.py"]
