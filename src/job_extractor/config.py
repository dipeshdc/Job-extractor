from dataclasses import dataclass


@dataclass(frozen=True)
class ScrapeConfig:
    base_url: str = "https://realpython.github.io/fake-jobs/"
    card_selector: str = "div.card-content"
    title_selector: str = "h2.title"
    company_selector: str = "h3.subtitle"
    location_selector: str = "p.location"
    link_selector: str = "a.card-footer-item"
