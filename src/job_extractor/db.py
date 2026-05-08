import sqlite3
from typing import Iterable

from .models import JobListing


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE
        )
        """
    )
    conn.commit()


def save_jobs(conn: sqlite3.Connection, jobs: Iterable[JobListing]) -> int:
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT OR IGNORE INTO jobs (title, company, location, url) VALUES (?, ?, ?, ?)",
        [(job.title, job.company, job.location, str(job.url)) for job in jobs],
    )
    conn.commit()
    return cursor.rowcount


def fetch_all_jobs(conn: sqlite3.Connection) -> list[JobListing]:
    rows = conn.execute("SELECT title, company, location, url FROM jobs").fetchall()
    return [JobListing(title=row[0], company=row[1], location=row[2], url=row[3]) for row in rows]
