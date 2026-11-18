from base import Job


def collect():

    jobs = [
        Job(
            title="Technical Consultant",
            company="Deloitte",
            location="Kuala Lumpur",
            salary="RM6000",
            job_url="https://example.com/job1",
            source="Manual",
        ),
        Job(
            title="Data Analyst",
            company="PETRONAS",
            location="Kuala Lumpur",
            salary="RM5500",
            job_url="https://example.com/job2",
            source="Manual",
        ),
        Job(
            title="Digital Transformation Consultant",
            company="Accenture",
            location="Kuala Lumpur",
            salary="RM8000",
            job_url="https://example.com/job3",
            source="Manual",
        ),
    ]

    return jobs
