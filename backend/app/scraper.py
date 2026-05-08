import logging
from playwright.async_api import async_playwright

from app.models import JobListing
from app.config import ScrapeConfig

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

    logger.info(f"Starting scrape: {url}")
    jobs: list[JobListing] = []

    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(headless=headless)
            page = await browser.new_page()
            page.set_default_timeout(30000)
            page.set_default_navigation_timeout(30000)
            
            await page.goto(url, wait_until="networkidle")
            await page.wait_for_selector(config.card_selector)

            cards = await page.query_selector_all(config.card_selector)
            logger.info(f"Found {len(cards)} job cards")

            for idx, card in enumerate(cards):
                try:
                    title_el = await card.query_selector(config.title_selector)
                    company_el = await card.query_selector(config.company_selector)
                    location_els = await card.query_selector_all(config.location_selector)
                    link_els = await card.query_selector_all(config.link_selector)

                    # Get 2nd link (Apply) not 1st (Learn)
                    link_el = link_els[1] if len(link_els) > 1 else (link_els[0] if link_els else None)

                    title = (await title_el.text_content()).strip() if title_el else ""
                    company = (await company_el.text_content()).strip() if company_el else ""
                    location = (await location_els[0].text_content()).strip() if location_els else "N/A"
                    href = (await link_el.get_attribute("href")) if link_el else None

                    job_url = _normalize_url(url, href)

                    if title and company:
                        jobs.append(
                            JobListing(
                                title=title,
                                company=company,
                                location=location,
                                url=job_url,
                            )
                        )
                        logger.debug(f"✓ Card {idx+1}: {title}")
                except Exception as e:
                    logger.warning(f"✗ Card {idx+1} error: {e}")
                    continue

            await browser.close()

    except Exception as e:
        logger.error(f"Scraper error: {e}")
        raise

    logger.info(f"✓ Scrape completed: {len(jobs)} jobs extracted")
    return jobs
