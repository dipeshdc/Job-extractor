import sqlite3

from job_extractor.db import fetch_all_jobs, init_db, save_jobs
from job_extractor.models import JobListing


def test_save_jobs_inserts_unique_rows(tmp_path) -> None:
    db_path = tmp_path / "jobs.db"
    conn = sqlite3.connect(db_path)
    init_db(conn)

    jobs = [
        JobListing(
            title="Engineer",
            company="Example Co",
            location="Remote",
            url="https://example.com/job/1",
        ),
        JobListing(
            title="Engineer",
            company="Example Co",
            location="Remote",
            url="https://example.com/job/1",
        ),
    ]

    inserted = save_jobs(conn, jobs)
    stored = fetch_all_jobs(conn)
    conn.close()

    assert inserted == 1
    assert len(stored) == 1
