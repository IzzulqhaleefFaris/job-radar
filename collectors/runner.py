from collectors.manual_collector import collect
from services.job_service import save_job
from services.telegram_service import send_job_notification

jobs = collect()

for job in jobs:

    inserted = save_job(job)

    if inserted:

        print(
            f"NEW JOB: {job.title}"
        )

        send_job_notification(job)

    else:

        print(
            f"DUPLICATE: {job.title}"
        )