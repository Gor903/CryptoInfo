FROM python:3-slim AS builder
ADD . /app
WORKDIR /app

# We are installing a dependency here directly into our app source dir
RUN pip install -r requirements.txt

CMD ["bash", "script.sh"]