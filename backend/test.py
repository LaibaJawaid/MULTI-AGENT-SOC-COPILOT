import psycopg

conn = psycopg.connect(
    host="127.0.0.1",
    port=5432,
    user="postgres",
    password="postgres",
    dbname="socdb",
)

print("✅ Connected Successfully!")
conn.close()