# 🚀 Quick Deploy Guide (5 Minutes)

## Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Ready for deployment"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

## Step 2: Deploy on Render.com

1. Go to **https://render.com** → Sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo
4. Settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn ToDoApp.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: **Free**
5. Click **"Create Web Service"**

## Step 3: Add Database

1. **"New +"** → **"PostgreSQL"**
2. **Plan**: **Free**
3. Copy the **Internal Database URL**
4. Go back to Web Service → **Environment** → Add:
   - **Key**: `DATABASE_URL`
   - **Value**: (paste the database URL)

## Step 4: Get Your Link! 🎉

Your app will be live at: `https://your-app-name.onrender.com`

**Share this link on LinkedIn, GitHub, your portfolio!**

---

📖 **Full guide**: See `DEPLOYMENT.md` for detailed instructions

