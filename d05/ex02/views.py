from django.shortcuts import render
from django.conf import settings
import psycopg2

DB_PARAMS = settings.DATABASES.get("default", dict())
MOVIES = [
    {
        'episode_nb': 1,
        'title': 'The Phatom Menace',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '1999-05-19',
    },
    {
        'episode_nb': 2,
        'title': 'Attack of th Clones',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2002-05-16',
    },
    {
        'episode_nb': 3,
        'title': 'Revenge of the Sith',
        'director': 'George Lucas',
        'producer': 'Rick McCallum',
        'release_date': '2005-05-19',
    }
]

def work_with_db(query):
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
                cur.execute(query)
            conn.commit()
            status, message = True, None
    except Exception as ex:
        print(f"ERROR>{ex}")
        return False
    return True


def populate(request, table_name):
    values = str()
    for mv in MOVIES:
        values += f"""\
({mv.get("episode_nb", str())}, \
'{mv.get("title", str())}', \
'{mv.get("director", str())}', \
'{mv.get("producer", str())}', \
'{mv.get("release_date", str())}'),\
"""
        
    query = f"""
INSERT INTO {table_name} \
(episode_nb, title, \
director, producer, \
release_date) \
VALUES {values[:-1]} \
ON CONFLICT DO NOTHING;\
"""
    status = work_with_db(query)
    return render(request, "ex00/index.html", context={"status":status})