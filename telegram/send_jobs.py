import os
import psycopg2
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

conn = psycopg2.connect(
    host="localhost",
    database="jobradar",
    user="jobradar",
    password="Izzulqf01"
)

cur = conn.cursor()

cur.execute("""
SELECT
    id,
    title,
    company,
    location,
    source,
    score
FROM jobs
WHERE notified = FALSE
""")

jobs = cur.fetchall()

for job in jobs:

    job_id = job[0]
    title = job[1]
    company = job[2]
    location = job[3]
    source = job[4]
    score = job[5]

    message = f"""
🔔 New Job Match

Position: {title}
Company: {company}
Location: {location}

Source: {source}
Score: {score}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )

    cur.execute("""
    UPDATE jobs
    SET notified = TRUE
    WHERE id = %s
    """, (job_id,))

conn.commit()

cur.close()
conn.close()

print("✅ Notifications sent")
