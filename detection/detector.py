"""
Main phishing detector class
"""
from detection.rules import DetectionRules

class PhishingDetector:
    """Rule-based phishing detection system"""
    
    def __init__(self):
        self.risk_score = 0
        self.flags = []
        self.details = {}
    
    def analyze_email(self, email_data):
        """Analyze email using rule-based heuristics"""
        self.risk_score = 0
        self.flags = []
        self.details = {}
        
        sender = email_data.get('sender', '')
        subject = email_data.get('subject', '')
        body = email_data.get('body', '')
        headers = email_data.get('headers', {})
        attachments = email_data.get('attachments', [])
        
        # Run all detection rules
        score, flags, details = DetectionRules.check_sender_authenticity(sender, headers)
        self.risk_score += score
        self.flags.extend(flags)
        self.details.update(details)
        
        score, flags = DetectionRules.check_subject_patterns(subject)
        self.risk_score += score
        self.flags.extend(flags)
        
        score, flags = DetectionRules.check_body_content(body)
        self.risk_score += score
        self.flags.extend(flags)
        
        score, flags, details = DetectionRules.check_urls(body)
        self.risk_score += score
        self.flags.extend(flags)
        self.details.update(details)
        
        score, flags = DetectionRules.check_attachments(attachments)
        self.risk_score += score
        self.flags.extend(flags)
        
        score, flags = DetectionRules.check_headers(headers)
        self.risk_score += score
        self.flags.extend(flags)
        
        score, flags = DetectionRules.check_urgency_language(subject, body)
        self.risk_score += score
        self.flags.extend(flags)
        
        # Calculate final classification
        classification = self._get_classification()
        
        return {
            'risk_score': self.risk_score,
            'classification': classification,
            'flags': self.flags,
            'details': self.details
        }
    
    def _get_classification(self):
        """Determine final classification based on risk score"""
        if self.risk_score >= 60:
            return 'PHISHING'
        elif self.risk_score >= 30:
            return 'SUSPICIOUS'
        else:
            return 'SAFE'
