# ThreatShield - Email Phishing Detection System

A professional, enterprise-grade email phishing detection web application using **rule-based and heuristic analysis**. This system provides comprehensive security analysis without relying on AI or Machine Learning, using deterministic detection rules instead.

## Features

### Security Analysis
- **Rule-Based Detection**: Deterministic phishing detection using security heuristics
- **Sender Validation**: Email authentication checks (SPF, DKIM analysis)
- **URL Analysis**: Malicious link detection and suspicious domain identification
- **Content Pattern Matching**: Phishing keyword and urgency language detection
- **Header Inspection**: Email header analysis for spoofing attempts
- **Risk Scoring**: Comprehensive threat assessment with severity classification

### Professional Interface
- **Enterprise-Grade UI**: Clean, minimal cybersecurity dashboard design
- **Dark Theme**: Professional neutral color palette optimized for security operations
- **Responsive Design**: Full support for desktop, tablet, and mobile devices
- **Dual Analysis Modes**: Manual email analysis and .eml file upload
- **Real-Time Results**: Detailed threat assessment with risk scoring

### Authentication System
- Secure login/signup with password hashing
- Session management
- User-friendly modal-based authentication

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with enterprise design system
- **Security**: Rule-based detection engine (no ML/AI)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone or navigate to the project directory**
   ```bash
   cd "d:\Projects\Phising Email Detector"
   ```

2. **Install required Python packages**
   ```bash
   pip install flask werkzeug
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`

## Usage Guide

### Getting Started

1. **Create an Account**
   - Click "Create Account" on the login modal
   - Enter username, email, and password (min 8 characters)
   - Submit to register

2. **Sign In**
   - Use your credentials to access the dashboard

### Analyzing Emails

#### Manual Analysis
1. Select the "Manual Analysis" tab
2. Enter the email details:
   - Sender email address
   - Subject line
   - Email body content
3. Click "Analyze Email"
4. Review the comprehensive threat assessment

#### File Upload Analysis
1. Select the "File Upload (.eml)" tab
2. Drag and drop an .eml file or click to browse
3. Click "Analyze File"
4. Review results with email preview

### Understanding Results

The analysis provides:

- **Risk Score (0-100)**: Numerical threat assessment
- **Classification**: 
  - **SAFE**: No significant threats detected
  - **SUSPICIOUS**: Caution advised, verification needed
  - **PHISHING**: High-confidence phishing attempt

- **Detection Flags**: Specific security issues identified
- **Technical Details**: Sender domain, URL analysis, timestamps

## Detection Rules

The system implements multiple security heuristics:

### Sender Authentication
- SPF validation checks
- DKIM signature verification
- Domain spoofing detection
- Display name vs. email mismatch

### URL Analysis
- IP address usage in links
- Suspicious TLD detection (.tk, .ml, .ga, etc.)
- URL shortener identification
- Excessive URL counting

### Content Analysis
- Phishing keyword detection
- Urgency language patterns
- Request for personal information
- Poor formatting indicators

### Header Analysis
- Return-Path mismatches
- Multiple mail server hops
- Missing authentication headers

### Attachment Scanning
- Suspicious file extensions
- Double extension detection

## Project Structure

```
Phising Email Detector/
├── app.py                      # Flask backend with detection engine
├── templates/
│   └── index.html             # Main application interface
├── static/
│   ├── css/
│   │   └── style.css          # Enterprise-grade styling
│   └── js/
│       └── main.js            # Frontend application logic
├── uploads/                    # Temporary file storage
└── README.md                  # Documentation
```

## Security Considerations

- **No AI/ML**: Pure rule-based detection for transparency and explainability
- **Password Hashing**: Werkzeug security for credential storage
- **Session Management**: Secure Flask sessions
- **File Validation**: .eml file type verification
- **Input Sanitization**: XSS prevention in user inputs

## Design Philosophy

The interface follows enterprise cybersecurity standards:

- **Neutral Color Palette**: Dark charcoal with muted green accents
- **Professional Typography**: Inter font family for readability
- **Minimal UI**: Clean, distraction-free security focus
- **SOC-Style Dashboard**: Designed for security operations centers
- **Accessibility**: WCAG-compliant contrast and keyboard navigation

## Future Enhancements

Potential improvements:
- Database integration for user persistence
- Email parsing enhancement
- Additional detection rules
- Export analysis reports (PDF/JSON)
- Batch file processing
- API endpoint for integrations

## Support

For issues or questions, please refer to the project documentation.

---

**Note**: This is a rule-based detection system designed for educational purposes. For production use, integrate with comprehensive email security infrastructure and consider additional validation layers.
