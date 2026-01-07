# ThreatShield - Modular Project Structure

## 📁 New Project Structure

```
Phising Email Detector/
│
├── app.py                          # Main Flask app (28 lines - minimal)
├── requirements.txt
├── README.md
├── vercel.json
├── users_db.json
│
├── config/                         # ✅ Configuration
│   ├── __init__.py
│   └── config.py                   # App settings, secrets, paths
│
├── models/                         # ✅ Data models
│   ├── __init__.py
│   └── user.py                     # User database operations
│
├── utils/                          # ✅ Utility functions
│   ├── __init__.py
│   ├── validators.py               # Input validation
│   ├── email_parser.py             # .eml file parsing
│   └── file_handler.py             # File upload/cleanup
│
├── detection/                      # ✅ Phishing detection logic
│   ├── __init__.py
│   ├── patterns.py                 # Keywords, domains, patterns
│   ├── rules.py                    # Detection rule checks
│   └── detector.py                 # Main PhishingDetector class
│
├── routes/                         # ✅ API endpoints
│   ├── __init__.py
│   ├── main.py                     # Homepage route
│   ├── auth.py                     # Login/register/logout
│   └── analysis.py                 # Email analysis endpoints
│
├── api/
│   └── index.py                    # Vercel serverless handler
│
├── static/
│   ├── css/
│   └── js/
│
└── templates/
    └── index.html
```

## 🔧 How to Use the New Structure

### Running the Application
```bash
python app.py
```

### Importing Modules
```python
# In any file, import like this:
from config.config import Config
from models.user import user_db
from detection.detector import PhishingDetector
from utils.validators import validate_registration_input
```

## 📝 Quick Reference

### Adding a New Detection Rule
1. Add pattern to `detection/patterns.py`
2. Add rule logic to `detection/rules.py`
3. Call it from `detection/detector.py`

### Adding a New API Endpoint
1. Create route in appropriate file in `routes/`
2. Import necessary utilities/models
3. Blueprint auto-registers in `app.py`

### Modifying Configurations
- Edit `config/config.py`
- No need to touch other files

## ✅ Benefits
- **Organized**: Each file has one clear purpose
- **Debuggable**: Bugs are easier to locate
- **Testable**: Test individual modules
- **Scalable**: Add features without mess
- **Professional**: Industry-standard structure
