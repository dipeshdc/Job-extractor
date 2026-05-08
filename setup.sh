#!/bin/bash

echo "🚀 Job Extractor - Full Stack Setup"
echo "===================================="
echo ""

# Backend setup
echo "📦 Setting up Backend..."
cd backend
pip install -r requirements.txt
playwright install
echo "✅ Backend ready! Run: python main.py"
echo ""

# Frontend setup
echo "📦 Setting up Frontend..."
cd ../frontend
npm install
echo "✅ Frontend ready! Run: npm run dev"
echo ""

echo "🎯 Next steps:"
echo "1. Terminal 1: cd backend && python main.py"
echo "2. Terminal 2: cd frontend && npm run dev"
echo "3. Open: http://localhost:3000"
echo ""
echo "🎉 Happy scraping!"
