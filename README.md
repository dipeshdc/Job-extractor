# Job Extractor

Async Playwright scraper that collects job listings and stores them in SQLite, with JSON export.

## Features
- Async Playwright scraping
- Pydantic models for validation
- SQLite persistence
- JSON export
- Logging
- Pytest tests

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Run
```bash
python -m job_extractor --url https://realpython.github.io/fake-jobs/ --db-path data/jobs.db --json-path data/output/jobs.json
```

## Tests
```bash
pytest
```

## Config
The default selectors target the Real Python fake jobs demo site. You can override the URL with `--url`.
