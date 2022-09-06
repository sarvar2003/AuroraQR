FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential curl \
    libpq-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*


RUN addgroup --system django \
    && adduser --system --ingroup django django

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . .
RUN mkdir staticfiles
RUN python manage.py collectstatic --noinput --clear

RUN chown -R django:django /code
USER django

CMD gunicorn core.wsgi:application 
