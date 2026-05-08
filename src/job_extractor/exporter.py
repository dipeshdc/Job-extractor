import json
from pathlib import Path
from typing import Iterable

from .models import JobListing


def export_json(jobs: Iterable[JobListing], output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    payload = [job.model_dump() for job in jobs]
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
