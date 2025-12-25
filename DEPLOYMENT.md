# ThreatShield - Deployment Guide

## Deploy to Vercel

### Prerequisites
- GitHub account
- Vercel account (sign up at [vercel.com](https://vercel.com))
- Git repository pushed to GitHub

### Deployment Steps

1. **Go to Vercel Dashboard**
   - Visit [vercel.com](https://vercel.com)
   - Sign in with your GitHub account

2. **Import Project**
   - Click "Add New" → "Project"
   - Select your repository: `ThreatShield---Phishing-Email-Detector-`
   - Click "Import"

3. **Configure Project**
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Build Command**: Leave empty
   - **Output Directory**: Leave empty
   
4. **Environment Variables** (Optional)
   Add these if needed:
   ```
   FLASK_ENV=production
   ```

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (2-3 minutes)
   - Your app will be live at: `https://your-project-name.vercel.app`

### Important Notes

⚠️ **Limitations on Vercel Free Tier:**
- File uploads are stored in **temporary serverless storage** (will be deleted after function execution)
- Session data is **not persistent** across serverless function invocations
- **10-second execution timeout** for serverless functions
- Not suitable for long-running processes

### Recommended Alternatives for Production

For a production Flask application with file uploads and sessions:

1. **Heroku** (Better for Flask apps)
   - Persistent file storage
   - Better session management
   - Longer execution times

2. **PythonAnywhere**
   - Free tier available
   - Great for Flask applications
   - Persistent storage

3. **Railway**
   - Modern deployment platform
   - Good for Python apps
   - Free tier available

4. **Render**
   - Native Python support
   - Free tier with persistent storage

### Deploy to Heroku Instead (Recommended)

Create `Procfile`:
```
web: gunicorn app:app
```

Add to requirements.txt:
```
gunicorn==21.2.0
```

Then:
```bash
heroku login
heroku create threatshield-detector
git push heroku main
```

### Local Testing

Before deploying, test locally:
```bash
python app.py
```

Visit: `http://localhost:5000`

---

**Note**: Vercel is optimized for static sites and Next.js. For full-stack Flask apps with file uploads, consider the alternatives listed above.
