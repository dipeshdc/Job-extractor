import json

from job_extractor.exporter import export_json
from job_extractor.models import JobListing


def test_export_json_writes_payload(tmp_path) -> None:
    jobs = [
        JobListing(
            title="Engineer",
            company="Example Co",
            location="Remote",
            url="https://example.com/job/1",
        )
    ]

    output_path = tmp_path / "jobs.json"
    export_json(jobs, output_path)

    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert data[0]["title"] == "Engineer"
    assert data[0]["company"] == "Example Co"
    assert data[0]["location"] == "Remote"
    assert data[0]["url"] == "https://example.com/job/1"
