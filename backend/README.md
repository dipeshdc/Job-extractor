# Backend API

FastAPI backend that scrapes jobs from any website.

## Setup

```bash
cd backend
pip install -r requirements.txt
playwright install
```

## Run

### Development
```bash
python main.py
# or
bash run_dev.sh
```

API runs on `http://localhost:8000`

### Production
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API Endpoints

### GET `/health`
Health check endpoint.

```bash
curl http://localhost:8000/health
```

### GET `/api/scrape`
Scrape jobs from a URL.

**Query Parameters:**
- `url` (required): The job listing URL to scrape

**Example:**
```bash
curl "http://localhost:8000/api/scrape?url=https://realpython.github.io/fake-jobs/"
```

**Response:**
```json
{
  "status": "success",
  "count": 100,
  "jobs": [
    {
      "title": "Senior Python Developer",
      "company": "Payne, Roberts and Davis",
      "location": "Stewartbury, AA",
      "url": "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
    }
  ]
}
```

## Deploy to Railway

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Select your repository
5. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables (if needed)
7. Deploy!

Railway will automatically assign a public URL like: `https://job-extractor-api.railway.app`
