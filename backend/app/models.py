from pydantic import BaseModel, AnyUrl


class JobListing(BaseModel):
    title: str
    company: str
    location: str
    url: AnyUrl

    class Config:
        str_strip_whitespace = True
