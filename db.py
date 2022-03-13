import psycopg2 as psy

#check database is connected
#connection = None
#try:
con = psy.connect(
    host = "localhost",
    database = "guru99",
    user = "postgres",
    password = "nezuko",
    port = "5432"
)
#except:
#    print('Database not connected.')

#cursors - vessel to communicate with db (NOTE: client/server side cursor types exist)
cur = con.cursor()

#execute query
cur.execute("select std_id, std_name from employees")

rows = cur.fetchall()

#print(rows)
for r in rows:
    print(f"std_id {r[0]} std_name {r[1]}")

#close cursor
cur.close()

#close
con.close()
