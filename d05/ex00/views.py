from django.shortcuts import render
from django.conf import settings
import psycopg2

DB_PARAMS = settings.DATABASES.get("default", dict())

# Create your views here.
def init(request):
    
    query = f"""\
CREATE TABLE IF NOT EXISTS ex00_movies \
(episode_nb INT PRIMARY KEY, \
title VARCHAR(64) NOT NULL UNIQUE, \
opening_crawl TEXT, \
director VARCHAR(32) NOT NULL, \
producer VARCHAR(128) NOT NULL, \
release_date DATE NOT NULL);"""
    try:
        if not DB_PARAMS:
            raise Exception("Не удалось получить данные для соединения с БД.")
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
            status = True
    except Exception as ex:
        status = False
        print(f"ERROR> {ex}")
    
    return render(request, "ex00/index.html", context={"status":status})