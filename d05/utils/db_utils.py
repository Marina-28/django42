import psycopg2

def work_with_db(query, DB_PARAMS, SELECT=False):
    selected_fields = list()
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
                if SELECT:
                    selected_fields = cur.fetchall()
                    return True, selected_fields
            conn.commit()
            status = True,
    except Exception as ex:
        print(f"ERROR>{ex}")
        return False, None
    return True, None