from dataclasses import dataclass


@dataclass(frozen=True)
class ScrapeConfig:
    card_selector: str = "div.card-content"
    title_selector: str = "h2"
    company_selector: str = "h3"
    location_selector: str = "p"
    link_selector: str = "a"
