from fastapi import APIRouter, HTTPException, Query
import logging

from app.scraper import scrape_jobs

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["scraper"])


@router.get("/scrape")
async def scrape(url: str = Query(..., description="URL to scrape jobs from")):
    """
    Scrape jobs from the provided URL.
    
    **Parameters:**
    - `url`: The URL of the job listing page
    
    **Returns:**
    - `status`: success or error
    - `count`: Number of jobs scraped
    - `jobs`: List of job listings with title, company, location, url
    """
    if not url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="URL must start with http:// or https://")

    try:
        logger.info(f"API Request: Scrape {url}")
        jobs = await scrape_jobs(url=url, headless=True)
        
        return {
            "status": "success",
            "count": len(jobs),
            "jobs": [job.model_dump(mode="json") for job in jobs],
        }
    except Exception as e:
        logger.error(f"API Error: {e}")
        raise HTTPException(status_code=500, detail=f"Scraping failed: {str(e)}")
