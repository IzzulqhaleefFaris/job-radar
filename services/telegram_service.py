import os
import requests

from dotenv import load_dotenv

load_dotenv()


def send_job_notification(job):

    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    print("BOT_TOKEN loaded:", bot_token is not None)
    print("CHAT_ID loaded:", chat_id is not None)

    message = f"""
🔔 New Job Found

🏢 Company:
{job.company}

💼 Position:
{job.title}

📍 Location:
{job.location}

💰 Salary:
{job.salary}

🔗 Link:
{job.job_url}

📌 Source:
{job.source}
"""

    try:

        response = requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            data={
                "chat_id": chat_id,
                "text": message
            },
            timeout=10
        )

        print("Status Code:", response.status_code)
        print("Response:", response.text)

    except Exception as e:

        print("Telegram Error:")
        print(e)