import argparse
import logging
import sqlite3

from .config import ScrapeConfig
from .db import fetch_all_jobs, init_db, save_jobs
from .exporter import export_json
from .logging_config import setup_logging
from .scraper import scrape_jobs

logger = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scrape jobs and persist them.")
    parser.add_argument(
        "--url",
        default=ScrapeConfig().base_url,
        help="Target page with job listings.",
    )
    parser.add_argument("--db-path", default="data/jobs.db", help="SQLite DB path.")
    parser.add_argument(
        "--json-path",
        default="data/output/jobs.json",
        help="Output JSON path.",
    )
    parser.add_argument(
        "--headless",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Run browser in headless mode.",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Logging level (e.g. INFO, DEBUG).",
    )
    return parser.parse_args()


async def run() -> None:
    args = parse_args()
    setup_logging(args.log_level)

    logger.info("Starting job extractor")
    jobs = await scrape_jobs(url=args.url, headless=args.headless)

    conn = sqlite3.connect(args.db_path)
    init_db(conn)
    inserted = save_jobs(conn, jobs)
    stored_jobs = fetch_all_jobs(conn)
    conn.close()

    export_json(stored_jobs, args.json_path)
    logger.info("Completed", extra={"inserted": inserted, "total": len(stored_jobs)})


def main() -> None:
    import asyncio

    asyncio.run(run())


if __name__ == "__main__":
    main()
