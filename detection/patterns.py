"""
Phishing detection patterns and constants
"""

# Suspicious keywords commonly found in phishing emails
SUSPICIOUS_KEYWORDS = [
    'urgent', 'verify account', 'suspended', 'confirm identity', 'click here',
    'verify your account', 'unusual activity', 'security alert', 'act now',
    'limited time', 'expire', 'update payment', 'billing problem', 'prize',
    'winner', 'congratulations', 'claim', 'free money', 'nigerian prince',
    'inheritance', 'tax refund', 'irs', 'bitcoin', 'cryptocurrency wallet'
]

# Suspicious domain TLDs
SUSPICIOUS_DOMAINS = [
    '.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.work', '.click',
    '.link', '.zip', '.download'
]

# Legitimate domains for spoofing detection
LEGITIMATE_DOMAINS = [
    'google.com', 'microsoft.com', 'apple.com', 'amazon.com', 'facebook.com',
    'linkedin.com', 'twitter.com', 'github.com', 'stackoverflow.com', 'paypal.com',
    'netflix.com', 'instagram.com', 'yahoo.com', 'dropbox.com', 'spotify.com'
]

# Common typosquatting character substitutions
TYPOSQUATTING_CHARS = {
    'a': ['4', '@'],
    'e': ['3'],
    'i': ['1', '!', 'l'],
    'l': ['1', 'i', '!'],
    'o': ['0'],
    's': ['5', '$'],
    't': ['7'],
    'g': ['9'],
    'b': ['8']
}

# Suspicious file extensions
SUSPICIOUS_EXTENSIONS = [
    '.exe', '.scr', '.bat', '.cmd', '.com', '.pif', '.vbs', '.js',
    '.jar', '.zip', '.rar', '.iso', '.dll'
]

# URL shorteners
URL_SHORTENERS = [
    'bit.ly', 'tinyurl.com', 'goo.gl', 't.co', 'ow.ly'
]

# Urgency patterns
URGENCY_PATTERNS = [
    'immediately', 'urgent', 'action required', 'act now',
    'within 24 hours', 'expire', 'suspend', 'limited time',
    'today only', 'last chance'
]

# Personal information request patterns
PERSONAL_INFO_PATTERNS = [
    r'social security', r'credit card', r'password', r'pin\s*code',
    r'account\s*number', r'routing\s*number', r'date\s*of\s*birth'
]
