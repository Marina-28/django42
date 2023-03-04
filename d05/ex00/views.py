from django.shortcuts import render
from django.conf import settings
import psycopg2

DB_PARAMS = settings.DATABASES.get("default", dict())


{'ENGINE': 'django.db.backends.postgresql', 'NAME': 'django42', 'USER': 'django42', 'PASSWORD': 'marina', 'HOST': '127.0.0.1', 'PORT': '5432', 'ATOMIC_REQUESTS': False, 'AUTOCOMMIT': True, 'CONN_MAX_AGE': 0, 'CONN_HEALTH_CHECKS': False, 'OPTIONS': {}, 'TIME_ZONE': None, 'TEST': {'CHARSET': None, 'COLLATION': None, 'MIGRATE': True, 'MIRROR': None, 'NAME': None}}

def set_status(status, message):
    status = False
    message = "Не удалось получить данные для соединения с БД."
    return status, message

# Create your views here.
def init(request):

    if not DB_PARAMS:
        status, message = False, "Не удалось получить данные для соединения с БД."
    
    query = f"""\
CREATE TABLE IF NOT EXISTS ex00_movies \
(episode_nb INT PRIMARY KEY, \
title VARCHAR(64) NOT NULL UNIQUE, \
opening_crawl TEXT, \
director VARCHAR(32) NOT NULL, \
producer VARCHAR(128) NOT NULL, \
release_date DATE NOT NULL);"""
    try:
        with psycopg2.connect(
            database=DB_PARAMS.get("NAME", str()),
            user=DB_PARAMS.get("USER", str()),
            password=DB_PARAMS.get("PASSWORD", str()),
            host=DB_PARAMS.get("HOST", str()),
            port=DB_PARAMS.get("PORT", str())
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("drop table if exists ex00_movies;")
                cur.execute(query)
            conn.commit()
            status, message = True, None
    except Exception as ex:
        status, message = False, "Произошла ошибка при создании таблицы"
        print(f"ERROR>{ex}")
    
    return render(request, "ex00/index.html", context={"status":status, "message":message})