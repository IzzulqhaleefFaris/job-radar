from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
INSERT INTO jobs
(title, company, location, source, score)
VALUES
(%s,%s,%s,%s,%s)
""", (
    "Technical Consultant",
    "Deloitte",
    "Kuala Lumpur",
    "JobStreet",
    28
))

conn.commit()

print("✅ Job saved successfully")

cur.close()
conn.close()
