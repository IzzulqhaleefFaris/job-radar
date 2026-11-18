import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(
    page_title="Job Radar",
    layout="wide"
)

st.title("🚀 Job Radar")

conn = psycopg2.connect(
    host="localhost",
    database="jobradar",
    user="jobradar",
    password="Izzulqf01"
)

query = """
SELECT
    id,
    title,
    company,
    location,
    source,
    score,
    status,
    notified
FROM jobs
ORDER BY id DESC
"""

df = pd.read_sql(query, conn)

total_jobs = len(df)

notified_jobs = len(
    df[df["notified"] == True]
)

saved_jobs = len(
    df[df["status"] == "Saved"]
)

applied_jobs = len(
    df[df["status"] == "Applied"]
)

new_jobs = len(
    df[df["status"] == "New"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Jobs", total_jobs)
col2.metric("New", new_jobs)
col3.metric("Saved", saved_jobs)
col4.metric("Applied", applied_jobs)

st.subheader("Jobs")

st.dataframe(
    df,
    use_container_width=True
)

st.subheader("Update Job Status")

job_id = st.number_input(
    "Job ID",
    min_value=1,
    step=1
)

new_status = st.selectbox(
    "Status",
    [
        "New",
        "Saved",
        "Applied",
        "Assessment",
        "Interview",
        "Offer",
        "Rejected"
    ]
)

if st.button("Update Status"):

    cur = conn.cursor()

    cur.execute("""
        UPDATE jobs
        SET status = %s
        WHERE id = %s
    """, (new_status, job_id))

    conn.commit()

    st.success("Status updated successfully!")

conn.close()
