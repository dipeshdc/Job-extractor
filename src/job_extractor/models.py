from pydantic import AnyUrl, BaseModel, ConfigDict, Field


class JobListing(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    title: str = Field(..., min_length=1)
    company: str = Field(..., min_length=1)
    location: str = Field(..., min_length=1)
    url: AnyUrl
