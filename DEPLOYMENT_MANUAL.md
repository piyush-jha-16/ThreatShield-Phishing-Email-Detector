# ThreatShield - Manual Deployment Guide for Vercel

## Deploy to Vercel via Website (Step-by-Step)

### Step 1: Create Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Click **"Sign Up"** in the top-right corner
3. Choose **"Continue with GitHub"**
4. Authorize Vercel to access your GitHub account
5. Complete the signup process

### Step 2: Access Vercel Dashboard
1. After logging in, you'll be on the Vercel Dashboard
2. You should see "Let's build something new" or your existing projects

### Step 3: Import Your Project
1. Click the **"Add New..."** button (top-right)
2. Select **"Project"** from the dropdown menu
3. You'll see "Import Git Repository" page

### Step 4: Connect GitHub Repository
1. If this is your first time:
   - Click **"Install Vercel for GitHub"**
   - Select your GitHub account
   - Choose either:
     - **"All repositories"** OR
     - **"Only select repositories"** and choose `ThreatShield-Phishing-Email-Detector-`
   - Click **"Install"**

2. After installation:
   - Your repository will appear in the list
   - Find **"ThreatShield-Phishing-Email-Detector-"**
   - Click **"Import"** button next to it

### Step 5: Configure Project Settings
1. **Project Name**: 
   - Keep auto-generated name or change to: `phising-email-detector`

2. **Framework Preset**: 
   - Select **"Other"** from dropdown

3. **Root Directory**: 
   - Leave as **"./"** (default)

4. **Build Settings**:
   - **Build Command**: Leave blank (Vercel will use vercel.json)
   - **Output Directory**: Leave blank
   - **Install Command**: Leave as default (`pip install -r requirements.txt`)

5. **Environment Variables** (Optional):
   - Click **"Environment Variables"** to expand
   - Add if needed:
     - **Key**: `FLASK_ENV`
     - **Value**: `production`
   - Click **"Add"**

### Step 6: Deploy
1. Review all settings
2. Click the big **"Deploy"** button at the bottom
3. Wait for deployment (typically 1-3 minutes)
4. You'll see:
   - Building logs in real-time
   - "Building..." → "Deploying..." → "Ready"

### Step 7: Access Your Live Application
1. Once complete, you'll see:
   - 🎉 **Congratulations** message
   - **Production URL**: `https://phising-email-detector.vercel.app`
   - **Visit** button to open your app

2. Click **"Visit"** or copy the URL
3. Your ThreatShield app is now live!

### Step 8: View Deployment Details
1. Click on your project name
2. You'll see:
   - **Deployments** tab - all deployment history
   - **Settings** tab - project configuration
   - **Domains** tab - custom domain setup
   - **Analytics** tab - usage statistics

---

## Managing Future Deployments

### Automatic Deployments (Recommended)
Once connected, Vercel automatically deploys when you push to GitHub:
```bash
git add .
git commit -m "Update message"
git push origin main
```
- Vercel detects the push and deploys automatically
- Check deployment status on Vercel dashboard

### Manual Redeployment via Website
1. Go to Vercel Dashboard
2. Select your project
3. Click **"Deployments"** tab
4. Find latest deployment
5. Click **"⋯"** (three dots)
6. Select **"Redeploy"**

---

## Important Notes

### ⚠️ Vercel Limitations for Flask Apps:
- **File uploads** are stored in temporary serverless storage (deleted after execution)
- **Session data** is not persistent across serverless function invocations
- **10-second timeout** for serverless functions
- Not ideal for long-running processes

### ✅ What Works on Vercel:
- Login/Registration (temporary sessions)
- Manual email analysis
- .eml file upload and analysis (temporary)
- All UI features

---

## Troubleshooting

### If deployment fails:
1. Check **Build Logs** in deployment details
2. Verify `vercel.json` is in your repository
3. Ensure `requirements.txt` has all dependencies
4. Check Python version compatibility

### If app doesn't work correctly:
1. Check **Function Logs** in deployment details
2. Click on your deployment → **"View Function Logs"**
3. Look for error messages

### Common Issues:
- **Session not persisting**: Normal on Vercel, users need to login each visit
- **File upload lost**: Expected behavior with serverless functions
- **Timeout errors**: Function took longer than 10 seconds

---

## Alternative Deployment Options (Recommended for Production)

### Heroku (Better for Flask)
1. Create account at [heroku.com](https://heroku.com)
2. Install Heroku CLI
3. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
4. Add to requirements.txt:
   ```
   gunicorn==21.2.0
   ```
5. Deploy:
   ```bash
   heroku login
   heroku create threatshield-detector
   git push heroku main
   ```

### Railway
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project"
4. Select your repository
5. Railway auto-detects Python and deploys

### Render
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Select your repository
5. Choose "Python" as environment
6. Deploy

---

## Your Current Deployment

**Live URL**: https://phising-email-detector.vercel.app

**Repository**: https://github.com/piyush-jha-16/ThreatShield-Phishing-Email-Detector-

**Status**: ✅ Active and Deployed

---

For questions or issues, check the Vercel documentation: [vercel.com/docs](https://vercel.com/docs)
