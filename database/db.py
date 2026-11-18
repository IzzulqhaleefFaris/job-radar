import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="jobradar",
        user="jobradar",
        password="Izzulqf01"
    )
