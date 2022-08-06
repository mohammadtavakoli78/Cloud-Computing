FROM python:3.8-alpine as base
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1

WORKDIR /app

RUN apk add --update \
    postgresql-dev \
    gcc \
    musl-dev \
    linux-headers \
    python3-dev \
    libpq-dev \
    postgresql \
    postgresql-contrib

COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

FROM python:3.8-alpine

COPY --from=base /app /app
COPY --from=base /usr/local/lib/python3.8/  /usr/local/lib/python3.8/
COPY --from=base /usr/local/bin/ /usr/local/bin/

ENV SERVER_PORT=${SERVER_PORT}
ENV EXPIRES_AFTER_SEC=${EXPIRES_AFTER_SEC}
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_URL=${DB_URL}
ENV DB_PORT=${DB_PORT}

WORKDIR /app
EXPOSE 8000

# for kubernetes
#CMD ["tail" , "-f" , "/dev/null"] //for debug
#CMD ["python" , "manage.py" , "migrate"]
#CMD ["python" , "manage.py" , "makemigrations"]
#CMD ["python", "manage.py" ,"runserver", "0.0.0.0:8000" , "--noreload"]

