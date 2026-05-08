import pytest
from pydantic import ValidationError

from job_extractor.models import JobListing


def test_job_listing_strips_whitespace() -> None:
    job = JobListing(
        title="  Engineer  ",
        company="  Example Co ",
        location="  Remote ",
        url="https://example.com/job/1",
    )

    assert job.title == "Engineer"
    assert job.company == "Example Co"
    assert job.location == "Remote"


def test_job_listing_invalid_url() -> None:
    with pytest.raises(ValidationError):
        JobListing(
            title="Engineer",
            company="Example Co",
            location="Remote",
            url="not-a-url",
        )
