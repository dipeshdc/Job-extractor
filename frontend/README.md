# Frontend - Job Extractor UI

Next.js frontend for the Job Extractor application.

## Setup

```bash
cd frontend
npm install
```

## Run

### Development
```bash
npm run dev
```

Frontend runs on `http://localhost:3000`

### Production
```bash
npm run build
npm start
```

## Environment Variables

Create `.env.local`:
```
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
```

For production (Vercel), set in Vercel dashboard:
```
NEXT_PUBLIC_BACKEND_URL=https://your-railway-backend.railway.app
```

## Deploy to Vercel

1. Push to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Add environment variable:
   - Key: `NEXT_PUBLIC_BACKEND_URL`
   - Value: `https://your-railway-backend.railway.app`
6. Click "Deploy"

## Features

- 🎯 Clean, modern UI
- ⚡ Real-time job scraping
- 🎨 Beautiful gradient design
- 📱 Fully responsive
- 🔗 Links directly to job postings
- ✨ Smooth animations

## How It Works

1. User enters a job listing URL
2. Clicks "Scrape Jobs"
3. Frontend sends request to backend API
4. Backend scrapes the website with Playwright
5. Results stream back to frontend
6. Jobs displayed in beautiful card layout

## File Structure

```
frontend/
├── pages/
│   ├── _app.js          # App wrapper
│   └── index.js         # Main page
├── styles/
│   ├── globals.css      # Global styles
│   └── Home.module.css  # Component styles
├── package.json
├── next.config.js
└── README.md
```

## Connected to Backend

The frontend communicates with the backend API at:
- Local: `http://localhost:8000/api/scrape`
- Production: `https://your-railway-backend.railway.app/api/scrape`
