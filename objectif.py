import psycopg2
params={
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "RAYANDU98",
}
def dev_perso(objectif,priorite,temps_estime,deadline):
    conn = psycopg2.connect(**params)
    if priorite <= 1 or priorite>5:
        priorite = int(input("Sur un ordre de 1 à 5 quel est la priorité de ton objectif : "))
    if temps_estime <= 1:
        temps_estime = int(input("En nombre d'heure quel est le temps estimé de cette tâche : "))
    cur = conn.cursor()
    cur.execute("INSERT INTO taches(objectif,deadline,priorite,temps_estime) VALUES(%s,%s,%s,%s)",(objectif,deadline,priorite,temps_estime))
    conn.commit()
    conn.close()
    cur.close()
    return objectif, priorite, temps_estime
