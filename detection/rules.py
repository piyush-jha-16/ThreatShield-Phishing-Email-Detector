"""
Detection rules for phishing analysis
"""
import re
from urllib.parse import urlparse
from detection.patterns import (
    SUSPICIOUS_KEYWORDS, SUSPICIOUS_DOMAINS, LEGITIMATE_DOMAINS,
    TYPOSQUATTING_CHARS, SUSPICIOUS_EXTENSIONS, URL_SHORTENERS,
    URGENCY_PATTERNS, PERSONAL_INFO_PATTERNS
)

class DetectionRules:
    """Collection of detection rules for phishing analysis"""
    
    @staticmethod
    def check_typosquatting(domain):
        """Detect typosquatting attempts against known brands"""
        for legit_domain in LEGITIMATE_DOMAINS:
            legit_name = legit_domain.split('.')[0]
            
            if len(legit_name) >= 4:
                for i, char in enumerate(legit_name):
                    if char in TYPOSQUATTING_CHARS:
                        for replacement in TYPOSQUATTING_CHARS[char]:
                            typo_variant = legit_name[:i] + replacement + legit_name[i+1:]
                            if typo_variant in domain and legit_domain not in domain:
                                return legit_name, typo_variant
        return None, None
    
    @staticmethod
    def check_sender_authenticity(sender, headers):
        """Check sender email and domain authenticity"""
        flags = []
        risk_score = 0
        details = {}
        
        if not sender:
            risk_score += 20
            flags.append('Missing sender information')
            return risk_score, flags, details
        
        # Extract domain
        match = re.search(r'@([\w\.-]+)', sender)
        if match:
            domain = match.group(1).lower()
            details['sender_domain'] = domain
            
            # Check for suspicious TLDs
            for suspicious_tld in SUSPICIOUS_DOMAINS:
                if domain.endswith(suspicious_tld):
                    risk_score += 25
                    flags.append(f'Suspicious domain TLD: {suspicious_tld}')
            
            # Check for typosquatting
            legit_brand, typo_variant = DetectionRules.check_typosquatting(domain)
            if legit_brand:
                risk_score += 50
                flags.append(f'TYPOSQUATTING DETECTED: Domain mimics "{legit_brand}" using character substitution ({typo_variant})')
            
            # Check for domain spoofing attempts
            for legit_domain in LEGITIMATE_DOMAINS:
                if legit_domain in domain and domain != legit_domain:
                    risk_score += 40
                    flags.append(f'Possible domain spoofing: mimicking {legit_domain}')
        
        # Check for display name mismatch
        display_match = re.match(r'^(.+?)\s*<(.+?)>$', sender)
        if display_match:
            display_name = display_match.group(1).strip()
            email_addr = display_match.group(2).strip()
            
            for legit_domain in LEGITIMATE_DOMAINS:
                company_name = legit_domain.split('.')[0]
                if company_name.lower() in display_name.lower():
                    if legit_domain not in email_addr.lower():
                        risk_score += 35
                        flags.append(f'Display name spoofing: claims to be {company_name}')
        
        # Check SPF, DKIM, DMARC from headers
        spf = headers.get('Received-SPF', '').lower()
        if 'fail' in spf:
            risk_score += 30
            flags.append('SPF authentication failed')
        
        dkim = headers.get('DKIM-Signature', '')
        if not dkim and risk_score > 0:
            risk_score += 10
            flags.append('Missing DKIM signature')
        
        return risk_score, flags, details
    
    @staticmethod
    def check_subject_patterns(subject):
        """Analyze subject line for phishing patterns"""
        flags = []
        risk_score = 0
        
        if not subject:
            return risk_score, flags
        
        subject_lower = subject.lower()
        
        # Check for suspicious keywords
        found_keywords = [kw for kw in SUSPICIOUS_KEYWORDS if kw in subject_lower]
        
        if found_keywords:
            risk_score += len(found_keywords) * 8
            flags.append(f'Suspicious keywords in subject: {", ".join(found_keywords[:3])}')
        
        # Check for excessive punctuation
        if subject.count('!') >= 2 or subject.count('?') >= 2:
            risk_score += 10
            flags.append('Excessive punctuation in subject')
        
        # Check for all caps
        if subject.isupper() and len(subject) > 10:
            risk_score += 12
            flags.append('Subject in all capitals')
        
        return risk_score, flags
    
    @staticmethod
    def check_body_content(body):
        """Analyze email body content"""
        flags = []
        risk_score = 0
        
        if not body:
            return risk_score, flags
        
        body_lower = body.lower()
        
        # Check for suspicious keywords
        found_keywords = [kw for kw in SUSPICIOUS_KEYWORDS if kw in body_lower]
        
        if found_keywords:
            risk_score += len(found_keywords) * 5
            if len(found_keywords) > 3:
                flags.append(f'Multiple suspicious keywords: {", ".join(found_keywords[:3])}...')
        
        # Check for requests for personal information
        for pattern in PERSONAL_INFO_PATTERNS:
            if re.search(pattern, body_lower):
                risk_score += 25
                flags.append('Requests personal/financial information')
                break
        
        # Check for poor formatting
        if re.search(r'\s{3,}', body) or body.count('\n\n\n') > 2:
            risk_score += 8
            flags.append('Poor formatting detected')
        
        return risk_score, flags
    
    @staticmethod
    def check_urls(body):
        """Extract and analyze URLs in email body"""
        flags = []
        risk_score = 0
        details = {}
        
        if not body:
            return risk_score, flags, details
        
        # Find all URLs
        url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        urls = re.findall(url_pattern, body)
        
        if not urls:
            return risk_score, flags, details
        
        details['url_count'] = len(urls)
        suspicious_urls = []
        
        for url in urls[:10]:
            parsed = urlparse(url if url.startswith('http') else 'http://' + url)
            domain = parsed.netloc.lower()
            
            # Check for IP addresses
            if re.match(r'\d+\.\d+\.\d+\.\d+', domain):
                risk_score += 30
                suspicious_urls.append(url[:50])
                flags.append('URL uses IP address instead of domain')
            
            # Check for suspicious TLDs
            for suspicious_tld in SUSPICIOUS_DOMAINS:
                if domain.endswith(suspicious_tld):
                    risk_score += 20
                    suspicious_urls.append(url[:50])
                    break
            
            # Check for URL shorteners
            if any(shortener in domain for shortener in URL_SHORTENERS):
                risk_score += 15
                flags.append('Contains URL shortener links')
            
            # Check for misleading URLs
            if '@' in parsed.netloc:
                risk_score += 35
                flags.append('Misleading URL with @ symbol')
        
        if len(urls) > 5:
            risk_score += 10
            flags.append(f'Excessive number of URLs: {len(urls)}')
        
        if suspicious_urls:
            details['suspicious_urls'] = suspicious_urls[:3]
        
        return risk_score, flags, details
    
    @staticmethod
    def check_attachments(attachments):
        """Analyze email attachments"""
        flags = []
        risk_score = 0
        
        if not attachments:
            return risk_score, flags
        
        for attachment in attachments:
            name = attachment.lower()
            for ext in SUSPICIOUS_EXTENSIONS:
                if name.endswith(ext):
                    risk_score += 40
                    flags.append(f'Suspicious attachment type: {ext}')
                    break
            
            # Check for double extensions
            if name.count('.') >= 2:
                risk_score += 25
                flags.append('Double extension in attachment')
        
        return risk_score, flags
    
    @staticmethod
    def check_headers(headers):
        """Analyze email headers"""
        flags = []
        risk_score = 0
        
        # Check for mismatched return paths
        from_addr = headers.get('From', '')
        return_path = headers.get('Return-Path', '')
        
        if from_addr and return_path:
            from_domain = re.search(r'@([\w\.-]+)', from_addr)
            return_domain = re.search(r'@([\w\.-]+)', return_path)
            
            if from_domain and return_domain:
                if from_domain.group(1) != return_domain.group(1):
                    risk_score += 20
                    flags.append('Mismatched sender and return-path domains')
        
        # Check for multiple received headers
        received = headers.get('Received', '')
        if isinstance(received, list):
            if len(received) > 5:
                risk_score += 10
                flags.append('Multiple mail server hops detected')
        
        return risk_score, flags
    
    @staticmethod
    def check_urgency_language(subject, body):
        """Check for urgency and pressure tactics"""
        flags = []
        risk_score = 0
        
        text = (subject + ' ' + body).lower()
        urgency_count = sum(1 for pattern in URGENCY_PATTERNS if pattern in text)
        
        if urgency_count >= 3:
            risk_score += 20
            flags.append('Creates false sense of urgency')
        elif urgency_count >= 2:
            risk_score += 10
        
        return risk_score, flags
