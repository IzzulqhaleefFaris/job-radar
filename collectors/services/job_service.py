import psycopg2


def save_job(job):

    conn = psycopg2.connect(
        host="localhost",
        database="jobradar",
        user="postgres"
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM jobs
        WHERE title = %s
        AND company = %s
        """,
        (
            job.title,
            job.company
        )
    )

    existing = cur.fetchone()

    if existing:

        cur.close()
        conn.close()

        return False

    cur.execute(
        """
        INSERT INTO jobs
        (
            title,
            company,
            location,
            salary,
            job_url,
            source
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            job.title,
            job.company,
            job.location,
            job.salary,
            job.job_url,
            job.source
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return True