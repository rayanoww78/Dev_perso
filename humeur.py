import psycopg2
params={
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "RAYANDU98",
}

def Humeur(humeur,raison):
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("INSERT INTO humeur(Humeur,raison) VALUES(%s,%s)",(humeur,raison))
    conn.commit()
    cur.close()
    conn.close()

