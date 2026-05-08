# 💼 Job Extractor

A full-stack web scraping application that extracts job listings from any website in real-time. Built with **Python FastAPI** backend and **Next.js React** frontend. Deploy free on **Vercel + Railway**.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green?style=flat-square)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black?style=flat-square)](https://nextjs.org/)
[![Vercel](https://img.shields.io/badge/Vercel-Deploy-blue?style=flat-square)](https://vercel.com/)
[![Railway](https://img.shields.io/badge/Railway-Deploy-0b0d0e?style=flat-square)](https://railway.app/)

---

## ✨ Features

✅ **Real-time Job Scraping** - Extract jobs from any website instantly  
✅ **Beautiful UI** - Modern, responsive React interface  
✅ **Async Backend** - Non-blocking Playwright scraper  
✅ **No Database** - Pure scraping, no storage needed  
✅ **Free Deployment** - Vercel (frontend) + Railway (backend)  
✅ **Production Ready** - Error handling, logging, CORS  
✅ **Fully Configurable** - Support any website structure  
✅ **Portfolio Project** - Perfect for internships/interviews  

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Git

### Local Development

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
playwright install
python main.py
```
✅ Backend: `http://localhost:8000`

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```
✅ Frontend: `http://localhost:3000`

**Open:** `http://localhost:3000` and start scraping! 🎉

---

## 📋 How It Works

```
User enters URL
    ↓
Clicks "Scrape Jobs"
    ↓
Frontend calls Backend API
    ↓
Backend launches Playwright
    ↓
Extracts job data
    ↓
Returns beautiful JSON
    ↓
Frontend displays results ✨
```

---

## 📁 Project Structure

```
job_extractor/
├── backend/                 # Python FastAPI
│   ├── main.py             # FastAPI app
│   ├── app/
│   │   ├── scraper.py      # Playwright logic
│   │   ├── models.py       # Pydantic models
│   │   ├── config.py       # CSS selectors
│   │   └── routes/
│   │       └── scraper_routes.py  # /api/scrape
│   ├── requirements.txt
│   └── README.md
│
├── frontend/                # Next.js React
│   ├── pages/
│   │   └── index.js        # Main page
│   ├── styles/
│   │   └── Home.module.css # Beautiful styles
│   ├── package.json
│   ├── .env.local
│   └── README.md
│
├── setup.sh                # Quick setup
├── COMPREHENSIVE_README.md # Full documentation ⭐
└── .gitignore
```

---

## 🔌 API Endpoints

### GET `/health`
Check if backend is alive.
```bash
curl http://localhost:8000/health
```

### GET `/api/scrape?url={url}`
Scrape jobs from a URL.
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
      "company": "Tech Company",
      "location": "Remote",
      "url": "https://..."
    }
  ]
}
```

---

## 📤 Deployment

### Deploy Backend (Railway - $5 free credit)

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. "New Project" → "Deploy from GitHub"
4. Select repository
5. Railway auto-detects Python and deploys ✅

**Get URL:** `https://your-backend.railway.app`

### Deploy Frontend (Vercel - Free)

1. Push to GitHub
2. Go to [vercel.com](https://vercel.com)
3. "New Project" → "Import from GitHub"
4. Add environment variable:
   ```
   NEXT_PUBLIC_BACKEND_URL = https://your-backend.railway.app
   ```
5. Deploy ✅

**Get URL:** `https://your-app.vercel.app`

---

## 💰 Cost

| Service | Tier | Cost |
|---------|------|------|
| Vercel | Free | $0 |
| Railway | Free Trial | $0* |
| **Total** | - | **$0/month** 🎉 |

*After $5 credit (~2-3 months), $5/month for hobby tier

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Playwright, Pydantic
- **Frontend:** Next.js, React, CSS Modules
- **Deployment:** Vercel, Railway

---

## 🔧 Configuration

To support different websites, edit `backend/app/config.py`:

```python
@dataclass(frozen=True)
class ScrapeConfig:
    card_selector: str = "div.job-card"
    title_selector: str = "h2.title"
    company_selector: str = "h3.company"
    location_selector: str = "p.location"
    link_selector: str = "a.apply"
```

Find selectors by inspecting any job card on your target website.

---

## 📚 Documentation

- **Full Guide:** See `COMPREHENSIVE_README.md` for detailed setup, deployment, troubleshooting
- **Backend Docs:** See `backend/README.md`
- **Frontend Docs:** See `frontend/README.md`

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Backend fails to start | Run `playwright install` |
| Connection refused | Ensure backend is running on port 8000 |
| No jobs appear | Check `.env.local` has correct backend URL |
| Frontend blank | Open browser console (F12) for errors |

---

## 💡 Portfolio Tips

✨ **Showcase This Project:**
- Deploy it live (Vercel + Railway)
- Add GitHub repository link
- Write about your tech choices
- mention in interviews/resume

**Interview Talking Points:**
- "Built async Playwright scraper for performance"
- "Separated frontend/backend for independent scaling"
- "Deployed full-stack app on free tier"
- "Implemented real-time streaming frontend"

---

## 📄 License

MIT - Feel free to use for anything!

---

## 🎯 Next Steps

```bash
# 1. Setup locally
bash setup.sh

# 2. Test it works
# Open http://localhost:3000

# 3. Deploy to production
# Follow deployment section above

# 4. Share on portfolio!
```

**Ready? Start with:** `bash setup.sh` 🚀

---

**For detailed setup, configuration, and troubleshooting:** See [COMPREHENSIVE_README.md](COMPREHENSIVE_README.md)
