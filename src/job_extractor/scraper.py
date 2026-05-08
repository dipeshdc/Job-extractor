import logging
from typing import Iterable

from playwright.async_api import async_playwright

from .config import ScrapeConfig
from .models import JobListing

logger = logging.getLogger(__name__)


def _normalize_url(base_url: str, href: str | None) -> str:
    if not href:
        return base_url
    if href.startswith("http://") or href.startswith("https://"):
        return href
    return f"{base_url.rstrip('/')}/{href.lstrip('/')}"


async def scrape_jobs(
    url: str,
    config: ScrapeConfig | None = None,
    headless: bool = True,
) -> list[JobListing]:
    config = config or ScrapeConfig()

    logger.info("Starting scrape", extra={"url": url})
    jobs: list[JobListing] = []

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=headless)
        page = await browser.new_page()
        await page.goto(url, wait_until="domcontentloaded")
        await page.wait_for_selector(config.card_selector)

        cards = await page.query_selector_all(config.card_selector)
        for card in cards:
            title_el = await card.query_selector(config.title_selector)
            company_el = await card.query_selector(config.company_selector)
            location_el = await card.query_selector(config.location_selector)
            link_els = await card.query_selector_all(config.link_selector)
            
            # Get 2nd link (Apply) not 1st (Learn)
            link_el = link_els[1] if len(link_els) > 1 else (link_els[0] if link_els else None)

            title = (await title_el.text_content()).strip() if title_el else ""
            company = (await company_el.text_content()).strip() if company_el else ""
            location = (await location_el.text_content()).strip() if location_el else ""
            href = (await link_el.get_attribute("href")) if link_el else None

            job_url = _normalize_url(url, href)
            try:
                jobs.append(
                    JobListing(
                        title=title or "",
                        company=company or "",
                        location=location or "",
                        url=job_url,
                    )
                )
            except Exception as exc:
                logger.warning("Skipping card due to validation error: %s", exc)

        await browser.close()

    logger.info("Scrape completed", extra={"count": len(jobs)})
    return jobs
